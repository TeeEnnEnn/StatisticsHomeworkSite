from flask import Blueprint, render_template

main = Blueprint("main", __name__)


@main.route("/", methods=["GET", "POST"])
def home():
    functions = ["normal", "mean", "mode", "median", "variance", "standard deviation", "covariance", "pooled variance", "t-distribution"]
    return render_template("home.html", functions=functions)
