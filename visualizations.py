import data
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import dash

# setting plt figure style
plt.style.use('ggplot');

data.modify_data_visualizations
bike_visual = pd.read_csv("data/BikeDataVisualizations.csv")
bike = pd.read_csv("data/prediction_data.csv")

# Creates a bar graph to visualize sales over time
def sales_over_time():
    # Object-oriented method
    fig, ax = plt.subplots(figsize=(20,9));

    # Plot the data
    bar = ax.bar(bike_visual["Datetime"],
                 bike_visual["Rented Bike Count"],
                 color="maroon");

    # Customize the plot
    ax.set(title='Sales Over Time',
        xlabel="Date",
        ylabel="Number of Sales");

    # Add a horizontal line
    ax.axhline(bike_visual["Rented Bike Count"].mean(),
               label="Mean",
               color="black",
               linestyle="--");
    return fig.savefig("images/sales_over_time.png")

# Scatter plot showing relationship between bike rentals and temperature
def temper_scatter():
    # Setting subplots and initializing the figure size
    fig, ax = plt.subplots(figsize=(20,8))

    # Plot the data
    scatter = ax.scatter(x=bike_visual["Temperature (C)"],
                         y=bike_visual["Rented Bike Count"],
                         c=bike_visual["Rented Bike Count"],
                         cmap='plasma');

    # Customize the plot
    ax.set(title='Relationship between Bike Rental and Temperature',
        xlabel="Temperature (C)",
        ylabel="Rented Bike Count");

    # Add a legend
    ax.legend(*scatter.legend_elements(), title="Rentals");

    # Add a horizontal line
    ax.axhline(bike_visual["Rented Bike Count"].mean(),
               label="Mean",
               linestyle="--");
    return fig.savefig("images/sales_and_temp.png")

# Scatter plot showing relationship between bike rentals and precipitation
def precip_scatter():
    # Setting subplots and initializing the figure size
    fig, ax = plt.subplots(figsize=(20,8))

    # Plot the data
    scatter = ax.scatter(x=bike_visual["Datetime"],
                         y=bike_visual["Rented Bike Count"],
                         c=bike_visual["Precipitation"],
                         cmap='coolwarm_r');

    # Customize the plot
    ax.set(title='Relationship between Bike Rental and Precipitation',
           xlabel="Date",
           ylabel="Rented Bike Count");

    # Add a legend
    ax.legend(*scatter.legend_elements(), title="Precipitation - 1=True");

    # Add a horizontal line
    ax.axhline(bike_visual["Rented Bike Count"].mean(),
               label="Mean",
               color="black",
               linestyle="--");
    return fig.savefig("images/sales_and_precip.png")

# Scatter plot showing relationship between bike rentals and precipitation
def humid_scatter():
    # Setting subplots and initializing the figure size
    fig, ax = plt.subplots(figsize=(20,8))

    ## Plot the data
    scatter = ax.scatter(x=bike_visual["Humidity (%)"],
                         y=bike_visual["Rented Bike Count"],
                         c=bike_visual["Rented Bike Count"],
                         cmap="plasma");

    # Customize the plot
    ax.set(title='Relationship between Bike Rental and Humidity',
        xlabel="Humidity (%)",
        ylabel="Rented Bike Count");

    # Add a legend
    ax.legend(*scatter.legend_elements(), title="Rentals");

    # Add a horizontal line
    ax.axhline(bike_visual["Rented Bike Count"].mean(),
               label="Mean",
               linestyle="--");
    return fig.savefig("images/sales_and_humid.png")

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