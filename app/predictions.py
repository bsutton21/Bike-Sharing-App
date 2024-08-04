from statistics import mean
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Initializes bike_preds with the prediction_data.csv data
bike_preds = pd.read_csv("data/prediction_data.csv")

# This implements the machine learning RandomForestRegressor algorithm for the prediction model
def predictor(attributes):
    x = bike_preds.drop(["Rented Bike Count"], axis=1)
    y = bike_preds["Rented Bike Count"]

    # Splitting into training and test data
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

    # Creating the model
    model = RandomForestRegressor()

    # Fitting with training data, then scoring with test data
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)

    # Takes the user-entered data and runs it through the model
    user_data = pd.read_csv("data/UserBikeData.csv")
    user_data["Humidity (%)"] = int(attributes["humidity"])
    user_data["Temperature (C)"] = int(attributes["temperature"])
    user_data["Precipitation"] = int(attributes["precipitation"])
    # Makes prediction with the user data
    user_preds = model.predict(user_data)
    # Creates "user_model" object to pass to the html for display on the page
    user_model = {"predicted_demand": user_preds.sum(), "score": score}

    return user_model
