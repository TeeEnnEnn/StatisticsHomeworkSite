from flask import Blueprint, render_template, flash, url_for
import numpy as np
import math as math

from Stats.simple.forms import DataSetForm

data_set = np.array([])

simple = Blueprint("simple", __name__)


@simple.route("/simple", methods=["GET", "POST"])
def home():
    global data_set  # Add this line to indicate you want to modify the global variable

    form = DataSetForm()
    functions = ["mean", "mode", "median", "variance", "standard deviation"]

    if form.validate_on_submit():
        data_set = np.append(data_set, form.value.data)
        flash("Data Successfully Entered", category="success")

    mean = get_mean(data_set)
    _range = get_range(data_set)
    mode = get_mode(data_set)
    median = get_median(data_set)
    variance = get_variance(data_set)
    standard_deviation = get_standard_deviation(data_set)

    return render_template("simple_home.html", functions=functions, data_set=data_set, form=form,
                           data_set_size=data_set.size,
                           mean=mean, range=_range, mode=mode, median=median, variance=variance,
                           standard_deviation=standard_deviation)


def get_mean(values) -> float:
    if values.size == 0:
        return 0
    return round(values.sum() / values.size, 3)


def get_range(values) -> float:
    if values.size == 0:
        return 0
    return round(values.max() - values.min(), 3)


def get_mode(values) -> float:
    if values.size == 0:
        return 0
    # get one then go through all. have another array to keep the number of appearnaces
    return 0


def get_median(values) -> float:
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


def get_variance(values) -> float:
    if values.size == 0:
        return 0
    return 0


def get_standard_deviation(values) -> float:
    if values.size == 0:
        return 0
    return round(math.sqrt(get_variance(values)), 3)

# def reset_data_set(old_data_set):
#    return np.array([])
