from flask import Flask, render_template
import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, GridSearchCV
import datetime

app = Flask(__name__)

@app.route("/")
def profile(): 
    return render_template("main.html") # don't put html in the return statement


if __name__ == "__main__":
    app.run(debug=True) # tells it to start the server