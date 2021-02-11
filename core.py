from flask import Flask
from wsgiref.simple_server import make_server
app = Flask(__name__)
app.config["DEBUG"] = False

@app.route('/')
def hello_world():
    return 'Hello world'

@app.route("/api/v1/hello-world-<int:variant>", methods=["GET"])
def index(variant):
    """Endpoint return number of variant(must be int)"""
    return f"Hello world {variant}"
if __name__ == '__main__':
    with make_server('', 5000, app) as server:
        print("Super?")

        server.serve_forever()