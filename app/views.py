import datetime

from flask import flash
from flask import json
from flask import render_template
from werkzeug.utils import redirect

from app import app
from app import models
from app.actions import create_user, unlock_user, lock_user, delete_user
from app.forms import EmailForm, BulkCreateForm

STATUS_200 = json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
STATUS_404 = json.dumps({'success': False}), 404, {'ContentType': 'application/json'}
STATUS_409 = json.dumps({'success': False}), 409, {'ContentType': 'application/json'}

@app.route('/')
@app.route('/index')
def index():
    users = models.User.query.all()

    return render_template('index.html',
                           title='Test User Data Service',
                           users=users)


@app.route('/ping', methods=['GET'])
def ping():
    return STATUS_200


@app.route('/getuser', methods=['GET'])
def getuser():
    users = models.User.query.all()
    for user in users:
        if not user.locked:
            lock_user(user)
            return json.dumps(user.as_dict())

    return STATUS_409


@app.route('/delete/<userID>', methods=['POST'])
def delete(userID):
    users = models.User.query.all()
    for user in users:
        if user.id == int(userID):
            delete_user(user)
            return redirect('/index')
    return STATUS_404


@app.route('/lock/<userID>', methods=['GET', 'POST'])
def lock(userID):
    users = models.User.query.all()
    for user in users:
        if user.id == int(userID):
            lock_user(user)
            return redirect('/index')
    return STATUS_404


@app.route('/unlock/<userID>', methods=['GET', 'POST'])
def unlock(userID):
    users = models.User.query.all()
    for user in users:
        if user.id == int(userID):
            unlock_user(user)
            return redirect('/index')
    return STATUS_404


@app.route('/create', methods=['GET', 'POST'])
def create():
    form = EmailForm()
    if form.validate_on_submit():
        flash('New user requested with email "%s"' %
              form.email.data)
        create_user(form.email.data)

        return redirect('/index')
    return render_template('create.html',
                           title='Create a new test user',
                           form=form)


@app.route('/bulkcreate', methods=['GET', 'POST'])
def bulkcreate():
    form = BulkCreateForm()
    if form.validate_on_submit():
        flash('New users bulk created')
        count = int(form.count.data)
        prefix = form.prefix.data
        domain = form.domain.data

        for i in range(count):
            email = "{0}{1}@{2}".format(prefix, i, domain)
            create_user(email)

        return redirect('/index')
    return render_template('bulkcreate.html',
                           title='Create a number of new test users',
                           form=form)
