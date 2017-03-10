from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    locked = db.Column(db.Boolean)
    date_last_locked = db.Column(db.DateTime)

    def __repr__(self):
        # return '<User %r>' % self.email
        return '<User {0}> <Locked {1}>'.format(self.email, self.locked)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
