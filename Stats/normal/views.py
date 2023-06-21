from flask import Blueprint, render_template

from Stats.normal.forms import NormalForm

normal = Blueprint("normal", __name__)

@normal.route("/normal", methods=["GET", "POST"])
def home():
    form = NormalForm()
    return render_template("normal.html", form=form)
