from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

engine=None
Base=declarative_base()
db = SQLAlchemy()

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(30), nullable=True)
    password = db.Column(db.String(20), nullable=False)
    last_login = db.Column(db.DateTime, nullable=True)
    issues = db.relationship('Issue', backref='user', lazy='dynamic')

    def get_id(self):
        return str(self.user_id)

class Librarian(db.Model):
    __tablename__ = 'librarian'
    librarian_id = db.Column(db.Integer, primary_key=True)
    librarian_email = db.Column(db.String(30), nullable=True)
    password = db.Column(db.String(20), nullable=False)

class Section(db.Model):
    section_id = db.Column(db.Integer, primary_key=True)
    section_name = db.Column(db.String(20), unique=True, nullable=False)
    books = db.relationship('Book', backref='section', lazy='dynamic')

class Issue(db.Model):
    issue_id = db.Column(db.Integer, primary_key=True)
    issue_date = db.Column(db.Date)
    book_id = db.Column(db.Integer, db.ForeignKey('book.book_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    status = db.Column(db.String(20))

class Book(db.Model):
    book_id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(20), unique=True, nullable=False)
    authors = db.Column(db.String(50), nullable=False)
    file_data = db.Column(db.String(1000), nullable=False)
    section_id = db.Column(db.Integer, db.ForeignKey('section.section_id'))
    issues = db.relationship('Issue', backref='book', lazy='dynamic')

