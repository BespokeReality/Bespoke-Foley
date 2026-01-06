from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    """
    Return index.html template.
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
