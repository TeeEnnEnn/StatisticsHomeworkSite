from flask_wtf import FlaskForm
from wtforms import SubmitField, DecimalField, IntegerField
from wtforms.validators import DataRequired, ValidationError


def validate_required(form, field):
    """
    A function used to validate whether an input is required.
    :param form: The form upon which this function is acting
    :param field: The field to validate
    :return: None
    """
    if field.data == 0:
        return
    if not field.data and field.raw_data[0] != 0:
        raise ValidationError(f"{field.label.text} is a required value")


class NormalForm(FlaskForm):
    """
    A form used for the normal distribution
    """
    mean = DecimalField("Mean (μ)", validators=[validate_required], render_kw={'placeholder': 'Mean'})
    standard_deviation = DecimalField("SD (σ)", validators=[DataRequired()],
                                      render_kw={'placeholder': 'Standard Deviation'})
    x = DecimalField("x", validators=[DataRequired()], render_kw={'placeholder': 'x'})
    submit = SubmitField("Calculate")


class BinomialForm(FlaskForm):
    """
    A form used for the binomial distribution
    """
    n = IntegerField("n", validators=[DataRequired()], render_kw={'placeholder': 'Number of attempts'})
    p = DecimalField("p", validators=[DataRequired()], render_kw={'placeholder': 'Probability of success'})
    x = IntegerField("x", validators=[DataRequired()], render_kw={'placeholder': 'Number of outcomes'})
    submit = SubmitField("Calculate")


class ChiSquaredForm(FlaskForm):
    """
    A form used for the chi squared distribution
    """
    chi_square = DecimalField("Chi square", validators=[DataRequired()], render_kw={'placeholder': 'Chi Squared value'})
    freedom = IntegerField("df", validators=[DataRequired()], render_kw={'placeholder': 'Degrees of Freedom'})
    submit = SubmitField("Calculate")


class TForm(FlaskForm):
    """
    A form used for the T distribution
    """
    x = DecimalField("T", validators=[DataRequired()], render_kw={'placeholder': 'T Value'})
    freedom = IntegerField("df", validators=[DataRequired()], render_kw={'placeholder': 'Degrees of Freedom'})
    submit = SubmitField("Calculate")


class FForm(FlaskForm):
    """
    A form used for the F distribution
    """
    x = DecimalField("F", validators=[DataRequired()], render_kw={'placeholder': 'F value'})
    freedom_n = IntegerField("dfn", validators=[DataRequired()],
                             render_kw={'placeholder': 'Numerator Degrees of Freedom'})
    freedom_d = IntegerField("dfd", validators=[DataRequired()],
                             render_kw={'placeholder': 'Denominator Degrees of Freedom'})
    submit = SubmitField("Calculate")


class PoissonForm(FlaskForm):
    """
    A form used for the Poisson distribution
    """
    k = IntegerField("k", validators=[DataRequired()], render_kw={'placeholder': 'k'})
    mean = DecimalField("λ", validators=[DataRequired()], render_kw={'placeholder': 'λ'})
    submit = SubmitField("Calculate")


class GeometricForm(FlaskForm):
    """
    A form used for the geometric distribution
    """
    n = IntegerField("n", validators=[DataRequired()], render_kw={'placeholder': 'Number of attempts'})
    p = DecimalField("p", validators=[DataRequired()], render_kw={'placeholder': 'Probability of success'})
    submit = SubmitField("Calculate")
