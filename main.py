from crypt import methods
from flask import Flask, render_template, redirect, url_for, request, session
import pandas as pd
import numpy as np
import datetime

app = Flask(__name__)
username = "admin"
password = "admin"

@app.route("/", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def index(): 
    return render_template("login.html") # loads the login page

@app.route("/main", methods=["GET", "POST"])
def login():
    if request.form["username"] == username and request.form["password"] == password:
        return render_template("main.html")
    else:
        return render_template("login.html")

@app.route("/main")
def main():
    return render_template("main.html") # loads the main page

@app.route("/predict", methods=["POST", "GET"])
def predict():
    if request.method == "POST":
        return render_template("machine_learning.html") # loads the machine learning page
    else:
        print("Invalid Request")

@app.route("/visualizations")
def visual():
    return render_template("visuzalizations.html") # loads the visualizations page

if __name__ == "__main__":
    app.run(debug=True) # tells it to start the app/server