from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from flask import Flask


# class Note(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     data = db.Column(db.String(10000))
#     date = db.Column(db.DateTime(timezone=True), default=func.now())
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    Last_name = db.Column(db.String(150), default="")
    Middle_name = db.Column(db.String(150), default="")
    Mobile = db.Column(db.Integer, default="")
    Address = db.Column(db.String(150), default="")
    income = db.Column(db.Integer, default="")
    Pay_Interval = db.Column(db.String(150), default="")
    Relationship_Stauts = db.Column(db.String(150), default="")
    Dependants = db.Column(db.Integer, default="")       
    Housing_Situation = db.Column(db.String(150), default="")
    Liabilities = db.Column(db.Integer, default="")       
    Food = db.Column(db.Integer, default="")   
    Utilities  = db.Column(db.Integer, default="")  
    Entertainment = db.Column(db.Integer, default="")  
    Clothing = db.Column(db.Integer, default="")  
    Home = db.Column(db.Integer, default="")  
    Private_Insurance = db.Column(db.Integer, default="")  
    Memberships = db.Column(db.Integer, default="")  
    Child_Support = db.Column(db.Integer, default="")  
    Education_Cost = db.Column(db.Integer, default="")  
    Employment_Type = db.Column(db.String(150), default="")
    Occupation =  db.Column(db.String(150), default="")
    Company_Name =  db.Column(db.String(150), default="")
    Service_Time =  db.Column(db.Integer, default="")
    Credit_Limit =  db.Column(db.Integer, default="")