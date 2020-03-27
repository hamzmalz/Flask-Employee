from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, TimeField
from wtforms.validators import DataRequired, Email

class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email(message='Enter valid email address')])
    phone = FloatField('Phone', validators=[DataRequired()])
    hourly = FloatField('Hourly Rate', validators=[DataRequired()])
    submit = SubmitField('Register')

class PunchInForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    time_in = TimeField('Time In', validators=[DataRequired()])
    submit = SubmitField('Submit')

class PunchOutForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    time_out = TimeField('Time Out', validators=[DataRequired()])
    submit = SubmitField('Submit')

