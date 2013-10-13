CREATE TABLE user
(user_id integer primary key autoincrement
date_stamp DATETIME DEFAULT CURRENT_TIMESTAMP,
last_name text,
first_name text,
email text,
phone text,
address text,
org_state text,
org_zip text,
password text,
org_id integer);

CREATE TABLE organization
(org_id integer primary key autoincrement,
date_stamp DATETIME DEFAULT CURRENT_TIMESTAMP,
org_name text,
org_address text,
org_state text,
org_zip text,
org_email text,
org_phone text,
org_type text);

CREATE TABLE event
(event_id integer primary key autoincrement,
date_stamp DATETIME DEFAULT CURRENT_TIMESTAMP,
title text,
day text,
time integer,
location text,
description text,
anchor_amount real,
amount_min real,
max_attendees integer,
registration_start integer,
registration_end integer,
owner_id integer); /* This is must be a user_id */


CREATE TABLE register
(register_id integer,
date_stamp DATETIME DEFAULT CURRENT_TIMESTAMP,
rsvp text, /* Yes, No or null */
donation real,
user_id integer,
event_id integer);


