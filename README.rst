This software is a browser for D20 system data.

This is capable of using Open Game Content licensed SRD data, and custom
personal data.

Requirements
============

* Python 2.6 or a higher version of Python 2.x
* Django 1.2
* Django South 0.7.x (tested with 0.7.3)
* Some database engine supported by Django (SQLite3 used in the default config)

Quick start instructions
========================

The following instructions are for installing and deploying locally. If you
need to install this in a public server read the Django documentation about
deploying Django sites.

Install the requirements, and virtualenv. virtualenv is not a requirement, but
it is a good idea to have. Then run the following commands::

 virtualenv --no-site-packages srd20
 source srd20/bin/activate
 cd srd20
 easy_install django south
 git clone https://github.com/machinalis/django-srd20.git django_srd20
 cd django_srd20

At this point you can customize settings.py or add a local_settings.py; but
the defaults should work.

The first time you should should setup the database in the following way::

 ./manage.py syncdb # This will ask for an admin password
 ./manage migrate

Doing this again later won't break anything, but is not required. You can also
load some of the provided OGL licensed content into the database with the
following command::

 ./manage.py loaddata srd20/fixtures/srd.json

To run a development server that you can access with a web browser::

 ./manage runserver

While the above is running (until interrupting with CTRL+C) you can point a
browser to http://127.0.0.1:8000/ and use the application

