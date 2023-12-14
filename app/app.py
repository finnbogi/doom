from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    pod_name = os.getenv('HOSTNAME', 'Unknown Pod Name')
    pod_ip = os.getenv('POD_IP', 'Unknown Pod IP')

    return render_template('index.html', pod_name=pod_name, pod_ip=pod_ip)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)