import datetime

from app import models, db


def create_user(email):
    u = models.User(email=email, locked=False, date_last_locked=datetime.datetime.utcnow())
    db.session.add(u)
    db.session.commit()


def delete_user(user):
    db.session.delete(user)
    db.session.commit()


def lock_user(user):
    user.locked = True
    user.date_last_locked = datetime.datetime.utcnow()
    db.session.commit()


def unlock_user(user):
    user.locked = False
    db.session.commit()
