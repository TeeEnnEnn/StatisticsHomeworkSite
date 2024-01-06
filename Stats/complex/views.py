from flask import Blueprint, render_template, send_file, request, jsonify

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


@complex_.get("/complex/normal")
def normal():
	"""
	The normal distribution page
	:return: a template
	"""

	distribution = Distribution("Normal Distribution", "Continuous Probability Distribution",
	                            "The Normal distribution, also known as the Gaussian distribution, is a "
	                            "probability distribution that is symmetric about the mean, showing that data near "
	                            "the mean are more frequent in occurrence than data far from the mean.In graphical "
	                            "form, the normal distribution appears as a 'bell curve'.")
	# Source: https://www.investopedia.com/terms/n/normaldistribution.asp#:~:text=Normal%20distribution%2C%20also%20known%20as,as%20a%20%22bell%20curve%22.
	# probability = calculator.normal(mean, standard_deviation, x)
	return render_template("normal.html",
	                       distribution=distribution, functions=functions)


@complex_.post("/complex/normal")
def normal_calculation():
	try:
		data = request.json
		mean = data.get("mean", 0)
		sd = data.get("sd", 0)
		x = data.get("x", 0)

	except Exception as error:
		return jsonify(error=str(error), message="error")

	try:
		result = float(calculator.normal(mean, sd, x))
		return jsonify(probability=result, message="success")
	except Exception as error:
		return jsonify(error=str(error), message="error")


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

	distribution = Distribution("Binomial Distribution", "Discrete Probability Distribution",
	                            "The binomial distribution with parameters n and p is the discrete probability "
	                            "distribution of the number of successes in a sequence of n independent experiments, "
	                            "each asking a yes–no question, and each with its own Boolean-valued outcome: "
	                            "success (with probability p) or failure (with probability q = 1 - p).")
	# Source: https://en.wikipedia.org/wiki/Binomial_distribution
	# probability, mean, variance, standard_deviation = calculator.binomial(n=n, p=p, x=x)
	return render_template("binomial.html",
	                       distribution=distribution, functions=functions)


@complex_.route("/complex/t-distribution", methods=["GET", "POST"])
def t_distribution():
	"""
	The T distribution page
	:return: A template
	"""

	distribution = Distribution("T Distribution", "Continuous Probability Distribution",
	                            "The Student's t-distribution (or simply the t-distribution) is a "
	                            "continuous probability distribution that generalizes the standard normal distribution."
	                            "Like the Normal Distribution, it is symmetric around zero and bell-shaped."
	                            "However, the t-distribution has heavier tails and the amount of probability mass in "
	                            "the tails is controlled by the parameter df (degrees of freedom) . For df = 1 the "
	                            "Student's t distribution becomes the standard Cauchy distribution, whereas "
	                            "for df → ∞ it becomes the standard normal distribution N(0,1)")
	# Source:
	# probability = calculator.t_distribution(x=x, freedom=freedom)
	return render_template("t_distribution.html",
	                       distribution=distribution, functions=functions)


@complex_.route("/complex/f-distribution", methods=["GET", "POST"])
def f_distribution():
	"""
	The F distribution page
	:return: A template
	"""

	distribution = Distribution("F Distribution", "Continuous Probability Distribution",
	                            "The F distribution is a uni-variate continuous distribution often "
	                            "used in hypothesis testing.")
	# Source:  https://www.statlect.com/probability-distributions/F-distribution
	# probability = calculator.f_distribution(x=x, freedom_n=freedom_n, freedom_d=freedom_d)
	return render_template("f_distribution.html",
	                       distribution=distribution, functions=functions)


@complex_.route("/complex/chi-squared-distribution", methods=["GET", "POST"])
def chi_squared():
	"""
	The chi-squared distribution page
	:return: A template
	"""

	distribution = Distribution("Chi Squared Distribution", "Continuous Probability Distribution",
	                            "The chi-squared distribution with k degrees of freedom is the distribution "
	                            "of a sum of the squares of k independent standard normal random variables. The "
	                            "chi-squared distribution is a special case of the gamma distribution and is one of "
	                            "the most widely used probability distributions in inferential statistics, notably in "
	                            "hypothesis testing and in construction of confidence intervals.")
	# Source: https://en.wikipedia.org/wiki/Chi-squared_distribution
	# probability = calculator.chi_squared_distribution(chi_square=chi_square, freedom=freedom)
	return render_template("chi_squared_distribution.html",
	                       distribution=distribution, functions=functions)


@complex_.route("/complex/poisson-distribution", methods=["GET", "POST"])
def poisson_distribution():
	"""
	The poisson distribution page
	:return: A template
	"""

	distribution = Distribution("Poisson Distribution", "Discrete Probability Distribution",
	                            "The Poisson distribution is a discrete probability distribution that "
	                            "expresses the probability of a given number of events occurring in a fixed interval "
	                            "of time or space if these events occur with a known constant mean rate and "
	                            "independently of the time since the last event.")
	# source: https://en.wikipedia.org/wiki/Poisson_distribution
	# probability = calculator.poisson_distribution(k, mean)
	return render_template("poisson-distribution.html", distribution=distribution,
	                       functions=functions)


@complex_.route("/complex/geometric-distribution", methods=["GET", "POST"])
def geometric_distribution():
	"""
	The geometric distribution page
	:return: A template
	"""

	distribution = Distribution("Geometric distribution", "Discrete Probability Distribution",
	                            "The geometric distribution gives the probability that the first occurrence "
	                            "of success requires k independent trials, each with success probability p. "
	                            "If the probability of success on each trial is p, then the probability that the "
	                            "kth trial is the first success is")
	# Source: https://en.wikipedia.org/wiki/Geometric_distribution
	# probability, expected_value, variance, standard_deviation = calculator.geometric_distribution(p, n)
	return render_template("geometric-distribution.html", distribution=distribution, functions=functions)
