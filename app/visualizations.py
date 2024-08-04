import data
import pandas as pd

# Calls the method to create the BikeDataVisualizations.csv file then initalizes bike_visual with that data
data.modify_data_visualizations
bike_visual = pd.read_csv("data/BikeDataVisualizations.csv")
# bike is initialized with "prediction_data.csv"
bike = pd.read_csv("data/prediction_data.csv")

######## TO DO: COMMENTS FOR ALL OF THESE ################################################################ 
def sales_graph():
    table = bike_visual
    table_date = table["Datetime"]
    table_count = table["Rented Bike Count"]
    sales_vis = {"date": table_date, "count": table_count}
    return sales_vis

def temp_graph():
    table = bike_visual
    table_temp = table["Temperature (C)"]
    table_count = table["Rented Bike Count"]
    sales_vis = {"temperature": table_temp, "count": table_count}
    return sales_vis

def precip_graph():
    table = bike_visual
    table_precip = table["Precipitation"]
    table_count = table["Rented Bike Count"]
    table_date = table["Date"]
    sales_vis = {"precipitation": table_precip, "count": table_count, "date": table_date}
    return sales_vis

def humid_graph():
    table = bike_visual
    table_humid = table["Humidity (%)"]
    table_count = table["Rented Bike Count"]
    sales_vis = {"humidity": table_humid, "count": table_count}
    return sales_vis

def bike_head():
    bike_head = bike.head(30)
    table_rows = bike_head
    table = {"columns": bike.columns, "rows": table_rows}
    return table