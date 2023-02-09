from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

import os


links = Blueprint('links', __name__)

@links.route('/user-dashboard', methods=['GET', 'POST'])
def user_dashboard():
    return render_template("User_dashboard.html", user=current_user)

@links.route('/user-info', methods=['GET', 'POST'])
def user_info():

    if request.method == 'POST':
        
        email = request.form.get('email')
        first_name = request.form.get('fname')
        Last_name = request.form.get('lname')
        Middle_name = request.form.get('mname')
        Mobile = request.form.get('mobile')
        Address = request.form.get('Address')
        income = request.form.get('income')
        Pay_Interval = request.form.get('Pay Interval')
        Relationship_Status = request.form.get('Relationship Stauts')
        Dependants = request.form.get('Dependants')
        Housing_Situation = request.form.get('Housing Situation')
        # Liabilities = request.form.get('income')
        Food = request.form.get('Food')
        Utilities = request.form.get('Utilities')
        Entertainment = request.form.get('Entertainment')
        Clothing = request.form.get('Clothing')
        Home = request.form.get('Home')
        Private_Insurance = request.form.get('Private Insurance')
        Memberships = request.form.get('Memberships')
        Child_Support = request.form.get('Child Support')
        Education_Cost = request.form.get('Education Cost')
        Employment_Type = request.form.get('Employment Type')
        Occupation = request.form.get('Occupation')
        Company_Name = request.form.get('Company Name')
        Service_Time = request.form.get('Service Time')
        Credit_Limit = request.form.get('Credit Limit')

        user = User.query.filter_by(email=email).first() 
        # user = current_user   
        user.first_name = first_name 
        user.Last_name = Last_name
        user.Middle_name = Middle_name
        user.Mobile = Mobile 
        user.Address = Address
        user.income=income 
        user.Pay_Interval = Pay_Interval
        user.Relationship_Status = Relationship_Status
        user.Dependants = Dependants
        user.Housing_Situation = Housing_Situation
        user.Food = Food
        user.Utilities = Utilities
        user.Entertainment = Entertainment
        user.Clothing = Clothing
        user.Home = Home
        user.Private_Insurance = Private_Insurance
        user.Memberships = Memberships
        user.Child_Support = Child_Support
        user.Education_Cost = Education_Cost
        user.Employment_Type = Employment_Type
        user.Occupation = Occupation
        user.Company_Name = Company_Name
        user.Service_Time = Service_Time
        user.Credit_Limit = Credit_Limit
        db.session.commit()
    
    
    return render_template("User_info.html", user=current_user)

@links.route('/success', methods=['POST'])  
def success():  
    if request.method == 'POST': 
        f = request.files['file']
        upload_dir = './user_uploads/'
        if not os.path.isdir(upload_dir):
            print("i'm in create upload dir")
            os.mkdir(upload_dir)
        user_path = os.path.join(upload_dir, str(current_user.id))
        if not os.path.isdir(user_path):
            print("i'm in if not os.path.isdir")
            os.mkdir(user_path)

        f.save(f"{user_path}/{f.filename}")

@links.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template("User_dashboard.html", user=current_user)

@links.route('/apply', methods=['GET', 'POST'])
def apply():
    if request.method == 'POST':
        if request.form.get('action1') == 'apply product 1':
            flash('your application for product 1 is under review, we will contact you via email asap!', category='success')
            if current_user.income>5:
                #send approval email
                flash('you got approved for product 1', category="success")
            else:
                flash('you got disapproved for product 1', category="error")
            
            
            
            
            
        elif  request.form.get('action2') == 'apply product 2':
            flash('your application for product 2 is under review, we will contact you via email asap!', category='success')
            if current_user.income>10:
                #send approval email
                flash('you got approved for product 2', category="success")
            else:
                flash('you got disapproved for product 2', category="error")       
        # else:
            # pass # unknown
    # elif request.method == 'GET':

        # return render_template("apply.html", user=current_user)

    return render_template("apply.html", user=current_user)

@links.route('/spending_habits', methods=['GET', 'POST'])
def spending_habits():
    return render_template("spending_habits.html", user=current_user)
    
@links.route('/documents', methods=['GET', 'POST'])
def documents():
    return render_template("documents.html", user=current_user)