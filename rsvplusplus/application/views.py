"""
views.py

URL route handlers

Note that any handler params must match the URL route params.
For example the *say_hello* handler, handling the URL route '/hello/<username>',
  must be passed *username* as the argument.

"""
from google.appengine.api import users
from google.appengine.runtime.apiproxy_errors import CapabilityDisabledError

from flask import request, render_template, flash, url_for, redirect

from flask_cache import Cache

from application import app
from decorators import login_required, admin_required
from forms import ExampleForm, UserForm, OrganizationForm, EventForm, RegisterForm 
from models import ExampleModel, User, Organization, Event, Register
import paypalrestsdk
from application import paypal_settings

# Flask-Cache (configured to use App Engine Memcache API)
cache = Cache(app)

def home():
    return redirect(url_for('list_examples'))


def say_hello(username):
    """Contrived example to demonstrate Flask's url routing capabilities"""
    return 'Hello %s' % username


@login_required
def list_examples():
    """List all examples"""
    examples = ExampleModel.query()
    form = ExampleForm()
    if form.validate_on_submit():
        example = ExampleModel(
            example_name=form.example_name.data,
            example_description=form.example_description.data,
            added_by=users.get_current_user()
        )
        try:
            example.put()
            example_id = example.key.id()
            flash(u'Example %s successfully saved.' % example_id, 'success')
            return redirect(url_for('list_examples'))
        except CapabilityDisabledError:
            flash(u'App Engine Datastore is currently in read-only mode.', 'info')
            return redirect(url_for('list_examples'))
    return render_template('list_examples.html', examples=examples, form=form)

@login_required
def edit_example(example_id):
    example = ExampleModel.get_by_id(example_id)
    form = ExampleForm(obj=example)
    if request.method == "POST":
        if form.validate_on_submit():
            example.example_name = form.data.get('example_name')
            example.example_description = form.data.get('example_description')
            example.put()
            flash(u'Example %s successfully saved.' % example_id, 'success')
            return redirect(url_for('list_examples'))
    return render_template('edit_example.html', example=example, form=form)


@login_required
def user_examples():
    """List users"""
    user = UserModel.query()
    form = UserForm()
    if form.validate_on_submit():
        user = UserModel(
            last_name=form.last_name.data,
            first_name=form.first_name.data,
            email=form.email.data,
            phone=form.phone.data,
            address=form.address.data,
            state=form.state.data,
            zip_code=form.zip_code.data,
            added_by=users.get_current_user()
        )
        try:
            example.put()
            example_id = example.key.id()
            flash(u'Example %s successfully saved.' % example_id, 'success')
            return redirect(url_for('list_examples'))
        except CapabilityDisabledError:
            flash(u'App Engine Datastore is currently in read-only mode.', 'info')
            return redirect(url_for('list_examples'))
    return render_template('list_examples.html', user=user, form=form)

@login_required
def edit_user(user_id):
    user = UserModel.get_by_id(user_id)
    form = UserForm(obj=example)
    if request.method == "POST":
        if form.validate_on_submit():
            user.last_name=form.data.get('last_name')
            user.first_name=form.data.get('first_name')
            user.email=form.data.get('email')
            user.phone=form.data.get('phone')
            user.address=form.data.get('address')
            user.state=form.data.get('state')
            user.zip_code=form.data.get('zip_code')
            user.put()
            flash(u'Example %s successfully saved.' % example_id, 'success')
            return redirect(url_for('user_examples'))
    return render_template('edit_example.html', user=user, form=form)


@login_required
def event_examples():
    """List all examples"""
    event = EventModel.query()
    form = ExampleForm()
    if form.validate_on_submit():
        event = ExampleModel(
            title=form.title.data,
            day=form.day.data,
            location=form.location.data,
            description=form.descrtiption.data,
            anchor_amount=form.anchor_amount.data,
            amount_min=form.amount_min.data,
            max_attendees=form.max_attendees.data,
            registration_start=form.registration_start.data,
            registration_end=form.registration_end.data,
            added_by=users.get_current_user()
        )
        try:
            example.put()
            example_id = example.key.id()
            flash(u'Example %s successfully saved.' % example_id, 'success')
            return redirect(url_for('event_examples'))
        except CapabilityDisabledError:
            flash(u'App Engine Datastore is currently in read-only mode.', 'info')
            return redirect(url_for('list_examples'))
    return render_template('list_examples.html', event=event, form=form)

@login_required
def edit_event(event_id):
    event = EventModel.get_by_id(event_id)
    form = EventForm(obj=example)
    if request.method == "POST":
        if form.validate_on_submit():
            event.title=form.data.get('title')
            event.day=form.data.get('day')
            event.location=form.data.get('location')
            event.description=form.data.get('descrtiption')
            event.anchor_amount=form.data.get('anchor_amount')
            event.amount_min=form.data.get('amount_min')
            event.max_attendees=form.data.get('max_attendees')
            event.registration_start=form.data.get('registration_start')
            event.registration_end=form.data.get('registration_end')
            
            event.put()
            flash(u'Example %s successfully saved.' % example_id, 'success')
            return redirect(url_for('list_examples'))
    return render_template('edit_example.html', event=event, form=form)


@login_required
def register_examples():
    """List register examples"""
    register = RegisterModel.query()
    form = RegisterForm()
    if form.validate_on_submit():
        register = RegisterModel(
            register_id=form.register.data,
            rsvp=form.rsvp.data,
            donation=form.donation.data,
            user_id=users.get_current_user()
        )
        try:
            register.put()
            register_id = register.key.id()
            flash(u'Example %s successfully saved.' % register_id, 'success')
            return redirect(url_for('list_examples'))
        except CapabilityDisabledError:
            flash(u'App Engine Datastore is currently in read-only mode.', 'info')
            return redirect(url_for('list_examples'))
    return render_template('list_examples.html', register=register, form=form)

@login_required
def edit_register(register_id):
    register = RegisterModel.get_by_id(register_id)
    form = RegisterForm(obj=example)
    if request.method == "POST":
        if form.validate_on_submit():
            register.rsvp = form.data.get('rsvp')
            register.donation = form.data.get('donation')
            
            register.put()
            flash(u'Example %s successfully saved.' % example_id, 'success')
            return redirect(url_for('register_examples'))
    return render_template('edit_register.html', register=register, form=form)


@login_required
def delete_example(example_id):
    """Delete an example object"""
    example = ExampleModel.get_by_id(example_id)
    try:
        example.key.delete()
        flash(u'Example %s successfully deleted.' % example_id, 'success')
        return redirect(url_for('list_examples'))
    except CapabilityDisabledError:
        flash(u'App Engine Datastore is currently in read-only mode.', 'info')
        return redirect(url_for('list_examples'))


@admin_required
def admin_only():
    """This view requires an admin account"""
    return 'Super-seekrit admin page.'


@cache.cached(timeout=60)
def cached_examples():
    """This view should be cached for 60 sec"""
    examples = ExampleModel.query()
    return render_template('list_examples_cached.html', examples=examples)


def warmup():
    """App Engine warmup handler
    See http://code.google.com/appengine/docs/python/config/appconfig.html#Warming_Requests

    """
    return ''

