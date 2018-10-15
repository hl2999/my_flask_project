from flask_wtf import FlaskForm
from wtforms import validators, FloatField, SubmitField, IntegerField, StringField, PasswordField

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

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[validators.InputRequired(), validators.Length(min=2, max=20)])
    password = PasswordField('Password', validators=[validators.InputRequired(), ])
    confirm_password = PasswordField('Confirm Password', validators=[validators.InputRequired(), validators.EqualTo('password')])
    submit = SubmitField('Sign Up')