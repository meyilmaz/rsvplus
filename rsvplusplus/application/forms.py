"""
forms.py

Web forms based on Flask-WTForms

See: http://flask.pocoo.org/docs/patterns/wtforms/
     http://wtforms.simplecodes.com/

"""

from flaskext import wtf
from flaskext.wtf import validators
from wtforms.ext.appengine.ndb import model_form

from .models import ExampleModel, User, Organization, Event, Register


class ClassicExampleForm(wtf.Form):
    example_name = wtf.TextField('Name', validators=[validators.Required()])
    example_description = wtf.TextAreaField('Description', validators=[validators.Required()])

# App Engine ndb model form example
ExampleForm = model_form(ExampleModel, wtf.Form, field_args={
    'example_name': dict(validators=[validators.Required()]),
    'example_description': dict(validators=[validators.Required()]),
})

# App Engine ndb model form example
UserForm = model_form(User, wtf.Form, field_args={
    'user_id': dict(validators=[validators.Required()]),
    'date_stamp': dict(validators=[validators.Required()]),
    'last_name': dict(validators=[validators.Required()]),
    'first_name': dict(validators=[validators.Required()]),
    'email': dict(validators=[validators.Required()]),
    'phone': dict(validators=[validators.Required()]),
    'address': dict(validators=[validators.Required()]),
    'state': dict(validators=[validators.Required()]),
    'zip_code': dict(validators=[validators.Required()]),
    'password': dict(validators=[validators.Required()]),
    'org_id': dict(validators=[validators.Required()])
})

OrganizationForm = model_form(Organization, wtf.Form, field_args={
    'org_id': dict(validators=[validators.Required()]),
    'date_stamp': dict(validators=[validators.Required()]),
    'org_name': dict(validators=[validators.Required()]),
    'org_address': dict(validators=[validators.Required()]),
    'org_state': dict(validators=[validators.Required()]),
    'org_zip': dict(validators=[validators.Required()]),
    'org_email': dict(validators=[validators.Required()]),
    'org_phone': dict(validators=[validators.Required()]),
    'org_type': dict(validators=[validators.Required()])
    
})

EventForm = model_form(Event, wtf.Form, field_args={
    'event_id': dict(validators=[validators.Required()]),
    'date_stamp': dict(validators=[validators.Required()]),
    'title': dict(validators=[validators.Required()]),
    'day': dict(validators=[validators.Required()]),
    'time': dict(validators=[validators.Required()]),
    'location': dict(validators=[validators.Required()]),
    'description': dict(validators=[validators.Required()]),
    'anchor_amount': dict(validators=[validators.Required()]),
    'amount_min': dict(validators=[validators.Required()]),
    'max_attendees': dict(validators=[validators.Required()]),
    'registration_start': dict(validators=[validators.Required()]),
    'registration_end': dict(validators=[validators.Required()]),
    'owner_id': dict(validators=[validators.Required()])
})

RegisterForm = model_form(Register, wtf.Form, field_args={
    'register_id': dict(validators=[validators.Required()]),
    'date_stamp': dict(validators=[validators.Required()]),
    'rsvp': dict(validators=[validators.Required()]),
    'donatation': dict(validators=[validators.Required()]),
    'user_id': dict(validators=[validators.Required()]),
    'event_id': dict(validators=[validators.Required()])

})

'''Register Model'''
    register_id = ndb.StringProperty()
    date_stamp = ndb.DateTimeProperty(auto_now_add=True)
    rsvp = ndb.StringProperty()
    donation = ndb.StringProperty()
    user_id = ndb.StringProperty()
    event_id = ndb.StringProperty()

