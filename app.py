

from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/")
def root():
    return redirect(url_for("home"))


@app.route("/home")
def home():
    return render_template("base_home.html")


@app.route("/child0")
def child0():
    return render_template("base_child0.html")


@app.route("/child1")
def child1():
    return render_template("base_child1.html")


if __name__ == '__main__':
    app.run(debug=True)
