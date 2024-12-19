from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    
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
