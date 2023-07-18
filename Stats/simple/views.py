from flask import Blueprint, render_template, flash, jsonify, request, send_file, redirect, url_for
import numpy as np

from Stats.simple.forms import DataSetForm
from Stats.simple.graph import generate_line_graph, generate_frequency_graph
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

    try:
        generate_line_graph(data_set)
        generate_frequency_graph(data_set)
        graph = True
    except ValueError as error:
        graph = False

    return render_template("simple_home.html", data_set=data_set, form=form,
                           data_set_size=data_set.size,
                           mean=mean, range=_range, mode=mode, median=median, variance=variance,
                           standard_deviation=standard_deviation, mean_deviation=mean_deviation,
                           lower_quartile=lower_quartile, upper_quartile=upper_quartile, inter_quartile=inter_quartile,
                           graph=graph)


@simple.route("/reset-data", methods=["POST"])
def reset_data():
    global data_set, cleared
    cleared = True
    data_set = np.array([])
    return jsonify({"message": "Data Set reset successfully"}), 200


@simple.route("/line-graph-image")
def line_graph_image():
    graph_image_path = "C:\\Users\\theon\\Documents\\GitHub\\StatisticsWebsiteClone\\Stats\\static\\line_graph.png"
    return send_file(graph_image_path, mimetype="image/png")


@simple.route("/frequency-graph-image")
def frequency_graph_image():
    graph_image_path = "C:\\Users\\theon\\Documents\\GitHub\\StatisticsWebsiteClone\\Stats\\static\\frequency_graph.png"
    return send_file(graph_image_path, mimetype="image/png")


@simple.route("/sort-ascending")
def ascending():
    global data_set
    data_set.sort()
    return redirect(url_for("simple.home"))


@simple.route("/sort-descending")
def descending():
    global data_set
    data_set[::-1].sort()
    return redirect(url_for("simple.home"))


@simple.route("/delete-item", methods=["POST"])
def delete_item():
    global data_set
    data = request.get_json()
    index = int(data.get("index")) - 1
    data_set = np.delete(data_set, index)
    return jsonify({"message": "Data Set changed successfully"}), 200
# the javascript to make this work still needs to be written
