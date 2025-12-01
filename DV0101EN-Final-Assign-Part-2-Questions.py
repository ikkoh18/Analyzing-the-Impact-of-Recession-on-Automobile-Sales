#!/usr/bin/env python
# coding: utf-8

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# ------------------------------------------------------------
# Load data
data = pd.read_csv(
    "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv"
)

# ------------------------------------------------------------
# Init app
app = dash.Dash(__name__)
server = app.server  # (opcional p/ deploy)

# ------------------------------------------------------------
# Dropdown config
dropdown_options = [
    {"label": "Yearly Statistics", "value": "Yearly Statistics"},
    {"label": "Recession Period Statistics", "value": "Recession Period Statistics"},
]
year_list = sorted(data["Year"].unique().tolist())

# ------------------------------------------------------------
# Layout
app.layout = html.Div(
    [
        html.H1(
            "Automobile Sales Statistics Dashboard",
            style={"textAlign": "center", "marginBottom": "12px"},
        ),

        # Report type
        html.Div(
            [
                html.Label("Select Statistics:"),
                dcc.Dropdown(
                    id="dropdown-statistics",
                    options=dropdown_options,
                    value="Yearly Statistics",
                    placeholder="Select a report type",
                    clearable=False,
                ),
            ],
            style={"maxWidth": 500, "margin": "0 auto 12px"},
        ),

        # Year selector
        html.Div(
            [
                html.Label("Select Year:"),
                dcc.Dropdown(
                    id="select-year",
                    options=[{"label": int(y), "value": int(y)} for y in year_list],
                    value=year_list[0],
                    clearable=False,
                ),
            ],
            style={"maxWidth": 500, "margin": "0 auto 24px"},
        ),

        # Output grid
        html.Div(
            id="output-container",
            className="chart-grid",
            style={
                "display": "grid",
                "gridTemplateColumns": "repeat(2, minmax(300px, 1fr))",
                "gap": "16px",
                "padding": "0 16px 24px",
            },
        ),
    ]
)

# ------------------------------------------------------------
# Enable/disable year dropdown
@app.callback(
    Output("select-year", "disabled"),
    Input("dropdown-statistics", "value"),
)
def update_input_container(selected_statistics):
    return selected_statistics != "Yearly Statistics"


# ------------------------------------------------------------
# Main plotting callback
@app.callback(
    Output("output-container", "children"),
    Input("dropdown-statistics", "value"),
    Input("select-year", "value"),
)
def update_output_container(selected_statistics, input_year):
    children = []

    if selected_statistics == "Recession Period Statistics":
        recession_data = data[data["Recession"] == 1].copy()

        # Plot 1: Average automobile sales over recession years
        yearly_rec = (
            recession_data.groupby("Year", as_index=False)["Automobile_Sales"]
            .mean()
        )
        R_chart1 = dcc.Graph(
            figure=px.line(
                yearly_rec,
                x="Year",
                y="Automobile_Sales",
                title="Average Automobile Sales over Recession Years",
            )
        )

        # Plot 2: Average vehicles sold by vehicle type (recessions)
        average_sales = (
            recession_data.groupby("Vehicle_Type", as_index=False)["Automobile_Sales"]
            .mean()
        )
        R_chart2 = dcc.Graph(
            figure=px.bar(
                average_sales,
                x="Vehicle_Type",
                y="Automobile_Sales",
                title="Average Vehicles Sold by Vehicle Type (Recessions)",
            )
        )

        # Plot 3: Advertisement expenditure share by vehicle type (recessions)
        exp_rec = (
            recession_data.groupby("Vehicle_Type", as_index=False)[
                "Advertising_Expenditure"
            ]
            .sum()
        )
        R_chart3 = dcc.Graph(
            figure=px.pie(
                exp_rec,
                names="Vehicle_Type",
                values="Advertising_Expenditure",
                title="Advertisement Expenditure Share by Vehicle Type (Recessions)",
            )
        )

        # Plot 4: Effect of unemployment rate on vehicle type and sales (recessions)
        unemp_data = (
            recession_data.groupby(["unemployment_rate", "Vehicle_Type"], as_index=False)[
                "Automobile_Sales"
            ]
            .mean()
        )
        R_chart4 = dcc.Graph(
            figure=px.bar(
                unemp_data,
                x="unemployment_rate",
                y="Automobile_Sales",
                color="Vehicle_Type",
                labels={
                    "unemployment_rate": "Unemployment Rate",
                    "Automobile_Sales": "Average Automobile Sales",
                },
                title="Effect of Unemployment Rate on Vehicle Type and Sales (Recessions)",
            )
        )

        children = [R_chart1, R_chart2, R_chart3, R_chart4]

    elif selected_statistics == "Yearly Statistics" and input_year is not None:
        yearly_data = data[data["Year"] == int(input_year)].copy()

        # Plot 1: Yearly Automobile sales (whole period, avg per year)
        yas = data.groupby("Year", as_index=False)["Automobile_Sales"].mean()
        Y_chart1 = dcc.Graph(
            figure=px.line(
                yas, x="Year", y="Automobile_Sales", title="Yearly Automobile Sales (Average per Year)"
            )
        )

        # Plot 2: Total Monthly Automobile sales (whole period)
        mas = data.groupby("Month", as_index=False)["Automobile_Sales"].sum()
        Y_chart2 = dcc.Graph(
            figure=px.line(
                mas, x="Month", y="Automobile_Sales", title="Total Monthly Automobile Sales (All Years)"
            )
        )

        # Plot 3: Average vehicles sold by vehicle type (selected year)
        avr_vdata = (
            yearly_data.groupby("Vehicle_Type", as_index=False)["Automobile_Sales"]
            .mean()
        )
        Y_chart3 = dcc.Graph(
            figure=px.bar(
                avr_vdata,
                x="Vehicle_Type",
                y="Automobile_Sales",
                title=f"Average Vehicles Sold by Vehicle Type in {input_year}",
            )
        )

        # Plot 4: Total Advertisement Expenditure by vehicle type (selected year)
        exp_data = (
            yearly_data.groupby("Vehicle_Type", as_index=False)[
                "Advertising_Expenditure"
            ]
            .sum()
        )
        Y_chart4 = dcc.Graph(
            figure=px.pie(
                exp_data,
                names="Vehicle_Type",
                values="Advertising_Expenditure",
                title=f"Advertisement Expenditure by Vehicle Type in {input_year}",
            )
        )

        children = [Y_chart1, Y_chart2, Y_chart3, Y_chart4]

    return children


# ------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8050)

