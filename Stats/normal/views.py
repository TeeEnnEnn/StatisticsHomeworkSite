from flask import Blueprint, render_template, flash, url_for

from Stats.normal.forms import NormalForm

normal = Blueprint("normal", __name__)


@normal.route("/normal", methods=["GET", "POST"])
def home():
    form = NormalForm()
    if form.validate_on_submit():
        mean = form.mean.data
        standard_deviation = form.standard_deviation.data
        z_value = form.z_value.data
        flash("Data Successfully Entered", category="success")
    return render_template("normal.html", form=form)
