from flask import Blueprint, render_template, send_file

from Stats.complex.forms import NormalForm, BinomialForm, ChiSquaredForm, FForm, TForm, PoissonForm, GeometricForm
from Stats.complex.graphs import create_bell_graph
from Stats.complex.utils import Calculator, Distribution

complex_ = Blueprint("complex", __name__)

functions = ["normal", "binomial", "f-distribution", "t-distribution", "chi-squared-distribution",
             "poisson-distribution", "geometric-distribution"]
accuracy = 4  # default accuracy value
calculator = Calculator(accuracy)


@complex_.route("/complex", methods=["GET", "POST"])
def home():
    """
    The main calculator page
    :return: a template
    """
    return render_template("complex_home.html", functions=functions)


@complex_.route("/complex/normal", methods=["GET", "POST"])
def normal():
    """
    The normal distribution page
    :return: a template
    """
    graph = False
    form = NormalForm()
    mean, standard_deviation, x = 0, 0, 0
    if form.validate_on_submit():
        mean = float(form.mean.data)
        standard_deviation = float(form.standard_deviation.data)
        x = float(form.x.data)
        try:
            create_bell_graph(mean, standard_deviation, x)
            graph = True
        except (RuntimeError, Exception):
            graph = False

    distribution = Distribution("Normal Distribution", "Continuous Probability Distribution",
                                "The Normal distribution, also known as the Gaussian distribution, is a "
                                "probability distribution that is symmetric about the mean, showing that data near "
                                "the mean are more frequent in occurrence than data far from the mean.In graphical "
                                "form, the normal distribution appears as a 'bell curve'.")
    # Source: https://www.investopedia.com/terms/n/normaldistribution.asp#:~:text=Normal%20distribution%2C%20also%20known%20as,as%20a%20%22bell%20curve%22.
    probability = calculator.normal(mean, standard_deviation, x)
    return render_template("normal.html", form=form, probability=probability,
                           distribution=distribution, graph=graph, functions=functions)


@complex_.route("/normal-image")
def normal_graph():
    """
    used to serve an image to the site
    :return: A graph (.png file)
    """
    graph_image_path = "static/normal-graph.png"
    return send_file(graph_image_path, mimetype="image/png")


@complex_.route("/complex/binomial", methods=["GET", "POST"])
def binomial():
    """
    The binomial distribution page
    :return: A template
    """
    x, n, p = 0, 0, 0
    form = BinomialForm()
    if form.validate_on_submit():
        n = int(form.n.data)
        p = float(form.p.data)
        x = int(form.x.data)

    distribution = Distribution("Binomial Distribution", "Discrete Probability Distribution",
                                "The binomial distribution with parameters n and p is the discrete probability "
                                "distribution of the number of successes in a sequence of n independent experiments, "
                                "each asking a yes–no question, and each with its own Boolean-valued outcome: "
                                "success (with probability p) or failure (with probability q = 1 - p).")
    # Source: https://en.wikipedia.org/wiki/Binomial_distribution
    probability, mean, variance, standard_deviation = calculator.binomial(n=n, p=p, x=x)
    return render_template("binomial.html", form=form, probability=probability, mean=mean,
                           variance=variance, standard_deviation=standard_deviation,
                           distribution=distribution, functions=functions)


@complex_.route("/complex/t-distribution", methods=["GET", "POST"])
def t_distribution():
    """
    The T distribution page
    :return: A template
    """
    form = TForm()
    freedom, x = 0, 0
    if form.validate_on_submit():
        freedom = int(form.freedom.data)
        x = float(form.x.data)

    distribution = Distribution("T Distribution", "Continuous Probability Distribution",
                                "The Student's t-distribution (or simply the t-distribution) is a "
                                "continuous probability distribution that generalizes the standard normal distribution."
                                "Like the Normal Distribution, it is symmetric around zero and bell-shaped."
                                "However, the t-distribution has heavier tails and the amount of probability mass in "
                                "the tails is controlled by the parameter df (degrees of freedom) . For df = 1 the "
                                "Student's t distribution becomes the standard Cauchy distribution, whereas "
                                "for df → ∞ it becomes the standard normal distribution N(0,1)")
    # Source:
    probability = calculator.t_distribution(x=x, freedom=freedom)
    return render_template("t_distribution.html", form=form, probability=probability,
                           distribution=distribution, functions=functions)


