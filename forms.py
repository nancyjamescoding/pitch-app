from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, IntegerField
from wtforms.validators import InputRequired, Length


class LogInForms(FlaskForm):
    username = StringField("username", validators=[
                           InputRequired(), Length(min=4, max=15)])
    password = PasswordField("password", validators=[
                             InputRequired(), Length(min=8, max=80)])
    remember = BooleanField("remember me")


class SignupForm(FlaskForm):
    username = StringField("username", validators=[
                           InputRequired(), Length(min=4, max=15)])
    password = PasswordField("password", validators=[
                             InputRequired(), Length(min=8, max=80)])
    remember = BooleanField("remember me")


class ScheduledForm(FlaskForm):
    username = StringField("username", validators=[
                           InputRequired(), Length(min=4, max=15)])
    password = PasswordField("password", validators=[
                             InputRequired(), Length(min=8, max=80)])
    remember = BooleanField("remember me")
