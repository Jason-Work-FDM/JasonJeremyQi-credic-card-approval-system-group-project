from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


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
    Mobile = db.Column(db.Integer, default=0)
    Address = db.Column(db.String(150), default="")
    income = db.Column(db.Integer, default=0)    
    Pay_Interval = db.Column(db.String(150), default="")
    Other_Income = db.Column(db.Integer, default=0)
    Pay_Interval_2 = db.Column(db.String(150), default="")
    Relationship_Status = db.Column(db.String(150), default="")
    Dependants = db.Column(db.Integer, default=0)       
    Housing_Situation = db.Column(db.String(150), default="")
    Home_Loans = db.Column(db.Integer, default=0)
    Personal_Loans = db.Column(db.Integer, default=0)
    Credit_Cards_Repayment = db.Column(db.Integer, default=0)
    Other_Liability = db.Column(db.Integer, default=0)           
    Food = db.Column(db.Integer, default=0)   
    Utilities  = db.Column(db.Integer, default=0)  
    Entertainment = db.Column(db.Integer, default=0)  
    Clothing = db.Column(db.Integer, default=0)  
    Home = db.Column(db.Integer, default=0)  
    Private_Insurance = db.Column(db.Integer, default=0)  
    Memberships = db.Column(db.Integer, default=0)  
    Child_Support = db.Column(db.Integer, default=0)  
    Education_Cost = db.Column(db.Integer, default=0)  
    Employment_Type = db.Column(db.String(150), default="")
    Occupation =  db.Column(db.String(150), default="")
    Company_Name =  db.Column(db.String(150), default="")
    Service_Time =  db.Column(db.Integer, default=0)
    Credit_Score =  db.Column(db.Integer, default=0)