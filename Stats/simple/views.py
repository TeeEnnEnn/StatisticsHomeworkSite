from flask import Blueprint, render_template, flash, jsonify
import numpy as np

from Stats.simple.forms import DataSetForm
from Stats.simple.utils import Calculator

data_set = np.array([])
cleared = False

simple = Blueprint("simple", __name__)


@simple.route("/simple", methods=["GET", "POST"])
def home():
    global data_set, cleared  # Add this line to indicate you want to modify the global variable

    if cleared is True:
        data_set = np.array([])

    accuracy = 5
    form = DataSetForm()

    if form.validate_on_submit():
        cleared = False
        data_set = np.append(data_set, form.value.data)
        accuracy = int(form.dropdown.data)
        flash("Data Successfully Entered", category="success")

    calculator = Calculator(accuracy)

    mean = calculator.get_mean(data_set)
    _range = calculator.get_range(data_set)
    mode = calculator.get_mode(data_set)
    median = calculator.get_median(data_set)
    variance = calculator.get_variance(data_set)
    standard_deviation = calculator.get_standard_deviation(data_set)
    mean_deviation = calculator.get_mean_deviation(data_set)
    lower_quartile = calculator.get_lower_quartile(data_set)
    upper_quartile = calculator.get_upper_quartile(data_set)
    inter_quartile = calculator.get_inter_quartile_range(data_set)

    return render_template("simple_home.html", data_set=data_set, form=form,
                           data_set_size=data_set.size,
                           mean=mean, range=_range, mode=mode, median=median, variance=variance,
                           standard_deviation=standard_deviation, mean_deviation=mean_deviation,
                           lower_quartile=lower_quartile, upper_quartile=upper_quartile, inter_quartile=inter_quartile)


@simple.route("/reset-data", methods=["POST"])
def reset_data():
    global data_set, cleared
    cleared = True
    data_set = np.array([])
    return jsonify({"message": "Data Set reset successfully"}), 200
