from flask import Blueprint, current_app, render_template, request, flash, redirect, url_for
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
        Other_Income = request.form.get('Other_Income')
        Pay_Interval_2 = request.form.get('Pay_Interval_2')
        Relationship_Status = request.form.get('Relationship Stauts')
        Dependants = request.form.get('Dependants')
        Housing_Situation = request.form.get('Housing Situation')
        Home_Loans = request.form.get('Home_Loans')
        Personal_Loans = request.form.get('Personal_Loans')
        Credit_Cards_Repayment = request.form.get('Credit_Cards_Repayment')
        Other_Liability = request.form.get('Other_Liability')
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
        Credit_Score = request.form.get('Credit Limit')

        user = User.query.filter_by(email=email).first() 
        # user = current_user   
        user.first_name = first_name 
        user.Last_name = Last_name
        user.Middle_name = Middle_name
        user.Mobile = Mobile 
        user.Address = Address
        user.income=income 
        user.Pay_Interval = Pay_Interval
        user.Other_Income = Other_Income 
        user.Pay_Interval_2 = Pay_Interval_2 
        user.Relationship_Status = Relationship_Status
        user.Dependants = Dependants
        user.Housing_Situation = Housing_Situation
        user.Home_Loans = Home_Loans
        user.Personal_Loans = Personal_Loans
        user.Credit_Cards_Repayment = Credit_Cards_Repayment
        user.Other_Liability = Other_Liability
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
        user.Credit_Score = Credit_Score
        db.session.commit()
        flash("Your profile has been updated!")

    return render_template("User_info.html", user=current_user)

@links.route('/success', methods=['POST'])  
def success():
    # current_app.config['UPLOAD_FOLDER']
    if request.method == 'POST': 
        f = request.files['file']
        if not os.path.isdir(current_app.config['UPLOAD_FOLDER']):
            os.mkdir(current_app.config['UPLOAD_FOLDER'])

        user_path = os.path.join(os.getcwd(), current_app.config['UPLOAD_FOLDER'], str(current_user.id))
        if not os.path.isdir(user_path):
            print("i'm in if not os.path.isdir")
            os.mkdir(user_path)

        f.save(f"{user_path}/{f.filename}")
        flash(f"\"{f.filename}\" successfully uploaded!")

    
    return redirect(url_for('documents.index'))

    

@links.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template("User_dashboard.html", user=current_user)

#get the total income per annum
def calc_incomePerAnnum(a):
    
    #translate pay interval to number
    def pi2num(pi):
        if pi == "Daily":
            x=260
        elif pi == "Weekly":
            x=52
        elif pi == "Monthly":
            x=12
        return x
    
    out = a["income"] * pi2num(a["Pay_Interval"]) + a["Other_Income"] * pi2num(a["Pay_Interval_2"]) 
    return out

#get the multipying factor for the total income per annum
def m_income(incomePerAnnum):
    m=0.2
    ipa= incomePerAnnum
    if ipa<30_000:
        m*=0
    elif ipa<50_000:
        m*=0.5
    elif ipa<70_000:
        m*=0.7
    elif ipa<100_000:
        m*=0.8
    elif ipa<150_000:
        m*=0.9
    else:
        m*=1
    return m

# get the multipying factor for (expense+liability)/income 
def m_DTI(a,ipa):
    # m stands for the multipying factor for DTI
    m=0.45
    ls_liabilities = [
        a["Home_Loans"],
        a["Personal_Loans"],
        a["Credit_Cards_Repayment"],
        a["Other_Liability"]
    ]
    liabilities = sum(ls_liabilities)
    ls_expenses = [
        a["Food"],
        a["Utilities"],
        a["Entertainment"],
        a["Clothing"],
        a["Home"],
        a["Private_Insurance"],
        a["Memberships"],
        a["Child_Support"],
        a["Education_Cost"],
    ]
    expenses = sum(ls_expenses)
    # m1 stands for the value of DTI
    m1 = (liabilities+expenses*12)/ipa
    if m1<0.3:
        m*=1
    elif m1<0.4:
        m*=0.8
    elif m1<0.5:
        m*=0.6
    elif m1<0.6:
        m*=0.3
    else:
        m=0
    return m

