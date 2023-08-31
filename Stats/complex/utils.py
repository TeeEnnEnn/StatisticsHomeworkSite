import math as m
from scipy import stats as stats


class Calculator:
    """
    A class used to calculate probabilities
    """
    def __init__(self, accuracy: int):
        self.accuracy = accuracy

    def binomial(self, n: int, p: float, x: int):
        """
        Binomial distribution calculator
        :param n: Number of attempts
        :param p: Probability of success
        :param x: x value
        :return: (probability, mean, variance, standard_deviation)
        """
        q = 1 - p
        probability = round(stats.binom.pmf(x, n, p), self.accuracy)
        mean = round(n * p, self.accuracy)
        variance = round(n * p * q, self.accuracy)
        standard_deviation = round(m.sqrt(variance), self.accuracy)
        return probability, mean, variance, standard_deviation

    def normal(self, mean: float, standard_deviation: float, x: float):
        """
        Normal Distribution Calculator
        :param mean: mean
        :param standard_deviation: standard deviation
        :param x: x value
        :return: probability
        """
        if standard_deviation == 0:
            return 0

        probability = stats.norm.cdf(x, mean, standard_deviation)
        return round(probability, self.accuracy)

    def t_distribution(self, x, freedom):
        """
        T distribution calculator
        :param x: x value
        :param freedom: degrees of freedom
        :return: probability
        """
        probability = stats.t.cdf(x, freedom)
        return round(probability, self.accuracy)

    def f_distribution(self, x, freedom_n, freedom_d):
        """
        F distribution calculator
        :param x: x value
        :param freedom_n: numerator degrees of freedom
        :param freedom_d: denominator degrees of freedom
        :return: probability
        """
        probability = stats.f.cdf(x, freedom_n, freedom_d)
        probability = 1 - probability
        return round(probability, self.accuracy)

    def chi_squared_distribution(self, chi_square, freedom):
        """
        Chi-Square calculator
        :param chi_square: chi-squared value
        :param freedom: degrees of freedom
        :return: probability
        """
        probability = stats.chi2.cdf(chi_square, freedom)
        probability = 1 - probability
        return round(probability, self.accuracy)

    def poisson_distribution(self, k, mean):
        """
        Poisson distribution calculator
        :param k: k value
        :param mean: mean
        :return: probability
        """
        return round(stats.poisson.pmf(k, mean), self.accuracy)

    def geometric_distribution(self, p, n):
        """
        Geometric distribution Calculator
        :param p: probability of success
        :param n: number of attempts
        :return: (probability, expected value, variance, standard_deviation)
        """
        if p == 0:
            return 0, 0, 0, 0

        probability = round((1 - p) ** (n - 1) * p, self.accuracy)
        expected = round(1 / p, self.accuracy)
        variance = round(((1 / p) / (p ** 2)), self.accuracy)
        standard_deviation = round(m.sqrt(((1 / p) / (p ** 2))), self.accuracy)
        return probability, expected, variance, standard_deviation


class Distribution:
    """
    Base distribution class
    """
    name: str
    description: str
    explanation: str

    def __init__(self, name, description, explanation):
        self.name = name
        self.description = description
        self.explanation = explanation
