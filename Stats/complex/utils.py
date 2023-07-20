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

