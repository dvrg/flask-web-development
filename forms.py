from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class User(FlaskForm):
    nama    = StringField('Siapa nama kamu?', validators=[DataRequired()])
    submit  = SubmitField('Lanjutkan')