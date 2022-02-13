from crypt import methods
from flask import Flask, render_template, redirect, url_for, request, session
import pandas as pd
import numpy as np
import datetime
from predictions import predictor
import data

app = Flask(__name__)
username = "admin"
password = "admin"

@app.route("/", methods=["GET"])
@app.route("/login", methods=["GET"])
def index(): 
    return render_template("login.html") # loads the login page

@app.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        if username == request.form['username'] and password == request.form['password']:
            return redirect("/main", code=307)
        else:
            return render_template("login.html")

@app.route("/main", methods=["GET", "POST"])
def main():
    return render_template("main.html") # loads the main page

@app.route("/predict", methods=["POST", "GET"])
def predict():
    if request.method == "POST":
        precip = request.values["precipitation"][0:1]
        temp = request.values["temperature"]
        humid = int(request.values["humidity"])
        predict_data = {"temperature": temp, "humidity": humid, "precipitation": precip}
        predict_model = predictor(predict_data)
        pred_demand = int(round(predict_model["predicted_demand"]))
        score = round(predict_model["score"], 3) * 100

        return render_template("predictions.html", pred_demand=pred_demand, score=score) # loads the machine learning page
    else:
        print("Invalid Request")

@app.route("/visualizations", methods=["GET", "POST"])
def visual():
    return render_template("visualizations.html") # loads the visualizations page

if __name__ == "__main__":
    app.run(debug=True) # tells it to start the app/server