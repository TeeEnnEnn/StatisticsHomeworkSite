from flask import Blueprint, render_template

from Stats.complex.forms import NormalForm, BinomialForm
from Stats.complex.utils import Distributions

complex_stats = Blueprint("complex", __name__)

functions = ["normal", "binomial"]


@complex_stats.route("/complex", methods=["GET", "POST"])
def home():
    return render_template("complex_home.html", functions=functions)


@complex_stats.route("/complex/normal", methods=["GET", "POST"])
def normal():
    form = NormalForm()
    mean, standard_deviation, x = 0, 0, 0
    calculator = Distributions(9)
    if form.validate_on_submit():
        mean = form.mean.data
        standard_deviation = form.standard_deviation.data
        x = form.x.data

    probability = calculator.normal(mean, standard_deviation, x)
    return render_template("normal.html", functions=functions, form=form, probability=probability)


@complex_stats.route("/complex/binomial", methods=["GET", "POST"])
def binomial():
    x, n, p = 0, 0, 0
    form = BinomialForm()
    calculator = Distributions(9)
    if form.validate_on_submit():
        n = form.n.data
        p = form.p.data
        x = form.x.data

    probability, mean, variance, standard_deviation = calculator.binomial(n=n, p=p, x=x)
    return render_template("binomial.html", functions=functions, form=form, probability=probability, mean=mean,
                           variance=variance, standard_deviation=standard_deviation)
