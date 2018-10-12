from flask_wtf import FlaskForm
from wtforms import validators, FloatField, SubmitField, IntegerField,

class InputForm(FlaskForm):
    input_a_number = FloatField('input',validators=[validators.InputRequired()],default=0)
    submit = SubmitField('calculate')

class PlotForm(FlaskForm):
    coefficient = IntegerField('input', validators=[validators.InputRequired()])
    plot = SubmitField('plot')

class EnergyPlotForm(FlaskForm):
    xlow = IntegerField('lower bound', validators=[validators.InputRequired()])
    xhigh = IntegerField('higher bound', validators=[validators.InputRequired()])
    plot = SubmitField('plot')