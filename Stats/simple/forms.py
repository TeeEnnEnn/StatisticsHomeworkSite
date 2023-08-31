from flask_wtf import FlaskForm
from wtforms import SubmitField, DecimalField, SelectField
from wtforms.validators import DataRequired


class DataSetForm(FlaskForm):
    """
    A form used when collecting data set values
    """
    value = DecimalField("New Value", validators=[DataRequired()])
    dropdown = SelectField("Decimals:",
                           choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')],
                           validators=[DataRequired()], default=3)
    submit = SubmitField("Enter", validators=[])
