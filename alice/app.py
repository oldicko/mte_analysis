from flask import Flask
from datetime import datetime

app = Flask(__name__)

call_count = 0

def get_current_time_string():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@app.route('/status')
def status():
    global call_count
    call_count += 1
    current_time = get_current_time_string()
    return f"{current_time} - Eclypses"

@app.route('/count')
def count():
    return f"The route has been called {call_count} times."
