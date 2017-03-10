from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired


class EmailForm(Form):
    email = StringField('email', validators=[DataRequired()])


class BulkCreateForm(Form):
    prefix = StringField('prefix', validators=[DataRequired()])
    domain = StringField('domain', validators=[DataRequired()])
    count = StringField('count', validators=[DataRequired()])