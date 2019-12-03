from sqlalchemy import Column, String
from api.app import db


class User(db.Model):
    __tablename__ = 'user'

    uuid = Column(String, primary_key=True)
    name = Column(String)
    email = Column(String)

    def __repr__(self):
        return "<User(name='%s', uuid='%s', email='%s')>" % (self.name, self.uuid, self.email)

