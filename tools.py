#This python file consists functions that help with developing and testing.
import os
def refresh():
    if os.path.exists("website/database.db"):
        os.remove("website/database.db")
    else:
        print("The file doesn't exist")
    from website import create_app
    app = create_app()
    # os.chdir("./website")

    # print(os.getcwd())

    # from website.models import User
    # from website import db
    # from flask_login import login_user, login_required, logout_user, current_user
    # from werkzeug.security import generate_password_hash, check_password_hash

    # new_user = User(
    #     email="1@gmail.com", 
    #     first_name="person1", 
    #     password=generate_password_hash(
    #     "password", 
    #     method='sha256'),#, income =-1)
    # )
    # db.session.add(new_user)
    # db.session.commit()
    # login_user(new_user, remember=True)    

    # from .models import User
    # os.chdir("..")