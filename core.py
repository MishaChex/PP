import flask


app = flask.Flask(__name__)
app.config["DEBUG"] = False


@app.route("/api/v1/hello-world-<int:variant>", methods=["GET"])
def index(variant):
    """Endpoint return number of variant(must be int)"""
    return f"Hello world {variant}"


if __name__ == '__main__':
    app.run()
