import numpy as np
from flask import Blueprint, render_template, jsonify, request, session, flash
import secrets
import pendulum
# moved datetime -> pendulum; because "TypeError: can't subtract offset-naive and offset-aware datetimes" inexplicably

from Stats.simple.utils import Calculator
from Stats import active_tokens

simple = Blueprint("simple", __name__)


@simple.before_request
def before_request():
	if "user_token" not in session:
		session["user_token"] = generate_unique_token()
		session["last_activity"] = pendulum.now()
		active_tokens.add(session["user_token"])

	if pendulum.now() - session["last_activity"] >= pendulum.duration(seconds=7200):
		if session["user_token"] in active_tokens:
			active_tokens.remove(session["user_token"])
			delete_graphs(session["user_token"])
			session.pop("user_token")
			session.pop("last_activity")
			flash("""
			Your session has ended.
			Your graphs have been deleted.
			Reload a page to get a new session
			""", "warning")

	session["last_activity"] = pendulum.now()

	print(session)
	print(len(active_tokens))


def delete_graphs(user_token: str):
	pass


def generate_unique_token() -> str:
	while True:
		token = secrets.token_hex(16)
		if token not in active_tokens:
			return token


@simple.get("/simple")
def home():
	return render_template("simple_home.html")


@simple.post("/simple/calculate")
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
