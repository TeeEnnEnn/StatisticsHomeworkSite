import numpy as np
from flask import Blueprint, render_template, jsonify, request


from Stats.simple.utils import Calculator

simple = Blueprint("simple", __name__)


@simple.route("/simple", methods=["GET"])
def home():
	return render_template("simple_home.html")


@simple.route("/simple/calculate", methods=["POST"])
def calculate():
	try:
		data = request.json
		values = data.get("dataset", [])
		if len(values) != 0:
			for i in range(len(values)):
				values[i] = int(values[i])

		data_set = np.array(values)

	except Exception as error:
		return jsonify(error=str(error), message="error")

	try:
		calculator = Calculator()
		result = {
			"mean": float(calculator.get_mean(data_set)),
			"range": float(calculator.get_range(data_set)),
			"mode": float(calculator.get_mode(data_set)),
			"median": float(calculator.get_median(data_set)),
			"variance": float(calculator.get_variance(data_set)),
			"standard_deviation": float(calculator.get_standard_deviation(data_set)),
			"mean_deviation": float(calculator.get_mean_deviation(data_set)),
			"lower_quartile": float(calculator.get_lower_quartile(data_set)),
			"upper_quartile": float(calculator.get_upper_quartile(data_set)),
			"inter_quartile": float(calculator.get_inter_quartile_range(data_set)),
			"lower_fence": float(calculator.get_lower_fence(data_set)),
			"upper_fence": float(calculator.get_upper_fence(data_set)),
		}
		return jsonify(result=result, message="success")
	except Exception as error:
		return jsonify(error=str(error), message="error")
