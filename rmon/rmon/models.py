"""rmon.model
function all model and serialize
"""

from flask_sqlalchemy import SQLAlchemy

from datetime import datetime

db = SQLAlchemy()

class Server(db.Model):
    """
    Redis Server Type
    """
    __tablename__ = 'redis_server'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(64),unique=True)
    description = db.Column(db.String(512))
    host = db.Column(db.String(15))
    port = db.Column(db.Integer, default=6379)
    password = db.Column(db.String())
    updated_at = db.Column(db.Datetime, default=datetime.utcnow)

    def __repr__(self):
        return '<Server(name=%s)>' % self.name

    def save(self):

        db.session.add(self)
        db.session.commit()

    def delete(self):

        db.session.delete(self)
        db.session.commit()

