from flask_wtf import Form, validators
from wtforms import StringField, BooleanField
from wtforms import validators
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length


class EmailForm(Form):
    email = EmailField('email', validators=[DataRequired(), validators.Email()])


class BulkCreateForm(Form):
    prefix = StringField('prefix',
                         validators=[DataRequired(), Length(min=3, max=25)],
                         default='test')

    domain = StringField('domain',
                         validators=[DataRequired(), Length(min=3, max=25)],
                         default='test.com')

    count = StringField('count',
                        validators=[DataRequired(), Length(min=1, max=2)],
                        default='5')