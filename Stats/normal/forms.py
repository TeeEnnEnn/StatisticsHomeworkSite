from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired


class NormalForm(FlaskForm):
    mean = IntegerField("mean", validators=[DataRequired()])
    standard_deviation = IntegerField("stanard deviation", validators=[DataRequired()])
    z_value = IntegerField("z value (less than)", validators=[DataRequired()])
    submit = SubmitField("Submit", validators=[DataRequired()])