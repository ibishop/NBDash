import json
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from utils.mapbox import figure_factory,figure_data
from utils.dash import year_slider
from utils.cleaning import filter_year
from dash.dependencies import Input, Output

# Load CSS
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Load Data
all_data = pd.read_csv("temp.csv")
data = filter_year(all_data, 2001 )
fig = figure_factory(data,'graph_income')
fig.update_layout(clickmode='event+select')


# Define Application
app = dash.Dash(external_stylesheets=external_stylesheets)
app.layout = html.Div([
    html.H1("NB Well-Being Dashboard"),
    html.Div([

        html.Div([
            html.Div(),
            html.Div(dcc.Graph(id='map', figure=fig,config={'scrollZoom': True})),
            html.Div(year_slider(all_data.year))
        ], style={'height': 500, 'width': 700}),

        html.Div([
            html.Div(id='selected-data')
        ], style={'height': 500, 'width': 700})
    ],style={'columnCount': 2})
])

@app.callback(
    Output('map', 'figure'),
    [Input('year-slider', 'value')])
def update_figure(selected_year):

    data = filter_year(all_data,selected_year)
    fig.update(data=figure_data(data,topic="graph_income"))
    return fig

@app.callback(
    Output('selected-data', 'children'),
    [Input('map', 'selectedData')])
def select_point(points):
    return str(points)



app.run_server(debug=True, use_reloader=False)