import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__) # create flask application

# connect flask application with the database  
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ os.path.join(basedir, 'data.sqlite') # set the database at specified location
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app) # pass the application to the SQLAlchemy class
 
 ###########################
  class Puppy(db.Model):
      # manual table name choice:
      __tablename__='puppies'

    # attribute "id" set to col, type integer 
      id = db.Column(db.Integer, primary_key = True)

      name = db.Column(db.Text)

      age = db.Column(db.Integer)


    def __init__(self, name, age):
        self.name = name
        self. age = age

    def __repr__(self):
        return f"Puppy {self.name} is {self.age} years old."
