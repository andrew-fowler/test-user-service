from flask import json
from flask import request
from werkzeug.utils import redirect

from app import STATUS_200, STATUS_409, STATUS_404, app
from app import models
from app.actions import create_user, lock_user, delete_user, unlock_user


@app.route('/ping', methods=['GET'])
def ping():
    return STATUS_200


@app.route('/user', methods=['POST'])
def user_post():
    create_user(request.form.email.data)
    return STATUS_200
    # TODO: implement error handling


@app.route('/user', methods=['GET'])
def user_get():
    users = models.User.query.all()
    for user in users:
        if not user.locked:
            lock_user(user)
            return json.dumps(user.as_dict())

    return STATUS_409


@app.route('/user/<userID>', methods=['DELETE'])
def user_delete(userID):
    users = models.User.query.all()
    for user in users:
        if user.id == int(userID):
            delete_user(user)
            return STATUS_200

    return STATUS_404


@app.route('/lock/<userID>', methods=['POST'])
def lock_post(userID):
    users = models.User.query.all()
    for user in users:
        if user.id == int(userID):
            lock_user(user)
            return STATUS_200

    return STATUS_404


@app.route('/lock/<userID>', methods=['DELETE'])
def lock_delete(userID):
    users = models.User.query.all()
    for user in users:
        if user.id == int(userID):
            unlock_user(user)
            return STATUS_200

    return STATUS_404