@complex_.route("/complex/f-distribution", methods=["GET", "POST"])
def f_distribution():
    """
    The F distribution page
    :return: A template
    """
    form = FForm()
    freedom_n, freedom_d, x = 0, 0, 0
    if form.validate_on_submit():
        freedom_n = int(form.freedom_n.data)
        freedom_d = int(form.freedom_d.data)
        x = form.x.data

    distribution = Distribution("F Distribution", "Continuous Probability Distribution",
                                "The F distribution is a uni-variate continuous distribution often "
                                "used in hypothesis testing.")
    # Source:  https://www.statlect.com/probability-distributions/F-distribution
    probability = calculator.f_distribution(x=x, freedom_n=freedom_n, freedom_d=freedom_d)
    return render_template("f_distribution.html", form=form, probability=probability,
                           distribution=distribution, functions=functions)


@complex_.route("/complex/chi-squared-distribution", methods=["GET", "POST"])
def chi_squared():
    """
    The chi-squared distribution page
    :return: A template
    """
    form = ChiSquaredForm()
    freedom, chi_square = 0, 0
    if form.validate_on_submit():
        freedom = int(form.freedom.data)
        chi_square = float(form.chi_square.data)

    distribution = Distribution("Chi Squared Distribution", "Continuous Probability Distribution",
                                "The chi-squared distribution with k degrees of freedom is the distribution "
                                "of a sum of the squares of k independent standard normal random variables. The "
                                "chi-squared distribution is a special case of the gamma distribution and is one of "
                                "the most widely used probability distributions in inferential statistics, notably in "
                                "hypothesis testing and in construction of confidence intervals.")
    # Source: https://en.wikipedia.org/wiki/Chi-squared_distribution
    probability = calculator.chi_squared_distribution(chi_square=chi_square, freedom=freedom)
    return render_template("chi_squared_distribution.html", form=form, probability=probability,
                           distribution=distribution, functions=functions)


@complex_.route("/complex/poisson-distribution", methods=["GET", "POST"])
def poisson_distribution():
    """
    The poisson distribution page
    :return: A template
    """
    form = PoissonForm()
    k, mean = 0, 0
    if form.validate_on_submit():
        k = int(form.k.data)
        mean = float(form.mean.data)

    distribution = Distribution("Poisson Distribution", "Discrete Probability Distribution",
                                "The Poisson distribution is a discrete probability distribution that "
                                "expresses the probability of a given number of events occurring in a fixed interval "
                                "of time or space if these events occur with a known constant mean rate and "
                                "independently of the time since the last event.")
    # source: https://en.wikipedia.org/wiki/Poisson_distribution
    probability = calculator.poisson_distribution(k, mean)
    return render_template("poisson-distribution.html", form=form, distribution=distribution,
                           probability=probability, functions=functions)


@complex_.route("/complex/geometric-distribution", methods=["GET", "POST"])
def geometric_distribution():
    """
    The geometric distribution page
    :return: A template
    """
    form = GeometricForm()
    n, p = 0, 0
    if form.validate_on_submit():
        n = float(form.n.data)
        p = float(form.p.data)

    distribution = Distribution("Geometric distribution", "Discrete Probability Distribution",
                                "The geometric distribution gives the probability that the first occurrence "
                                "of success requires k independent trials, each with success probability p. "
                                "If the probability of success on each trial is p, then the probability that the "
                                "kth trial is the first success is")
    # Source: https://en.wikipedia.org/wiki/Geometric_distribution
    probability, expected_value, variance, standard_deviation = calculator.geometric_distribution(p, n)
    return render_template("geometric-distribution.html", form=form, distribution=distribution,
                           probability=probability,
                           expected_value=expected_value, variance=variance, standard_deviation=standard_deviation,
                           functions=functions)
