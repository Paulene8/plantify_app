from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class RegisterForm(FlaskForm):
    username = StringField('Username')
    title = StringField('Title')
    post = SubmitField('Post')