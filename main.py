from crypt import methods
from flask import Flask, render_template, redirect, url_for, request, session
import pandas as pd
import numpy as np
import datetime

app = Flask(__name__)
username = "admin"
password = "admin"

@app.route("/")
def index(): 
    return render_template("login.html") # loads the login page

@app.route("/predict", methods="POST", "GET")
def predict():
    if request.method == "POST":
        return ##### TO DO
    return


if __name__ == "__main__":
    app.run(debug=True) # tells it to start the app/server