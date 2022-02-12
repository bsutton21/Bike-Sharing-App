import pandas as pd
import matplotlib.pyplot as plt
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import data

bike_preds = data.bike.drop("Datetime", axis=1)

def predictions(user_data):
    x = bike_preds.drop("Rented Bike Count", axis=1)
    y = bike_preds["Rented Bike Count"]

    # Definte different features and transformer pipeline
    categorical_features = ["Date", "Seasons", "Holiday", "Functioning Day", "Precipitation"]
    one_hot = OneHotEncoder()
    transformer = ColumnTransformer([("one_hot",
                                    one_hot,
                                    categorical_features)],
                                    remainder="passthrough")
    transformed_x = transformer.fit_transform(x)
    transformed_x

    # Splitting into training and test data
    X_train, X_test, y_train, y_test = train_test_split(transformed_x, y, test_size=0.2)

    # Creating the model
    model = RandomForestRegressor()

    # Fitting with training data, then scoring with test data
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)

    user_data = pd.read_csv("UserBikeData.csv")
    user_data["humidity"] = int(user_data("humidity"))
    user_data["temp"] = int(user_data["temp"])
    user_data["precipitation"] = int(user_data["precipitation"])

    user_preds = model.predict(user_data)
    user_model = {"user_preds": user_preds.sum(), "score":score}

    return user_model