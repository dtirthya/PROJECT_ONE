from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

class RegistrationForm(FlaskForm):
    first_name = StringField("FIRST NAME", validators=[DataRequired()])
    middle_name = StringField("MIDDLE NAME")
    last_name = StringField("LAST NAME", validators=[DataRequired()])
    email = StringField("EMAIL", validators=[DataRequired(), Email()])
    password = StringField("PASSWORD", validators=[DataRequired()])
    confirm_password = StringField("CONFIRM PASSWORD", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("SIGN UP")

class LoginForm(FlaskForm):
    email = StringField("EMAIL", validators=[DataRequired(), Email()])
    password = StringField("PASSWORD", validators=[DataRequired()])
    submit = SubmitField("LOGIN")