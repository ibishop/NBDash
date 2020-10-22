import json
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from utils.mapbox import figure_factory
from dash.dependencies import Input, Output

# Load CSS
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Load Data
data = pd.read_csv("temp.csv")
fig = figure_factory(data,'graph_income')

# Define Application
app = dash.Dash(external_stylesheets=external_stylesheets)
app.layout = html.Div([
    html.H1("NB Well Being Dashboard"),
    html.Div(
        dcc.Graph(id='map',figure=fig)
    )
])
app.run_server(debug=True, use_reloader=False)