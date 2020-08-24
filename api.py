from flask import Flask, jsonify

app = Flask(__name__)


healthz = [
        {
            "status": "OK",
            "version": "0.0.1",
            "uptime": "up since 2020-08-24 11:00:00"
        }
    ]


@app.route("/")
def helloWorld():
    return jsonify(data="Hello!")
@app.route("/healthz", methods=["GET"])
def gethealthz():
    return jsonify(healthz)


if __name__ == "__main__":
    app.run(port=8080)