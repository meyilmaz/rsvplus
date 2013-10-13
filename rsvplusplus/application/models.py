"""
models.py

App Engine datastore models

"""


from google.appengine.ext import ndb


class ExampleModel(ndb.Model):
    """Example Model"""
    example_name = ndb.StringProperty(required=True)
    example_description = ndb.TextProperty(required=True)
    added_by = ndb.UserProperty()
    timestamp = ndb.DateTimeProperty(auto_now_add=True)

class User(ndb.Model):
    '''User model'''
    user_id = ndb.IntegerProperty()
    date_stamp = ndb.DateTimeProperty(auto_now_add=True)
    last_name = ndb.StringProperty()
    first_name = ndb.StringProperty()
    email = ndb.StringProperty()
    phone = ndb.StringProperty()
    address = ndb.StringProperty()
    state = ndb.StringProperty()
    zip = ndb.StringProperty()
    password = ndb.StringProperty()
    org_id = ndb.StringProperty()

class Organization(ndb.Model):
    '''Organizational Model'''
    org_id = ndb.IntegerProperty()
    date_stamp = ndb.DateTimeProperty(auto_now_add=True)
    org_name = ndb.StringProperty()
    org_address = ndb.StringProperty()
    org_state = ndb.StringProperty()
    org_zip = ndb.StringProperty()
    org_email = ndb.StringProperty()
    org_phone = ndb.StringProperty()
    org_type = ndb.StringProperty()

class Event(ndb.Model):
    '''Event Model'''
    event_id = ndb.IntegerProperty
    date_stamp = ndb.DateTimeProperty(auto_now_add=True)
    title = ndb.StringProperty()
    day = ndb.StringProperty()
    time = ndb.StringProperty()
    location = ndb.StringProperty()
    description = ndb.StringProperty()
    anchor_amount = ndb.StringProperty()
    amount_min = ndb.StringProperty()
    max_attendees = ndb.StringProperty()
    registration_start = ndb.StringProperty()
    registration_end = ndb.StringProperty()
    owner_id = ndb.StringProperty()

class Register(ndb.Model):
    '''Register Model'''
    register_id = ndb.StringProperty()
    date_stamp = ndb.DateTimeProperty(auto_now_add=True)
    rsvp = ndb.StringProperty()
    donation = ndb.StringProperty()
    user_id = ndb.StringProperty()
    event_id = ndb.StringProperty()