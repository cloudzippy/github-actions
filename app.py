from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello() -> tuple:
    return jsonify(message="Hello from Flask in Docker!"), 200


@app.route("/health")
def health() -> tuple:
    return jsonify(status="ok"), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
