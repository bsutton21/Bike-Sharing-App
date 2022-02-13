from statistics import mean
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import data

bike_preds = pd.read_csv("data/prediction_data.csv")

def predictor(attributes):
    x = bike_preds.drop(["Rented Bike Count"], axis=1)
    y = bike_preds["Rented Bike Count"]

    x.to_csv("data/X.csv", index=False)
    print("x: ", x.dtypes)
    """
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
"""
    # Splitting into training and test data
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2) # <--- change this back to transformed_X if I revert

    # Creating the model
    model = RandomForestRegressor()

    # Fitting with training data, then scoring with test data
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)

    user_data = pd.read_csv("data/UserBikeData.csv")
    print("UserBikeData: ", user_data.dtypes)
    user_data["Humidity (%)"] = int(attributes["humidity"])
    user_data["Temperature (C)"] = int(attributes["temperature"])
    user_data["Precipitation"] = int(attributes["precipitation"])

    user_data.to_csv("data/test.csv", index=False)

    user_preds = model.predict(user_data) # <--- change this back to transformed_user_data if I revert

    user_model = {"predicted_demand": user_preds.sum(), "score": score}

    return user_model
"""
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
"""
