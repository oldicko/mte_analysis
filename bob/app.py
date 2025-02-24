from flask import Flask
import os
import requests

app = Flask(__name__)

@app.route('/')
def status():
    ip_addr = os.getenv('IP', '127.0.0.1')  # Use the host's IP address
    port = os.getenv('PORT', '80')
    upstream = os.getenv('UPSTREAM')
    headers = {
        'x-mte-outbound-token': 'TokenTokenTokenToken',
        'x-mte-upstream': upstream
    }
    try:
        response = requests.get(f'http://{ip_addr}:{port}/status', headers=headers)  # Ensure the correct path is used
        response.raise_for_status()
        data = response.text
    except requests.RequestException as e:
        data = f"Error: {e}"
    return data + " is a silly gooses"
