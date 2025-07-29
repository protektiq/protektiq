from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/greet")
def greet():
    name = request.args.get("name")
    # Vulnerable to XSS
    return f"<h1>Hello {name}</h1>"

@app.route("/read_file")
def read_file():
    filename = request.args.get("file")
    # Vulnerable to path traversal
    with open(filename, "r") as f:
        return f.read()

@app.route("/exec")
def exec_cmd():
    cmd = request.args.get("cmd")
    # Vulnerable to command injection
    return os.popen(cmd).read()

if __name__ == "__main__":
    app.run(debug=True) 