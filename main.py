from genericpath import exists
from flask import Flask, render_template, redirect, url_for, request, session
import pandas as pd
import numpy as np
import datetime
from predictions import predictor
import data
from visualizations import humid_graph, humid_scatter, precip_graph, precip_scatter, sales_graph, sales_over_time, temp_graph, temper_scatter, bike_head
from dash import Dash, dcc, html, dash_table
import dash_bootstrap_components as dbc
import plotly.graph_objects as go

server = Flask(__name__)
username = "admin"
password = "admin"

##### CREATING THE TABLE #####

table_data = bike_head()
# Creating columns for the bike head table
columns = table_data["columns"]
columns_for_table = []
for column in columns:
    columns_for_table.append(html.Th(column))

# Creating rows for the bike head table
rows = table_data["rows"]
rows_for_table = []
for column in columns:
    rows_for_table.append(html.Th(column))

# Organizing the columns in the table
table_header = [
    html.Thead(html.Tr([
        html.Th("Rented Bike Count"),
        html.Th("Hour"),
        html.Th("Temperature (C)"),
        html.Th("Humidity (%)"),
        html.Th("Seasons"),
        html.Th("Holiday"),
        html.Th("Functioning Day"),
        html.Th("Precipitation"),
        html.Th("Day"),
        html.Th("Month"),
        html.Th("Year")]))

    ]

for index, row in rows.iterrows():
    rows_for_table.append(html.Tr(
        [html.Td(row["Rented Bike Count"]),
         html.Td(row["Hour"]),
         html.Td(row["Temperature (C)"]),
         html.Td(row["Humidity (%)"]),
         html.Td(row["Seasons"]),
         html.Td(row["Holiday"]),
         html.Td(row["Functioning Day"]),
         html.Td(row["Precipitation"]),
         html.Td(row["Day"]),
         html.Td(row["Month"]),
         html.Td(row["Year"])
        ]))

# Organizing the rows in the table
table_body = [html.Tbody(
    rows_for_table
)]

# Initializing the sales over time graph data
sales_by_date_vis = sales_graph()
gofig = go.Figure()
sales_by_date = gofig.add_trace(go.Scatter(x=sales_by_date_vis["date"],
                                           y=sales_by_date_vis["count"]))

# Initializing the sales/temperature graph data
temp_vis = temp_graph()

# Initializing the sales/precipitation graph data
precip_vis = precip_graph()

# Initializing the sales/humidity graph data
humid_vis = humid_graph()

# Setting the navbar for the visualizations page
nav = dbc.NavbarSimple(
    children=[html.Form(dbc.NavItem(html.Button(dbc.NavLink("Back"))), action="/main", method="POST"),
              ],
    brand=" Bike Demand Prediction - Data Visualization & Table",
    brand_href="#",
    sticky="top",
    color='darkgrey',
)

##### CREATING A TABLE WITH 30 ROWS OF DATA #####
tab_head = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("First 30 Lines of the Raw Bike Data", style={"color": "indianred"}),
                        dbc.Table(table_body,
                                  bordered=True,
                                  dark=False,
                                  hover=True,
                                  responsive=True,
                                  striped=True,
                                  )
                    ]
                )
            ]
        ), html.Hr()
    ],
    className="mt-4",
)

##### CREATING THE SALES OVER TIME GRAPH #####
sales_time_vis = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Sales Over Time", style={"color": "indianred"}),
                        dcc.Graph(
                            figure=sales_by_date
                        )
                    ]
                ),
            ]
        ), html.Hr()
    ],
    className="mt-4",
)

