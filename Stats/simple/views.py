from flask import Blueprint, render_template, flash, jsonify
import numpy as np


from Stats.simple.forms import DataSetForm
from Stats.simple.utils import get_mean, get_range, get_mode, get_median, get_variance, get_standard_deviation, \
    get_mean_deviation, get_lower_quartile, get_upper_quartile

data_set = np.array([])
cleared = False

simple = Blueprint("simple", __name__)


@simple.route("/simple", methods=["GET", "POST"])
def home():
    global data_set, cleared  # Add this line to indicate you want to modify the global variable

    if cleared is True:
        data_set = np.array([])

    form = DataSetForm()
    functions = ["mean", "mode", "median", "variance", "standard deviation"]

    if form.validate_on_submit():
        cleared = False
        data_set = np.append(data_set, form.value.data)
        flash("Data Successfully Entered", category="success")

    mean = get_mean(data_set)
    _range = get_range(data_set)
    mode = get_mode(data_set)
    median = get_median(data_set)
    variance = get_variance(data_set)
    standard_deviation = get_standard_deviation(data_set)
    mean_deviation = get_mean_deviation(data_set)
    lower_quartile = get_lower_quartile(data_set)
    upper_quartile = get_upper_quartile(data_set)

    return render_template("simple_home.html", functions=functions, data_set=data_set, form=form,
                           data_set_size=data_set.size,
                           mean=mean, range=_range, mode=mode, median=median, variance=variance,
                           standard_deviation=standard_deviation, mean_deviation=mean_deviation,
                           lower_quartile=lower_quartile, upper_quartile=upper_quartile)


@simple.route("/reset-data", methods=["POST"])
def reset_data():
    global data_set, cleared
    cleared = True
    data_set = np.array([])
    return jsonify({"message": "Data Set reset successfully"}), 200
