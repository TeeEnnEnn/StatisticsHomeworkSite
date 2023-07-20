from flask_wtf import FlaskForm
from wtforms import SubmitField, DecimalField, IntegerField
from wtforms.validators import DataRequired


class NormalForm(FlaskForm):
    mean = DecimalField("Mean", validators=[]) # for some reason data required does not recognise 0 as data
    standard_deviation = DecimalField("Standard Deviation", validators=[DataRequired()])
    x = DecimalField("x", validators=[DataRequired()])
    submit = SubmitField("Calculate")


class BinomialForm(FlaskForm):
    n = IntegerField("n (number of attempts): ", validators=[DataRequired()])
    p = DecimalField("p (probability of success): ", validators=[DataRequired()])
    x = IntegerField("x (number of times for specific outcome)", validators=[DataRequired()])
    submit = SubmitField("Calculate")
