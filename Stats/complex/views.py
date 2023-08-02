from flask import Blueprint, render_template, send_file

from Stats.complex.forms import NormalForm, BinomialForm, ChiSquaredForm, FForm, TForm, PoissonForm, GeometricForm
from Stats.complex.graphs import create_bell_graph
from Stats.complex.utils import Distributions

complex_ = Blueprint("complex", __name__)

functions = ["normal", "binomial", "f-distribution", "t-distribution", "chi-squared-distribution",
             "poisson-distribution", "geometric-distribution"]
accuracy = 4
calculator = Distributions(accuracy)


@complex_.route("/complex", methods=["GET", "POST"])
def home():
    return render_template("complex_home.html", functions=functions)


@complex_.route("/complex/normal", methods=["GET", "POST"])
def normal():
    graph = False
    form = NormalForm()
    mean, standard_deviation, x = 0, 0, 0
    if form.validate_on_submit():
        mean = float(form.mean.data)
        standard_deviation = form.standard_deviation.data
        x = form.x.data
        try:
            create_bell_graph(mean, standard_deviation, x)
            graph = True
        except (RuntimeError, Exception):
            graph = False

    distribution_name = "Normal Distribution"
    probability = calculator.normal(mean, standard_deviation, x)
    return render_template("normal.html", form=form, probability=probability,
                           distribution_name=distribution_name, graph=graph, functions=functions)


@complex_.route("/normal-image")
def normal_graph():
    graph_image_path = "C:\\Users\\theon\\Documents\\GitHub\\StatisticsWebsiteClone\\Stats\\static\\normal-graph.png"
    return send_file(graph_image_path, mimetype="image/png")


@complex_.route("/complex/binomial", methods=["GET", "POST"])
def binomial():
    x, n, p = 0, 0, 0
    form = BinomialForm()
    if form.validate_on_submit():
        n = form.n.data
        p = form.p.data
        x = form.x.data

    distribution_name = "Binomial Distribution"
    probability, mean, variance, standard_deviation = calculator.binomial(n=n, p=p, x=x)
    return render_template("binomial.html", form=form, probability=probability, mean=mean,
                           variance=variance, standard_deviation=standard_deviation,
                           distribution_name=distribution_name, functions=functions)


@complex_.route("/complex/t-distribution", methods=["GET", "POST"])
def t_distribution():
    form = TForm()
    freedom, x = 0, 0
    if form.validate_on_submit():
        freedom = form.freedom.data
        x = form.x.data

    distribution_name = "T Distribution"
    probability = calculator.t_distribution(x=x, freedom=freedom)
    return render_template("t_distribution.html", form=form, probability=probability,
                           distribution_name=distribution_name, functions=functions)


@complex_.route("/complex/f-distribution", methods=["GET", "POST"])
def f_distribution():
    form = FForm()
    freedom_n, freedom_d, x = 0, 0, 0
    if form.validate_on_submit():
        freedom_n = form.freedom_n.data
        freedom_d = form.freedom_d.data
        x = form.x.data

    distribution_name = "F Distribution"
    probability = calculator.f_distribution(x=x, freedom_n=freedom_n, freedom_d=freedom_d)
    return render_template("f_distribution.html", form=form, probability=probability,
                           distribution_name=distribution_name, functions=functions)


@complex_.route("/complex/chi-squared-distribution", methods=["GET", "POST"])
def chi_squared():
    form = ChiSquaredForm()
    freedom, chi_square = 0, 0
    if form.validate_on_submit():
        freedom = form.freedom.data
        chi_square = form.chi_square.data

    distribution_name = "Chi Squared Distribution"
    probability = calculator.chi_squared_distribution(chi_square=chi_square, freedom=freedom)
    return render_template("chi_squared_distribution.html", form=form, probability=probability,
                           distribution_name=distribution_name, functions=functions)


@complex_.route("/complex/poisson-distribution", methods=["GET", "POST"])
def poisson_distribution():
    form = PoissonForm()
    k, mean = 0, 0
    if form.validate_on_submit():
        k = int(form.k.data)
        mean = float(form.mean.data)

    distribution_name = "Poisson Distribution"
    probability = calculator.poisson_distribution(k, mean)
    return render_template("poisson-distribution.html", form=form, distribution_name=distribution_name,
                           probability=probability, functions=functions)


@complex_.route("/complex/geometric-distribution", methods=["GET", "POST"])
def geometric_distribution():
    form = GeometricForm()
    n, p = 0, 0
    if form.validate_on_submit():
        n = float(form.n.data)
        p = float(form.p.data)

    distribution_name = "Geometric Distribution"
    probability, expected_value, variance, standard_deviation = calculator.geometric_distribution(p, n)
    return render_template("geometric-distribution.html", form=form, distribution_name=distribution_name,
                           probability=probability,
                           expected_value=expected_value, variance=variance, standard_deviation=standard_deviation,
                           functions=functions)
