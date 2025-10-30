from flask import Flask
app = Flask(__name__)
import os

@app.route('/')
def hello_geek():
    pod_name = os.environ.get("HOSTNAME", "Unknown Pod")
    return f'<div style="text-align: center;"><h1>Hello from GCP K8s!</h1><p>Welcome to GCP DevOps Course.</p><p>Pod Name: {pod_name}</p></div>'
    #return '<div style=\"text-align: center;\"><h1>Hello from GCP K8s!</h1><p>Welcome to GCP DevOps Course.</p><p></p></div>'


if __name__ == "__main__":
    app.run(debug=True)