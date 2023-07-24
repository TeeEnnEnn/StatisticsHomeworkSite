from flask_wtf import FlaskForm
from wtforms import SubmitField, DecimalField, IntegerField
from wtforms.validators import DataRequired, ValidationError


class NormalForm(FlaskForm):
    def validate_mean(form, field):
        if field.data == 0:
            return
        if not field.data and field.raw_data[0] != 0:
            raise ValidationError("Mean (μ) is a required value")

    mean = DecimalField("Mean (μ)", validators=[validate_mean], render_kw={'placeholder': 'Mean'})
    standard_deviation = DecimalField("SD (σ)", validators=[DataRequired()],
                                      render_kw={'placeholder': 'Standard Deviation'})
    x = DecimalField("x", validators=[DataRequired()], render_kw={'placeholder': 'x'})
    submit = SubmitField("Calculate")


class BinomialForm(FlaskForm):
    n = IntegerField("n", validators=[DataRequired()], render_kw={'placeholder': 'Number of attempts'})
    p = DecimalField("p", validators=[DataRequired()], render_kw={'placeholder': 'Probability of success'})
    x = IntegerField("x", validators=[DataRequired()], render_kw={'placeholder': 'Number of outcomes'})
    submit = SubmitField("Calculate")


class ChiSquaredForm(FlaskForm):
    chi_square = DecimalField("Chi square", validators=[DataRequired()], render_kw={'placeholder': 'Chi Squared value'})
    freedom = IntegerField("df", validators=[DataRequired()], render_kw={'placeholder': 'Degrees of Freedom'})
    submit = SubmitField("Calculate")


class TForm(FlaskForm):
    x = DecimalField("T", validators=[DataRequired()], render_kw={'placeholder': 'T Value'})
    freedom = IntegerField("df", validators=[DataRequired()], render_kw={'placeholder': 'Degrees of Freedom'})
    submit = SubmitField("Calculate")


class FForm(FlaskForm):
    x = DecimalField("F", validators=[DataRequired()], render_kw={'placeholder': 'F value'})
    freedom_n = IntegerField("dfn", validators=[DataRequired()],
                             render_kw={'placeholder': 'Numerator Degrees of Freedom'})
    freedom_d = IntegerField("dfd", validators=[DataRequired()],
                             render_kw={'placeholder': 'Denominator Degrees of Freedom'})
    submit = SubmitField("Calculate")
