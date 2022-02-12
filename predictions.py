from statistics import mean
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import data

data.modify_data()
bike_preds = pd.read_csv("data/BikeDataExpanded.csv")

def predictor(attributes):
    x = bike_preds.drop(["Rented Bike Count", "Datetime"], axis=1)
    y = bike_preds["Rented Bike Count"]

    x.to_csv("data/X.csv", index=False)

    # Define different features and transformer pipeline
    categorical_features = ["Date", "Seasons", "Holiday", "Functioning Day"]
    one_hot = OneHotEncoder()
    transformer = ColumnTransformer([("one_hot",
                                      one_hot,
                                      categorical_features)],
                                      remainder="passthrough")
    transformed_X = transformer.fit_transform(x)

    df=pd.DataFrame(transformed_X)
    df.to_csv("data/TransformedX.csv", index=False)

    # Splitting into training and test data
    X_train, X_test, y_train, y_test = train_test_split(transformed_X, y, test_size=0.2)

    # Creating the model
    model = RandomForestRegressor()

    # Fitting with training data, then scoring with test data
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)

    user_data = pd.read_csv("data/UserBikeData.csv")

    user_data["Humidity (%)"] = int(attributes["humidity"])
    user_data["Temperature (C)"] = int(attributes["temperature"])
    user_data["Precipitation"] = int(attributes["precipitation"])

    user_data.to_csv("data/test.csv", index=False)

    # Define different features and transformer pipeline
    categorical_features = ["Date", "Seasons", "Holiday", "Functioning Day"]
    one_hot = OneHotEncoder()
    transformer = ColumnTransformer([("one_hot",
                                      one_hot,
                                      categorical_features)],
                                      remainder="passthrough")
    transformed_user_data = transformer.fit_transform(user_data)

    df=pd.DataFrame(transformed_user_data)
    df.to_csv("data/UserPreds.csv", index=False)

    transformed_user_data = pd.DataFrame(transformed_user_data).dropna()

    df=pd.DataFrame(transformed_user_data)
    df.to_csv("data/AfterDropNa.csv", index=False)
    user_preds = model.predict(transformed_user_data)

    user_model = {"user_preds": user_preds.sum(), "score": score}

    return user_model