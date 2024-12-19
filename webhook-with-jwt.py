from flask import Flask, request, jsonify
import subprocess
import jwt
from datetime import datetime, timedelta

app = Flask(__name__)


SECRET_KEY = "your-secret-key"


def create_token():
    payload = {
        "sub": "webhook",  # Subject of the token
        "iat": datetime.utcnow(),  # Issued at
        "exp": datetime.utcnow() + timedelta(minutes=30)  # Expiry time
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

@app.route('/webhook', methods=['POST'])
def webhook():
   
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        return jsonify({"error": "Authorization header missing"}), 401

    
    token = auth_header.split()[-1]  # Expects "Bearer <token>"
    try:
        
        jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Token expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"error": "Invalid token"}), 401

    
    data = request.get_json()
    print(f"Received webhook data: {data}")

    try:
        # Execute the Ansible playbook
        subprocess.run(["ansible-playbook", "/path/to/your-playbook.yml"], check=True)
        return "Ansible playbook executed successfully", 200
    except subprocess.CalledProcessError:
        return "Error executing Ansible playbook", 500

if __name__ == '__main__':
    print("Use this JWT for testing:")
    print(create_token())  # Generate a JWT for testing
    app.run(host='0.0.0.0', port=5000)
