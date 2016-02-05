from flask.ext.wtf import Form
from wtforms import IntegerField, TextField, HiddenField, SelectField
from wtforms.validators import Required, Length, NumberRange
from flask.ext.babel import gettext


class DropBike(Form):
    ''' Form for dropping off a bike. '''

    start = TextField(validators=[Required, Length(5)],
                      description=gettext('Where are you ?'))
    time = TextField(validators=[Required],
                     description=gettext('Departure time'))
    people = SelectField(description='Number of people', choices=[
        (str(i), str(i)) for i in range(1, 9)
    ], validators=[Required])


class PickBike(Form):
    ''' Form for dropping off a bike. '''

    start = TextField(validators=[Required, Length(5)],
                      description=gettext('Where are you ?'))
    time = TextField(validators=[Required],
                     description=gettext('Departure time'))
    people = SelectField(description='Number of people', choices=[
        (str(i), str(i)) for i in range(1, 9)
    ], validators=[Required])


class FullTrip(Form):
    ''' Form for dropping off a bike. '''

    start = TextField(validators=[Required, Length(5)],
                      description=gettext('Where are you ?'))
    end = TextField(validators=[Required, Length(5)],
                    description=gettext('Where you want to go ?'))
    time = TextField(validators=[Required, Length(5, 5)],
                     description='Departure time')
    people = SelectField(description='Number of people', choices=[
        (str(i), str(i)) for i in range(1, 9)
    ], validators=[Required])
