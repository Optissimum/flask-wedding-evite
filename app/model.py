from app import database
from flask_wtf import Form
from wtforms import TextAreaField, BooleanField, IntegerField, TextField
from wtforms.validators import InputRequired, Length

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

class Settings(database.Model):
    id = database.Column(database.Integer(), primary_key=True)
    partners = database.Column(database.String())
    color_main = database.Column(database.String())
    color_acc1 = database.Column(database.String())
    color_acc2 = database.Column(database.String())
    color_acc3 = database.Column(database.String())
    color_acc4 = database.Column(database.String())

class UserForm(Form):
    name = TextField(
        'Name', [InputRequired()]
    )
    email = TextField(
        'Email', [InputRequired(), Length(min=6, max=40)]
    )
    address = TextAreaField(
        'Address', [InputRequired()]
    )
    rsvp = BooleanField(
        'RSVP', [InputRequired()]
    )
    plusone = IntegerField(
        'Plus One', [InputRequired()]
    )
    limitations = TextAreaField(
        'Dietary Restrictions', [InputRequired()]
    )

class SettingsForm(Form):
    partners = TextAreaField(
        'Names of Partners', [InputRequired()]
    )
    colorMain = TextField(
        'Main Color', [InputRequired(), Length(min=6, max=6)]
    )
    colorAccent1 = TextField(
        'Accent Color', [InputRequired(), Length(min=6, max=6)]
    )
    colorAccent2 = TextField(
        'Accent Color', [InputRequired(), Length(min=6, max=6)]
    )
    colorAccent3 = TextField(
        'Accent Color', [InputRequired(), Length(min=6, max=6)]
    )
    colorAccent4 = TextField(
        'Accent Color', [InputRequired(), Length(min=6, max=6)]
    )

database.create_all()
