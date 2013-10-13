# -*- coding: utf-8 -*-
"""
    RSVPLUS
    ~~~~~~

    A microblog example application written as Flask tutorial with
    Flask and sqlite3.

    :copyright: (c) 2010 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""

from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash


# create our little application :)
app = Flask(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE='rsvplus.db',
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


#def init_db():
#    """Creates the database tables."""
#    with app.app_context():
#        db = get_db()
#        with app.open_resource('rsvplus.sql', mode='r') as f:
#            db.cursor().executescript(f.read())
#        db.commit()


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


@app.route('/')
def show_entries():
    #db = get_db()
    #cur = db.execute('select title, text from entries order by id desc')
    #entries = cur.fetchall()
    return render_template('show_entries.html')


@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    #db = get_db()
    #db.execute('insert into entries (title, text) values (?, ?)',
    #             [request.form['title'], request.form['text']])
    #db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

@app.route('/newaccount')
def show_user_form():
    #db = get_db()
    #cur = db.execute('select last_name, first_name, email, phone, address, city, state, zip, password text from entries order by id desc')
    #entries = cur.fetchall()
    return render_template('user_form.html')

@app.route('/newaccount_add', methods=['POST'])
#@app.route('/newaccount_add/<user_id>', methods=['POST'])
#@app.route('/newaccount_add/<user_id>/<event_id>', methods=['POST'])
def add_user_form():
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('insert into user (last_name, first_name, email, phone, address, city, zip, password) values (?, ?, ?, ?, ?, ?, ?, ?)',\
        [request.form['last_name'], request.form['first_name'], request.form['email'], request.form['phone'],\
                request.form['address'], request.form['city'],\
                request.form['zip'], request.form['password']])
    db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_org_form'))


@app.route('/neworg')
def show_org_form():
    #db = get_db()
    #cur = db.execute('select title, text from entries order by id desc')
    #entries = cur.fetchall()
    return render_template('org_form.html')


@app.route('/neworg_add', methods=['POST'])
#@app.route('/newaccount_add/<user_id>', methods=['POST'])
#@app.route('/newaccount_add/<user_id>/<event_id>', methods=['POST'])
def add_org_form():
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('''insert into organization (org_name, org_address, org_city, org_state, org_zip, org_email, org_phone, org_type) values (?, ?, ?, ?, ?, ?, ?, ?)''', 
                [request.form['org_name'], request.form['org_address'],\
                request.form['org_city'], request.form['org_state'],\
                 request.form['org_zip'], request.form['org_email'],\
                 request.form['org_phone'], request.form['org_type']])
    db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_event_form'))



@app.route('/newevent')
def show_event_form():
    #db = get_db()
    #cur = db.execute('select title, text from entries order by id desc')
    #entries = cur.fetchall()
    return render_template('event_form.html')


@app.route('/newevent_add', methods=['POST'])
#@app.route('/newaccount_add/<user_id>', methods=['POST'])
#@app.route('/newaccount_add/<user_id>/<event_id>', methods=['POST'])
def add_event_form():
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('''insert into event (title, day, time, location, description, anchor_amount, amount_min, max_attendees, registration_start, registration_end) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',\
                [request.form['title'], request.form['day'],\
                request.form['time'], request.form['location'],\
                request.form['description'], request.form['anchor_amount'],\
                request.form['amount_min'], request.form['max_attendees'],\
                request.form['registration_start'], request.form['registration_end'],\
                request.form['owner_id']])
    db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))


@app.route('/newregistration')
def show_registration_form():
    db = get_db()
    cur = db.execute('select title, text from entries order by id desc')
    entries = cur.fetchall()
    return render_template('show_entries.html', entries=entries)

@app.route('/newregistration_add', methods=['POST'])
#@app.route('/newaccount_add/<user_id>', methods=['POST'])
#@app.route('/newaccount_add/<user_id>/<event_id>', methods=['POST'])
def add_registration_form():
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('insert into registration (rsvp, donation, user_id, event_id) values (?, ?, ?, ?)',\
                 [request.form['rsvp'], request.form['donation'], request.form['user_id'], request.form['event_id']])
    db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))


if __name__ == '__main__':
    #init_db()
    app.run()