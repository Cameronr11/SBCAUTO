from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class SBCForm(FlaskForm):
    formation = SelectField('Formation', choices=[('4-4-2', '4-4-2'), ('4-3-3', '4-3-3'), ('3-5-2', '3-5-2')], validators=[DataRequired()])
    criteria = SelectField('Criteria', choices=[('criteria1', 'Criteria 1'), ('criteria2', 'Criteria 2'), ('criteria3', 'Criteria 3')], validators=[DataRequired()])
    submit = SubmitField('Solve SBC')
