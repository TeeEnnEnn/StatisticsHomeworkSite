from flask_wtf import FlaskForm
from wtforms import SubmitField, DecimalField
from wtforms.validators import DataRequired


class NormalForm(FlaskForm):
    mean = DecimalField("mean", validators=[DataRequired()])
    standard_deviation = DecimalField("Standard deviation", validators=[DataRequired()])
    z_value = DecimalField("z value (less than)", validators=[DataRequired()])
    submit = SubmitField("Submit", validators=[DataRequired()])
