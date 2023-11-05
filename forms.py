from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class CookieForm(FlaskForm):
    key = StringField('Ключ:')
    value = StringField('Значення:')
    expires = IntegerField('Термін дії (секунди):')
    submit = SubmitField('Додати кукі')
