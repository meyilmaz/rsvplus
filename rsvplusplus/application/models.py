"""
models.py

App Engine datastore models

"""


from google.appengine.ext import ndb


class ExampleModel(ndb.Model):
    """Example Model"""
    example_name = ndb.StringProperty(required=True)
    example_description = ndb.TexProperty(required=True)
    added_by = ndb.UserProperty()
    timestamp = ndb.DateTimeProperty(auto_now_add=True)

class User(ndb.Model):
    '''User model'''
    user_id = ndb.IntegerProperty()
    date_stamp = ndb.DateTimeProperty(auto_now_add=True)
    last_name = nbd.StringProperty()
    first_name = nbd.StringProperty()
    email = nbd.StringProperty()
    phone = nbd.StringProperty()
    address = nbd.StringProperty()
    state = nbd.StringProperty()
    zip = nbd.StringProperty()
    password = nbd.StringProperty()
    org_id = nbd.StringProperty()

class Organization(ndb.Model):
    '''Organizational Model'''
    org_id = nbd.IntegerProperty()
    date_stamp = ndb.DateTimeProperty(auto_now_add=True)
    org_name = nbd.StringProperty()
    org_address = nbd.StringProperty()
    org_state = nbd.StringProperty()
    org_zip = nbd.StringProperty()
    org_email = nbd.StringProperty()
    org_phone = nbd.StringProperty()
    org_type = nbd.StringProperty()

class Event(ndb.Model):
    '''Event Model'''
    event_id = nbd.IntegerProperty
    date_stamp = ndb.DateTimeProperty(auto_now_add=True)
    title = nbd.StringProperty()
    day = nbd.StringProperty()
    time = nbd.StringProperty()
    location = nbd.StringProperty()
    description = nbd.StringProperty()
    anchor_amount = nbd.StringProperty()
    amount_min = nbd.StringProperty()
    max_attendees = nbd.StringProperty()
    registration_start = nbd.StringProperty()
    registration_end = nbd.StringProperty()
    owner_id = nbd.StringProperty()

class Register(ndb.Model):
    '''Register Model'''
    register_id = nbd.StringProperty()
    date_stamp = ndb.DateTimeProperty(auto_now_add=True)
    rsvp text = nbd.StringProperty()
    donation = nbd.StringProperty()
    user_id = nbd.StringProperty()
    event_id = nbd.StringProperty()