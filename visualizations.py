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
bike = pd.read_csv("data/BikeData.csv")

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

def bike_head():
    bike_head = bike.head(25)
    return bike_head.to_csv("data/bike_head.csv")