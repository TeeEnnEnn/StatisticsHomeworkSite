import math as m
from scipy import stats as stats


class Calculator:
    def __init__(self, accuracy: int):
        self.accuracy = accuracy

    def binomial(self, n: int, p: float, x: int):
        q = 1 - p
        probability = round(stats.binom.pmf(x, n, p), self.accuracy)
        mean = round(n * p, self.accuracy)
        variance = round(n * p * q, self.accuracy)
        standard_deviation = round(m.sqrt(variance), self.accuracy)
        return probability, mean, variance, standard_deviation

    def normal(self, mean: float, standard_deviation: float, x: float):
        if standard_deviation == 0:
            return 0

        probability = stats.norm.cdf(x, mean, standard_deviation)
        return round(probability, self.accuracy)

    def t_distribution(self, x, freedom):
        probability = stats.t.cdf(x, freedom)
        return round(probability, self.accuracy)

    def f_distribution(self, x, freedom_n, freedom_d):
        probability = stats.f.cdf(x, freedom_n, freedom_d)
        probability = 1 - probability
        return round(probability, self.accuracy)

    def chi_squared_distribution(self, chi_square, freedom):
        probability = stats.chi2.cdf(chi_square, freedom)
        probability = 1 - probability
        return round(probability, self.accuracy)

    def poisson_distribution(self, k, mean):
        return round(stats.poisson.pmf(k, mean), self.accuracy)

    def geometric_distribution(self, p, n):
        if p == 0:
            return 0, 0, 0, 0

        probability = round((1 - p) ** (n - 1) * p, self.accuracy)
        expected = round(1 / p, self.accuracy)
        variance = round(((1 / p) / (p ** 2)), self.accuracy)
        standard_deviation = round(m.sqrt(((1 / p) / (p ** 2))), self.accuracy)
        return probability, expected, variance, standard_deviation


class Distribution:
    name: str
    description: str
    explanation: str

    def __init__(self, name, description, explanation):
        self.name = name
        self.description = description
        self.explanation = explanation