##### CREATING THE BIKE RENTALS AND TEMPERATURE GRAPH #####
temp_vis = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Relationship between Bike Rentals and Temperature", style={"color": "indianred"}),
                        dcc.Graph(
                            id='temperature_vs_count',
                            figure={
                                'data': [
                                    dict(
                                        x=temp_vis["temperature"],
                                        y=temp_vis["count"],
                                        mode="markers",
                                        opacity=0.7,
                                        marker={
                                            'size': 8,
                                            'line': {'width': 0.5, 'color': 'white'},
                                            'color': temp_vis["temperature"]
                                        }
                                    )
                                ],
                                'layout': dict(
                                    xaxis={'title': 'Temperature'},
                                    yaxis={'title': 'Number of Bike Rentals'},
                                    margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                                    legend={'x': 0, 'y': 1},
                                    hovermode='closest'
                                )
                            }
                        ),
                    ]
                ),
            ]
        ), html.Hr()
    ],
    className="mt-4",
)
##### CREATING THE BIKE RENTALS AND PRECIPITATION GRAPH #####
precip_vis = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Relationship between Bike Rentals and Precipitation", style={"color": "indianred"}),
                        dcc.Graph(
                            id='precipitation_vs_count',
                            figure={
                                'data': [
                                    dict(
                                        x=precip_vis["date"],
                                        y=precip_vis["count"],
                                        mode="markers",
                                        opacity=0.7,
                                        marker={
                                            'size': 8,
                                            'line': {'width': 0.5, 'color': 'red'},
                                            'color': precip_vis["precipitation"]
                                        }
                                    )
                                ],
                                'layout': dict(
                                    xaxis={'title': 'Date'},
                                    yaxis={'title': 'Number of Bike Rentals'},
                                    color=precip_vis["precipitation"],
                                    margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                                    legend={'x': 0, 'y': 1},
                                    hovermode='closest'
                                )
                            }
                        ),
                    ]
                ),
            ]
        ), html.Hr()
    ],
    className="mt-4",
)
##### CREATING THE BIKE RENTALS AND HUMIDITY GRAPH #####
humid_vis = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Relationship between Bike Rentals and Humidity", style={"color": "indianred"}),
                        dcc.Graph(
                            id='humidity_vs_count',
                            figure={
                                'data': [
                                    dict(
                                        x=humid_vis["humidity"],
                                        y=humid_vis["count"],
                                        mode="markers",
                                        opacity=0.7,
                                        marker={
                                            'size': 8,
                                            'line': {'width': 0.5, 'color': 'white'},
                                            'color': humid_vis["humidity"]
                                        }
                                    )
                                ],
                                'layout': dict(
                                    xaxis={'title': 'Temperature'},
                                    yaxis={'title': 'Number of Bike Rentals'},
                                    margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                                    legend={'x': 0, 'y': 1},
                                    hovermode='closest'
                                )
                            }
                        ),
                    ]
                ),
            ]
        ), html.Hr()
    ],
    className="mt-4",
)
# Initializing the dash app
app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    server=server,
    routes_pathname_prefix='/visual/'
)
app.title = "Historical Bike Demand Visualizations"
app.layout = html.Div([nav, sales_time_vis, temp_vis, precip_vis, humid_vis, tab_head],
                      className = "container")

@server.route("/", methods=["GET"])
@server.route("/login", methods=["GET"])
def index(): 
    return render_template("login.html") # loads the login page

@server.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        if username == request.form['username'] and password == request.form['password']:
            return redirect("/main", code=307)
        else:
            return render_template("login.html")

@server.route("/main", methods=["GET", "POST"])
def main():
    return render_template("main.html") # loads the main page

@server.route("/predict", methods=["POST", "GET"])
def predict():
    if request.method == "POST":
        precip = request.values["precipitation"][0:1]
        temp = request.values["temperature"]
        humid = int(request.values["humidity"])
        predict_data = {"temperature": temp, "humidity": humid, "precipitation": precip}
        predict_model = predictor(predict_data)
        pred_demand = int(round(predict_model["predicted_demand"]))
        score = round(predict_model["score"], 3) * 100

        return render_template("predictions.html", pred_demand=pred_demand, score=score) # loads the machine learning page
    else:
        print("Invalid Request")

@server.route("/visualizations", methods=["GET", "POST"])
def visualizations():
    if not exists("images/sales_over_time.png"):
        sales_over_time()
    if not exists("images/sales_and_temp.png"):
        temper_scatter()
    if not exists("images/sales_and_precip.png"):
        precip_scatter()
    if not exists("images/sales_and_humid.png"):
        humid_scatter()
    visualizations.bike_head()
    bike_head = pd.read_csv("data/bike_head.csv")
    return render_template("visualizations.html", bike_head=bike_head.to_html()) # loads the visualizations page

if __name__ == "__main__":
    server.run(debug=True) # tells it to start the app/server