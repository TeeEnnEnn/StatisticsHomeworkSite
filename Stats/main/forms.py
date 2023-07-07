from flask_wtf import FlaskForm
from wtforms import SubmitField, DecimalField
from wtforms.validators import DataRequired

class DataSetform(FlaskForm):
    value = DecimalField("New Value", validators=[DataRequired()])
    submit = SubmitField("Submit", validators=[DataRequired()])