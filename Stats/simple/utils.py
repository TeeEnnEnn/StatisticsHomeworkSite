import math as math
from numpy import ndarray
import numpy as np
import statistics


def get_mean(values: ndarray) -> int | ndarray:
    if values.size == 0:
        return 0
    return np.mean(values)


def get_range(values: ndarray) -> float:
    if values.size == 0:
        return 0
    return round(max(values) - min(values), 3)


def get_mode(values: ndarray) -> int | tuple[ndarray, ndarray]:
    if values.size == 0:
        return 0

    values, counts = np.unique(values, return_counts=True)
    mode_indices = np.argmax(counts)
    mode = values[mode_indices]

    return mode


def get_median(values: ndarray) -> float:
    np.sort(values)

    if values.size == 0:
        return 0

    if values.size % 2 == 0:
        position = int(values.size / 2)
        median = (values[position - 1] + values[position]) / 2
        return median
    else:
        position = (values.size + 1) / 2
        median = values[int(position) - 1]
        return median


def get_variance(values: ndarray) -> int | ndarray:
    if values.size == 0:
        return 0

    mean = get_mean(values)
    square_difference = np.square(values - mean)
    variance = np.mean(square_difference)

    return variance


def get_standard_deviation(values: ndarray) -> float:
    if values.size == 0:
        return 0
    return round(math.sqrt(get_variance(values)), 3)


def get_mean_deviation(values: ndarray) -> float:
    if values.size == 0:
        return 0

    mean = get_mean(values)
    deviations = np.abs(values - mean)
    mean_deviation = np.sum(deviations) / values.size
    return mean_deviation


def get_lower_quartile(values: ndarray) -> float:
    if values.size < 2:
        return 0

    values = np.sort(values)

    lower_quartile = statistics.quantiles(values, n=4)[0]
    return float(lower_quartile)


def get_upper_quartile(values: ndarray):
    if values.size < 2:
        return 0

    values = np.sort(values)

    upper_quartile = statistics.quantiles(values, n=4)[2]
    return float(upper_quartile)
