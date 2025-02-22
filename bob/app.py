from flask import Flask
import os
import requests

app = Flask(__name__)

@app.route('/')
def status():
    ip_addr = os.getenv('IP', '127.0.0.1')  # Use the host's IP address
    port = os.getenv('PORT', '5000')
    try:
        response = requests.get(f'http://{ip_addr}:{port}')
        response.raise_for_status()
        data = response.text
    except requests.RequestException as e:
        data = f"Error: {e}"
    return data + " is a silly gooses"
