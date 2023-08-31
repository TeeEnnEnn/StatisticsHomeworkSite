import math as math
from numpy import ndarray
import numpy as np
import statistics


class Calculator:
    """
    The Calculator class performs calculations onm teh values within the dataset
    """

    def __init__(self, accuracy):
        """
        Initialization of the Calculator class
        :param accuracy:the rounding accuracy to be used for calculations.
        """
        self.accuracy = accuracy

    def get_mean(self, values: ndarray) -> float:
        """
        Average of the values in the dataset
        :param values: values in the data set
        :return: Average
        """
        if values.size == 0:
            return 0
        else:
            mean = float(np.mean(values))
            return round(number=mean, ndigits=self.accuracy)

    def get_range(self, values: ndarray) -> float:
        """
        Range of the values in the data set
        :param values: values in the data set
        :return: Range
        """
        if values.size == 0:
            return 0
        _range = np.ptp(values)
        return round(number=_range, ndigits=self.accuracy)

    def get_mode(self, values: ndarray) -> int | tuple[ndarray, ndarray]:
        """
        Returns the value that appears the most in the data set
        :param values: the values in the data set
        :return: Mode
        """
        if values.size == 0:
            return 0

        values, counts = np.unique(values, return_counts=True)
        mode_indices = np.argmax(counts)
        mode = values[mode_indices]

        return round(number=mode, ndigits=self.accuracy)

    def get_median(self, values: ndarray) -> float:
        """
        Returns the median value in the data set
        :param values: the values in the data set
        :return: Median
        """
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
        """
        Returns the variance
        :param values: the values in the data set
        :return: Variance
        """
        if values.size == 0:
            return 0

        mean = np.mean(values)
        square_difference = np.square(values - mean)
        variance = float(np.mean(square_difference))

        return round(number=variance, ndigits=self.accuracy)

    def get_standard_deviation(self, values: ndarray) -> float:
        """
        Returns the standard deviation
        :param values: the values in the data set
        :return: Standard Deviation
        """
        if values.size == 0:
            return 0
        standard_deviation = math.sqrt(self.get_variance(values))
        return round(number=standard_deviation, ndigits=self.accuracy)

    def get_mean_deviation(self, values: ndarray) -> float:
        """
        Returns the  mean deviation
        :param values: the values in the data set
        :return: Mean Deviation
        """
        if values.size == 0:
            return 0

        mean = np.mean(values)
        deviations = np.abs(values - mean)
        mean_deviation = np.sum(deviations) / values.size
        return round(number=mean_deviation, ndigits=self.accuracy)

    def get_lower_quartile(self, values: ndarray) -> float:
        """
        Returns the lower quartile
        :param values: the values in the data set
        :return: Lower quartile
        """
        if values.size < 2:
            return 0

        values = np.sort(values)

        lower_quartile = float(statistics.quantiles(values, n=4)[0])
        return round(number=lower_quartile, ndigits=self.accuracy)

    def get_upper_quartile(self, values: ndarray):
        """
        Returns the upper quartile
        :param values: the values in the data set
        :return: Upper Quartile
        """
        if values.size < 2:
            return 0

        values = np.sort(values)

        upper_quartile = float(statistics.quantiles(values, n=4)[2])
        return round(number=upper_quartile, ndigits=self.accuracy)

    def get_inter_quartile_range(self, values: ndarray):
        """
        Returns interquartile range
        :param values: the values in the data set
        :return: Inter Quartile Range
        """
        if values.size < 2:
            return 0
        inter_quartile = self.get_upper_quartile(values) - self.get_lower_quartile(values)
        return round(number=inter_quartile, ndigits=self.accuracy)

    def get_lower_fence(self, values: ndarray):
        """
        Returns lower fence
        :param values: the values in the data set
        :return: Lower Fence
        """
        if values.size < 2:
            return 0
        lower_quartile = float(statistics.quantiles(values, n=4)[0])
        inter_quartile = self.get_upper_quartile(values) - self.get_lower_quartile(values)
        lower_fence = lower_quartile - 1.5 * inter_quartile

        return round(lower_fence, self.accuracy)

    def get_upper_fence(self, values: ndarray):
        """
        Returns upper fence
        :param values: the values in the data set
        :return: Upper fence
        """
        if values.size < 2:
            return 0
        upper_quartile = float(statistics.quantiles(values, n=4)[2])
        inter_quartile = self.get_upper_quartile(values) - self.get_lower_quartile(values)
        upper_fence = upper_quartile + 1.5 * inter_quartile
        return round(upper_fence, self.accuracy)
