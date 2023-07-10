from flask_wtf import FlaskForm
from wtforms import SubmitField, DecimalField
from wtforms.validators import DataRequired


class DataSetForm(FlaskForm):
    value = DecimalField("New Value", validators=[DataRequired()])
    submit = SubmitField("Submit", validators=[])
