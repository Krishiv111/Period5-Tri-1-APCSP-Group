import requests, json
# import "packages" from flask
from flask import render_template  # import render_template from "public" flask libraries
# import "packages" from "this" project
from __init__ import app  # Definitions initialization
from api import app_api # Blueprint import api definition
from bp_projects.projects import app_projects # Blueprint directory import projects definition

app.register_blueprint(app_api) # register api routes
app.register_blueprint(app_projects) # register api routes

@app.errorhandler(404)  # catch for URL not found
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route('/')  # connects default URL to index() function
def index():
    return render_template("index.html")

@app.route('/stub/')  # connects /stub/ URL to stub() function
def stub():
    return render_template("About-Us.html")


@app.route('/bmi/')  # connects /bmi/ URL to bmi() function
def bmi():
    return render_template("bmi.html")

@app.route('/calorie/')  # connects /stub/ URL to stub() function
def calorie():
    return render_template("calorie.html")

@app.route('/fitnessgoals/')  # connects /stub/ URL to stub() function
def fitnessgoals():
    return render_template("fitnessgoals.html")

@app.route('/motivation/')  # connects /stub/ URL to stub() function
def motivation():

    url = "https://quotes15.p.rapidapi.com/quotes/random/"

    headers = {
        "X-RapidAPI-Key": "825200d0f8msh414d353da41bfcfp1ddcfcjsnb40ef386fce9",
        "X-RapidAPI-Host": "quotes15.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    print(response.text)
    output = json.loads(response.text)
    return render_template("motivation.html", quotes = output)



# this runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
