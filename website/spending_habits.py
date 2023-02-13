from flask import Blueprint, Flask, render_template
from flask_login import current_user
from .models import User
import plotly.express as px
import pandas as pd
import json
import plotly

spending_habits = Blueprint('spending_habits', __name__)

@spending_habits.route('/spending_habits')
def chart():
    df = pd.DataFrame({
        'Food': [current_user.Food],
        'Utilities': [current_user.Utilities],
        'Entertainment': [current_user.Entertainment],
        'Clothing': [current_user.Clothing],
        'Home': [current_user.Home],
        'Private Insurance': [current_user.Private_Insurance],
        'Memberships': [current_user.Memberships],
        'Child Support': [current_user.Child_Support],
        'Education Costs': [current_user.Education_Cost]
    })
    if any([df.iloc[0][expense] for expense in df]):
        fig = px.pie(df, values=df.sum(), names=df.columns)
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        return render_template('spending_habits.html', user=current_user, graphJSON=graphJSON)
    else:
        return render_template('spending_habits.html', user=current_user, graphJSON=None)
