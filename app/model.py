from app import database
from flask_wtf import Form
from wtforms import TextAreaField, BooleanField, IntegerField, TextField
from wtforms.validators import DataRequired, Length

class Guest(database.Model):
    email = database.Column(database.String(), primary_key = True)
    name = database.Column(database.String())
    address = database.Column(database.String())
    rsvp = database.Column(database.Boolean())
    limitations = database.Column(database.String())
    plusone = database.Column(database.Integer())

    def __init__(self, name, email, plusone, address, limitations, rsvp):
        self.name = name
        self.email = email
        self.plusone = plusone
        self.address = address
        self.limitations = limitations
        self.rsvp = rsvp

class UserForm(Form):
    name = TextField(
        'Name', validators=[DataRequired()]
    )
    email = TextField(
        'Email', validators=[DataRequired(), Length(min=6, max=40)]
    )
    address = TextAreaField(
        'Address', validators=[DataRequired()]
    )
    rsvp = BooleanField(
        'RSVP', validators=[DataRequired()]
    )
    plusone = IntegerField(
        'Plus One', validators=[DataRequired()]
    )
    limitations = TextAreaField(
        'Dietary Restrictions', validators=[DataRequired()]
    )

database.create_all()
