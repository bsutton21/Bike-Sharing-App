import pandas as pd
import numpy as np
import datetime

# initializing bike by reading in the BikeData.csv

def modify_data_visualizations():
    """

    Very little cleaning was required on this data.  I used Jupyter Notebook to verify that
    it contained no missing data in any column and that there were no extreme outliers that
    could skew the results.  These are the steps that I follow in this function:

    1) Reformat the "Date" column dd/mm/yyyy to standard data format
    2) Create pandas dataframe with dictionary of Day:Hour then combine the key/value pairs into a single, new "Datetime" column
    3) Created new "Precipitation" boolean column where "True" if rainfall or snowfall are >0
    4) Dropped "Rainfall (mm)", "Snowfall (cm)", "Wind speed (m/s)", "Visibility (10m)", 
       "Dew point temperature (C)", "Solar Radiation (MJ/m2)" since we aren't using those
       datapoints for our predictions.

    """
    bike = pd.read_csv("data/BikeData.csv")

    # Reformatting the data in the "Date" column from dd/mm/yyyy to standard date format
    for i in range(0, len(bike["Date"])):
        bike["Date"][i] = datetime.datetime.strptime(bike["Date"][i], "%d/%m/%Y").date()
    
    # Creating pd dataframe with dictionary of Day: Hour
    dt_df = pd.DataFrame({
        'Day': np.array(bike["Date"]), 
        'Hour': np.array(bike["Hour"])})

    # Combining the "Date" and "Hour" data from each row into one cell in the "Datetime" column
    bike["Datetime"] = pd.to_datetime(dt_df.Day) + pd.to_timedelta(dt_df.Hour, unit='h')

    # Adding Precipitation boolean column - "True" if either "Rainfall (mm)" or "Snowfall (cm)" are greater than 0
    bike["Precipitation"] = np.where((bike['Rainfall (mm)'] > 0) | (bike['Snowfall (cm)'] > 0), 1, 0)

    bike = bike.drop(["Rainfall (mm)", "Snowfall (cm)", "Wind speed (m/s)", "Visibility (10m)", "Dew point temperature (C)", "Solar Radiation (MJ/m2)"], axis=1)
    # Return bike with new "Datetime" and "Precipitation" columns
    return bike.to_csv("data/BikeDataVisualizations.csv", index=False)

def modify_data_predictions():
    return