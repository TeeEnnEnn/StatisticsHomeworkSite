import math as m

from scipy import stats as stats


class Distributions:
    def __init__(self, accuracy: int):
        self.accuracy = accuracy

    def binomial(self, n: int, p: float, x: int):
        q = 1 - p
        probability = round(m.comb(n, x) * p ** x * q ** (n - x), self.accuracy)
        mean = round(n * p, self.accuracy)
        variance = round(n * p * q, self.accuracy)
        standard_deviation = round(m.sqrt(variance), self.accuracy)
        return probability, mean, variance, standard_deviation

    def normal(self, mean: float, standard_deviation: float, x: float):
        if standard_deviation == 0:
            return 0

        mean = float(mean)
        standard_deviation = float(standard_deviation)
        x = float(x)

        # probability = (1 / (standard_deviation * m.sqrt(2 * m.pi))) * (
        #        m.e ** (-(1 / 2) * ((x - mean) / standard_deviation) ** 2))
        # return round(probability, self.accuracy)

        probability = stats.norm.cdf(x, mean, standard_deviation)
        return round(probability, self.accuracy)

    def t_distribution(self, x, freedom):
        x = float(x)
        freedom = float(freedom)

        probability = stats.t.cdf(x, freedom)
        return round(probability, self.accuracy)

    def f_distribution(self, x, freedom_n, freedom_d):
        x = float(x)
        freedom_n = float(freedom_n)
        freedom_d = float(freedom_d)

        probability = stats.f.cdf(x, freedom_n, freedom_d)
        probability = 1 - probability
        return round(probability, self.accuracy)

    def chi_squared_distribution(self, chi_square, freedom):
        chi_square = float(chi_square)
        freedom = float(freedom)

        probability = stats.chi2.cdf(chi_square, freedom)
        probability = 1 - probability
        return round(probability, self.accuracy)

    def poisson_distribution(self, k, mean):
        return round((m.e ** (-mean) * mean ** k) / (m.factorial(k)), self.accuracy)

    def geometric_distribution(self, p, n):
        probability, expected, variance, standard_deviation = 0, 0, 0, 0
        if p != 0:
            probability = round((1 - p) ** (n - 1) * p, self.accuracy)
            expected = round(1 / p, self.accuracy)
            variance = round(((1 / p) / (p ** 2)), self.accuracy)
            standard_deviation = round(m.sqrt(((1 / p) / (p ** 2))), self.accuracy)

        return probability, expected, variance, standard_deviation
