from wtforms import Form
from flask_wtf import FlaskForm

from wtforms import StringField, TelField, IntegerField
from wtforms import EmailField
# Aqui de los valdidadores importamos el dato obligatorio y el email
from wtforms.validators import DataRequired, Email


class UserForm(Form):
  nombre = StringField('nombre')
  apaterno = StringField('apaterno')
  amaterno = StringField('amaterno')
  email = EmailField('email')
  edad = IntegerField('edad')
  
