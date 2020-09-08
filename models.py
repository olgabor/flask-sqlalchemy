from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #might be removed with next release 
app.config['SQLALCHEMY_ECHO'] = True #allows to see what sqlalchamy is doing, returns the log of actions 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/flasql'

db = SQLAlchemy(app)

class User(db.Model): 
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    bio = db.Column(db.String(150))

    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f'User(id={self.id}, email="{self.email}", name="{self.name}")'

#     def as_dict(self, __tablename__):
#         return {
#             id: self.id,
#             name: self.name,
#             email: self.email,
#             bio: self.bio
#   }


    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns} #dictionary comprehension 
    

post_tags = db.Table('post_tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'), primary_key=True),
    db.Column('post_id', db.Integer, db.ForeignKey('posts.id'), primary_key=True))

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    Header = db.Column(db.String(150), unique=True, nullable=False)
    #author_id sets up one to many relationships between Users -> Posts 
    author_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='SET NULL')) #if user gets deleted this field gets deleted 
    body = db.Column(db.String, nullable=False)

    #many to many relationship 
    tags = db.relationship('Tag', secondary=post_tags, lazy='subquery',
        backref=db.backref('posts', lazy=True))

    def __repr__(self):
          return f'Post(id={self.id}, header="{self.Header}", author_id="{self.author_id}")'

class Tag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
          return f'Tag(id={self.id}, tag={self.tag})'


#create database 
#psql 
#CREATE DATABASE flasql
#quit q\

# Run ipython shell = we have access to the code we written 
#ipython 
#from models import db
# db.create_all() # creates all tables 