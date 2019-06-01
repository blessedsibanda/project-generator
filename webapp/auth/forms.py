from flask_wtf import FlaskForm as Form  
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo

from .models import User


class LoginForm(Form):
    email = StringField('Email', [DataRequired(), Email()])
    password = PasswordField('Password', [DataRequired()])
    remember = BooleanField("Remember Me")

    def validate(self):
        is_valid = super(LoginForm, self).validate()
        if not is_valid:
            return False
        user = User.query.filter_by(email=self.email.data).first()
        if not user:
            self.email.errors.append('Invalid email or password')
            return False
        if not user.check_password(self.password.data):
            self.email.errors.append('Invalid email or password')
            return False
        return True


class RegisterForm(Form):
    username = StringField('Username', [DataRequired(), Length(min=2,max=255)])
    email = StringField('Email', [DataRequired(), Email()])
    password = PasswordField('Password', [DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', [DataRequired(), EqualTo('password')])

    def validate(self):
        is_valid = super(LoginForm, self).validate()
        if not is_valid:
            return False
        user = User.query.filter_by(email=self.email.data).first()
        if user:
            self.email.errors.append('Email address already in use')
            return False
        user = User.query.filter_by(username=self.username.data).first()
        if user:
            self.username.errors.append('User with that username already exists')
            return False
        return True

