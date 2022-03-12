'''IF IMPLEMENTING AN APP WITH LOGIN FUNCTIONALITY

TODO - UNCOMMENT ALL
'''


from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Required, Email, EqualTo, Length
from ..models import User
from wtforms import ValidationError

class LoginForm(FlaskForm):
    username = StringField('Username',validators=[Required()])
    password = PasswordField('Password',validators=[Required()])
    remember = BooleanField('Remember Me!')
    submit = SubmitField('Login')

class RegForm(FlaskForm):
    email = StringField('Your Email Address', validators=[Required(),Email()])
    username = StringField('Enter Your Username', validators=[Required(),Length(min=5, max=20)])
    password = PasswordField('Password',validators = [Required(), EqualTo('password_confirm',message = 'Passwords must match'),Length(min=6, max=20)])
    password_confirm = PasswordField('Confirm Passwords',validators = [Required()])
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError("The Email has already been taken!")
    
    def validate_username(self, data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError("The username has already been taken")
