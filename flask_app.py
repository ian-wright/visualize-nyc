
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html", comments=comments)

    # otherwise, it's a POST
    comments.append(request.form["contents"])
    return redirect(url_for('index'))


@app.route("/atrain/")
def atrain():
	return render_template("atrain.html")

if __name__ = '__main__':
    app.run()