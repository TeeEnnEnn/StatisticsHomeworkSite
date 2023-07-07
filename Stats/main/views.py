from flask import Blueprint, render_template, flash, url_for

from Stats.main.forms import DataSetform

main = Blueprint("main", __name__)

data_set = []


@main.route("/", methods=["GET", "POST"])
def home():
    functions = ["normal", "mean", "mode", "median", "variance", "standard deviation", "covariance", "pooled variance", "t-distribution"]
    return render_template("home.html", functions=functions)

@main.route("/simple", methods=["GET", "POST"])
def simple_home():
    form = DataSetform()
    functions = ["normal", "mean", "mode", "median", "variance", "standard deviation", "covariance", "pooled variance", "t-distribution"]

    if form.validate_on_submit():
        data_set.append(form.value.data)
        flash("Data Successfully Entered", category="success")

    return render_template("simple_home.html", functions=functions, data_set=data_set, form=form)