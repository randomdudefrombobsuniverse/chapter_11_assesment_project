from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Email


class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Edit Profile')

class LoginForm(FlaskForm):
    """Login Form"""
    username = StringField('Username', validators=[DataRequired(), Length(1, 64)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep Me Logged In')
    submit = SubmitField('Log in')

class RegisterForm(FlaskForm):
    """Register Form"""
    username = StringField('Username', validators=[DataRequired(), Length(1, 64)])
    email = StringField('Email',validators=[DataRequired(), Length(1, 64),Email()] )
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')

class TalktoAgentForm(FlaskForm):
    """TalktoAgent Form"""
    name = StringField('Name', validators=[DataRequired(), Length(1, 64)])
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    phone_number = StringField('Phone Number', validators=[DataRequired(), Length(1, 64)])
    body = TextAreaField('Message Body',validators=[DataRequired(), Length(1, 64),])
    submit = SubmitField('Submit')
    

class PostForm(FlaskForm):
    """Comment Form"""
    body = TextAreaField('Body', validators=[DataRequired()])
    submit = SubmitField('Post')
