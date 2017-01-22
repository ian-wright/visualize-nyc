
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/atrain/")
def atrain():
	return render_template("atrain.html")


if __name__ = '__main__':
    app.run()