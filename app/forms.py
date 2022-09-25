from flask_wtf import FlaskForm
from wtforms import  StringField, PasswordField, BooleanField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class RegistrationForm(FlaskForm):
    reddit_username = StringField('Reddit Username', validators=[DataRequired()])
    course = StringField('Course/Industry', validators=[DataRequired()])
    response_join = TextAreaField('Why do you want to join?', validators=[Length(min = 1, message = 'enter a minimum of 50 characters')])
    response_goal = TextAreaField('What are your current Study Goals?', validators=[Length(min = 1, message = 'enter a minimum of 50 characters')])
    response_pain = TextAreaField('What are your pain-points when Self-Studying?', validators=[Length(min = 1, message = 'enter a minimum of 50 characters')])
    response_expect = TextAreaField('What do you expect from our Community?', validators=[Length(min = 1, message = 'enter a minimum of 50 characters')])
    submit = SubmitField('Submit')
    
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign in')