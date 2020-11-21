import datetime
import hashlib

from ..base import db
from flask_login import UserMixin
from flask import current_app as app


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)

    _email = db.Column(db.String(), nullable=False, unique=True)
    _first_name = db.Column(db.String(), nullable=False)
    _last_name = db.Column(db.String(), nullable=False)
    _password = db.Column(db.String(), nullable=False)
    _registered_on = db.Column(db.DateTime(), nullable=False)
    _confirmed_account = db.Column(db.Boolean(), nullable=False, default=False)
    _confirmed_on = db.Column(db.DateTime(), nullable=True)

    def __init__(self, email, password, first_name, last_name):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self._register_on = datetime.datetime.now()

    @staticmethod
    def hash_password(password):
        return hashlib.md5((password + app.config['PASSWORD_SALT']).encode('utf-8')).hexdigest()

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def password(self):
        return self._email

    @password.setter
    def password(self, value):
        self._email = self.hash_password(value)

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value[:64]

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value[:64]

    @property
    def registered_on(self):
        return self._registered_on

    @property
    def confirmed_account(self):
        return self._confirmed_account

    def confirm_account(self):
        self._register_on = datetime.datetime.now()
        self._confirmed_account = True
