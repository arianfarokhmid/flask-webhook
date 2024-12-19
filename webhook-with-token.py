from flask import Flask, request, jsonify
import os
import subprocess

app = Flask(__name__)


AUTH_TOKEN = os.getenv("AUTH_TOKEN")

@app.route('/webhook', methods=['POST'])
def webhook():
    
    if not AUTH_TOKEN:
        return jsonify({"error": "Server configuration error: AUTH_TOKEN not set"}), 500

    
    token = request.headers.get("Authorization")  
    if not token or token.split()[-1] != AUTH_TOKEN:
        return jsonify({"error": "Unauthorized"}), 401

    if request.method == 'POST':
        data = request.get_json() 
        print(f"Received webhook data: {data}")

        try:
            
            subprocess.run(["ansible-playbook", "/path/to/your-playbook.yml"], check=True)
            return "Ansible playbook executed successfully", 200
        except subprocess.CalledProcessError:
            return "Error executing Ansible playbook", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