# get the multipying factor for Relationship and Housing 
def m_R_and_H(a):
    m=0 # m stands for the multipying factor for Relationship and Housing
    
    m1=0.05 # m1 stands for the multipying factor for Relationship Status
    if a["Relationship_Status"]=="Married" or a["Relationship_Status"]=="Defacto":
        m1*=0.8
        
    m2=0.1 # m2 stands for the multipying factor for number of dependants
    if a["Dependants"]>=6:
        m2=0
    elif a["Dependants"]>4:
        m2*=0.5
    elif a["Dependants"]>2:
        m2*=0.8
    
    m3=0.05 # m3 stands for the multipying factor for house status
    if a["Housing_Situation"]=="Mortgaged" or a["Housing_Situation"]=="Renting":
        m3*=0.8
        
    m=m1+m2+m3
    return m

# get the multipying factor for Employment
def m_employment(a):
    m=0 # m stands for the multipying factor for Employment
    
    m1=0.1 # m1 stands for the multipying factor for employment type 
    if a["Employment_Type"] == "Part Time":
        m1*=0.8
    elif a["Employment_Type"] == "Casual" or a["Employment_Type"] == "Self-employed":
        m1*=0.5
    elif a["Employment_Type"] == "Unemployed":
        m1*=0
    
    m2=0.05
    if a["Service_Time"] <=3:
        m2*=0
    m=m1+m2
    return m

def calc_Credit_Limit(a):
    
    m = 0 # the sum of the multiplying factors 
    # ipa stands for income per annum
    ipa = calc_incomePerAnnum(a)
    credit_limit =  ipa/2 # the upper limit of the applicant
    m+=m_income(ipa)
    m+=m_DTI(a,ipa)
    m+=m_R_and_H(a)
    m+=m_employment(a)
    return round(credit_limit*m/100)*100
    # if var1<30
    
    






@links.route('/apply', methods=['GET', 'POST'])
def apply():
    if request.method == 'POST':
        c=current_user
        # a stands for applicnat information dictionary 
        a = {
            "id":c.id,
            "first_name": c.first_name,
            "Last_name": c.Last_name,
            "Middle_name": c.Middle_name,
            "Mobile": c.Mobile ,
            "Address": c.Address,
            "income":c.income, 
            "Pay_Interval": c.Pay_Interval,
            "Other_Income": c.Other_Income ,
            "Pay_Interval_2": c.Pay_Interval_2 ,
            "Relationship_Status": c.Relationship_Status,
            "Dependants": c.Dependants,
            "Housing_Situation": c.Housing_Situation,
            "Home_Loans": c.Home_Loans,
            "Personal_Loans": c.Personal_Loans,
            "Credit_Cards_Repayment": c.Credit_Cards_Repayment,
            "Other_Liability": c.Other_Liability,
            "Food": c.Food,
            "Utilities": c.Utilities,
            "Entertainment": c.Entertainment,
            "Clothing": c.Clothing,
            "Home": c.Home,
            "Private_Insurance": c.Private_Insurance,
            "Memberships": c.Memberships,
            "Child_Support": c.Child_Support,
            "Education_Cost": c.Education_Cost,
            "Employment_Type": c.Employment_Type,
            "Occupation": c.Occupation,
            "Company_Name": c.Company_Name,
            "Service_Time": c.Service_Time,
            "Credit_Score": c.Credit_Score,
        }
        if request.form.get('action1') == 'Apply Low Fee Credit Card':
            flash('your application for product 1 is under review, we will contact you via email asap!', category='success')
            if c.Credit_Score <580:
                flash('you got disapproved for product 1', category="error")
            else:
                product="product1"
                Credit_Limit= calc_Credit_Limit(a)
                flash('you got approved for product 1, and your credit limit is: {}'.format(Credit_Limit), category="success")
            # if c.income>5:
            #     #send approval email
            #     flash('you got approved for product 1', category="success")
            # else:
            #     pass
            
            
            
            
        elif  request.form.get('action2') == 'Apply Rewards Credit Card':
            flash('your application for product 2 is under review, we will contact you via email asap!', category='success')
            if c.Credit_Score<670:
                flash('you got disapproved for product 2', category="error") 
            elif calc_incomePerAnnum(a) < 100_000:
                flash('you got disapproved for product 2', category="error") 
                    
            else:
                product="product2"
                Credit_Limit= calc_Credit_Limit(a)
                flash('you got approved for product 2, and your credit limit is: {}'.format(Credit_Limit), category="success")      
        # else:
            # pass # unknown
    # elif request.method == 'GET':

        # return render_template("apply.html", user=current_user)

    return render_template("apply.html", user=current_user)

