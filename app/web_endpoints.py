from flask import flash
from flask import render_template
from werkzeug.utils import redirect

from app import models, STATUS_404, app
from app.actions import delete_user, lock_user, unlock_user, create_user
from app.forms import EmailForm, BulkCreateForm


@app.route('/')
@app.route('/index')
def index():
    users = models.User.query.all()

    return render_template('index.html',
                           title='Test User Data Service',
                           users=users)


# @app.route('/ui_user', methods=['GET'])
# def ui_getuser():
#     users = models.User.query.all()
#     for user in users:
#         if not user.locked:
#             lock_user(user)
#             return json.dumps(user.as_dict())
#
#     return STATUS_409


@app.route('/ui_delete/<userID>', methods=['POST'])
def ui_delete(userID):
    users = models.User.query.all()
    for user in users:
        if user.id == int(userID):
            delete_user(user)
            return redirect('/index')
    return STATUS_404


@app.route('/ui_lock/<userID>', methods=['GET', 'POST'])
def ui_lock(userID):
    users = models.User.query.all()
    for user in users:
        if user.id == int(userID):
            lock_user(user)
            return redirect('/index')
    return STATUS_404


@app.route('/ui_unlock/<userID>', methods=['GET', 'POST'])
def ui_unlock(userID):
    users = models.User.query.all()
    for user in users:
        if user.id == int(userID):
            unlock_user(user)
            return redirect('/index')
    return STATUS_404


@app.route('/ui_create', methods=['GET', 'POST'])
def ui_create_user():
    form = EmailForm()
    if form.validate_on_submit():
        flash('New user requested with email "%s"' %
              form.email.data)
        create_user(form.email.data)

        return redirect('/index')
    return render_template('create.html',
                           title='Create a new test user',
                           form=form)


@app.route('/ui_bulkcreate', methods=['GET', 'POST'])
def ui_bulk_create_user():
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
