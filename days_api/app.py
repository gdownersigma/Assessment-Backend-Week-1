"""This file defines the API routes."""

# pylint: disable = no-name-in-module

from datetime import datetime, date

from flask import Flask, Response, request, jsonify

from date_functions import (convert_to_datetime, get_day_of_week_on,
                            get_days_between, get_current_age)

app_history = []

app = Flask(__name__)


def add_to_history(current_request):
    """Adds a route to the app history."""
    app_history.append({
        "method": current_request.method,
        "at": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "route": current_request.endpoint
    })

def clear_history():
    """Clears the app history."""
    app_history.clear()


@app.get("/")
def index():
    """Returns an API welcome messsage."""
    return jsonify({"message": "Welcome to the Days API."})


@app.route("/between",methods = ['POST'])
def days_between():
    """Return the days between two dates."""
    dates = request.json
    if 'first' not in dates or 'last' not in dates:
        return {
            'error': 'Missing required data.'
        }, 400
    try:
        first_date = convert_to_datetime(dates['first'])
        last_date = convert_to_datetime(dates['last'])
        add_to_history(request)
        return {
            'days': (get_days_between(first_date,last_date))
            }, 200
    except ValueError:
        return {
            'error': 'Unable to convert value to datetime.'
        }, 400
        
@app.route("/weekday",methods = ['POST'])
def get_weekday():
    """Return the weekday from a given date."""
    resp = request.json
    if 'date' not in resp:
        return {
            'error': 'Missing required data.'
        }, 400
    
    try:
        given_date = convert_to_datetime(resp['date'])
        day = get_day_of_week_on(given_date)
        add_to_history(request)
        return {
            'weekday': day
        }, 200
    except ValueError:
        return {
            'error': 'Unable to convert value to datetime.'
        }, 400



if __name__ == "__main__":
    app.config['TESTING'] = True
    app.config['DEBUG'] = True
    app.run(port=8080, debug=True)
