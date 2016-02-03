from flask.ext.wtf import Form
from wtforms import IntegerField, TextField, HiddenField
from wtforms.validators import Required, Length, NumberRange
from flask.ext.babel import gettext


class DropBike(Form):
    ''' Form for dropping off a bike. '''

    start = TextField(validators=[Required, Length(5)],
                      description=gettext('Where are you'))
    time = TextField(validators=[Required],
                     description=gettext('Where you want to go'))
    people = IntegerField(validators=[Required, NumberRange(0, 12)],
                          description=gettext('Number of people'))

class PickBike(Form):
    ''' Form for dropping off a bike. '''

    start = TextField(validators=[Required, Length(5)],
                      description=gettext('Where are you'))
    time = TextField(validators=[Required],
                     description=gettext('Where you want to go'))
    people = IntegerField(validators=[Required, NumberRange(0, 12)],
                          description=gettext('Number of people'))

class Trip(Form):
    ''' Form for dropping off a bike. '''

    start = TextField(validators=[Required, Length(5)],
                      description=gettext('Where are you'))
    end = TextField(validators=[Required, Length(5)],
                    description=gettext('Where you want to go'))
    time = TextField(validators=[Required, Length(5, 5)],
                     description='Departure time')
    people = IntegerField(validators=[Required, NumberRange(0, 12)],
                          description=gettext('Number of people'))
