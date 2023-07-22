from flask_wtf import FlaskForm
from wtforms import SubmitField, DecimalField, IntegerField
from wtforms.validators import DataRequired


class NormalForm(FlaskForm):
    mean = DecimalField("Mean", validators=[])  # for some reason data required does not recognise 0 as data
    standard_deviation = DecimalField("Standard Deviation", validators=[DataRequired()])
    x = DecimalField("x", validators=[DataRequired()])
    submit = SubmitField("Calculate")


class BinomialForm(FlaskForm):
    n = IntegerField("n (number of attempts): ", validators=[DataRequired()])
    p = DecimalField("p (probability of success): ", validators=[DataRequired()])
    x = IntegerField("x (number of times for specific outcome)", validators=[DataRequired()])
    submit = SubmitField("Calculate")


class ChiSquaredForm(FlaskForm):
    chi_square = DecimalField("Chi square : ", validators=[DataRequired()])
    freedom = IntegerField("df (Degrees of freedom_n):", validators=[DataRequired()])
    submit = SubmitField("Calculate")


class TForm(FlaskForm):
    x = DecimalField("T:", validators=[DataRequired()])
    freedom = IntegerField("df (Degrees of freedom)", validators=[DataRequired()])
    submit = SubmitField("Calculate")


class FForm(FlaskForm):
    x = DecimalField("F:", validators=[DataRequired()])
    freedom_n = IntegerField("dfn (Degrees of freedom Numerator)", validators=[DataRequired()])
    freedom_d = IntegerField("dfd (Degrees of freedom Denominator)", validators=[DataRequired()])
    submit = SubmitField("Calculate")
