import math as math
from numpy import ndarray
import numpy as np
import statistics


class Calculator:

    def __init__(self, accuracy):
        self.accuracy = accuracy

    def get_mean(self, values: ndarray) -> float:
        if values.size == 0:
            return 0
        else:
            mean = float(np.mean(values))
            return round(number=mean, ndigits=self.accuracy)

    def get_range(self, values: ndarray) -> float:
        if values.size == 0:
            return 0
        _range = np.ptp(values)
        return round(number=_range, ndigits=self.accuracy)

    def get_mode(self, values: ndarray) -> int | tuple[ndarray, ndarray]:
        if values.size == 0:
            return 0

        values, counts = np.unique(values, return_counts=True)
        mode_indices = np.argmax(counts)
        mode = values[mode_indices]

        return round(number=mode, ndigits=self.accuracy)

    def get_median(self, values: ndarray) -> float:
        np.sort(values)

        if values.size == 0:
            return 0

        if values.size % 2 == 0:
            position = int(values.size / 2)
            median = (values[position - 1] + values[position]) / 2
            return round(number=median, ndigits=self.accuracy)
        else:
            position = (values.size + 1) / 2
            median = values[int(position) - 1]
            return round(number=median, ndigits=self.accuracy)

    def get_variance(self, values: ndarray) -> int | ndarray:
        if values.size == 0:
            return 0

        mean = np.mean(values)
        square_difference = np.square(values - mean)
        variance = float(np.mean(square_difference))

        return round(number=variance, ndigits=self.accuracy)

    def get_standard_deviation(self, values: ndarray) -> float:
        if values.size == 0:
            return 0
        standard_deviation = math.sqrt(self.get_variance(values))
        return round(number=standard_deviation, ndigits=self.accuracy)

    def get_mean_deviation(self, values: ndarray) -> float:
        if values.size == 0:
            return 0

        mean = np.mean(values)
        deviations = np.abs(values - mean)
        mean_deviation = np.sum(deviations) / values.size
        return round(number=mean_deviation, ndigits=self.accuracy)

    def get_lower_quartile(self, values: ndarray) -> float:
        if values.size < 2:
            return 0

        values = np.sort(values)

        lower_quartile = float(statistics.quantiles(values, n=4)[0])
        return round(number=lower_quartile, ndigits=self.accuracy)

    def get_upper_quartile(self, values: ndarray):
        if values.size < 2:
            return 0

        values = np.sort(values)

        upper_quartile = float(statistics.quantiles(values, n=4)[2])
        return round(number=upper_quartile, ndigits=self.accuracy)

    def get_inter_quartile_range(self, values: ndarray):
        if values.size < 2:
            return 0
        inter_quartile = self.get_upper_quartile(values) - self.get_lower_quartile(values)
        return round(number=inter_quartile, ndigits=self.accuracy)

    def get_lower_fence(self, values: ndarray):
        if values.size < 2:
            return 0
        lower_quartile = float(statistics.quantiles(values, n=4)[0])
        inter_quartile = self.get_upper_quartile(values) - self.get_lower_quartile(values)
        lower_fence = lower_quartile - 1.5 * inter_quartile

        return round(lower_fence, self.accuracy)

    def get_upper_fence(self, values: ndarray):
        if values.size < 2:
            return 0
        upper_quartile = float(statistics.quantiles(values, n=4)[2])
        inter_quartile = self.get_upper_quartile(values) - self.get_lower_quartile(values)
        upper_fence = upper_quartile + 1.5 * inter_quartile
        return round(upper_fence, self.accuracy)
