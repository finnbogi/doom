from flask import Flask, render_template, send_from_directory
import socket
import os

app = Flask(__name__)

@app.route('/')
def index():
    container_name = socket.gethostname()
    container_ip = socket.gethostbyname(container_name)

    return render_template('index.html', pod_name=pod_name, pod_ip=pod_ip)

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)