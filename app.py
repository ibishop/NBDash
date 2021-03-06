import json
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from utils.mapbox import figure_factory
from utils.dash import year_slider, buttons, build_table,table_update, geography_searchbar,sort_menu
from utils.cleaning import filter_year
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate

# Load CSS
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Load Data
all_data = pd.read_csv("temp.csv")
data = filter_year(all_data, 2001 )
fig = figure_factory(data,'graph_income')
fig.update_layout(uirevision='same')

# Define Application
app = dash.Dash(external_stylesheets=external_stylesheets)
app.layout = html.Div([
    html.H1("NB Well-Being Dashboard"),
    html.Div([

        html.Div([
            html.Div(buttons( [ x for x in data.columns[3:] if "graph" in x]),id='buttons'),
            html.Div(dcc.Graph(id='map', figure=fig,config={'scrollZoom': True})),
            html.Div(year_slider(all_data.year))
        ], style={'height': 700, 'paddingRight': '0.5cm'}),

        html.Div([
            html.Div(geography_searchbar(data['Geography']), id='geo-bar'),
            html.Div(sort_menu(), id='sort-radial', style={'paddingTop': '0.1cm'}),
            html.Div(build_table(),id='selected-data', style={'height': 400 , 'width': 400})
        ], style={'height': 700, 'width': 700, 'rowCount':3})

    ],style={'columnCount': 2}),
])

@app.callback(
    Output('map', 'figure'),
    [Input('year-slider', 'value'),
     Input('selected-column','value'),
     Input('map','selectedData')])
def update_figure(selected_year,column,selection):

    data = filter_year(all_data, selected_year)
    fig = figure_factory(data,column)

    print("PRE")
    if selection:

        indicies = [ x['customdata'][0] for x in selection['points']]
        temp = data.reset_index().CSDUID.isin(indicies)
        temp = temp[temp].index
        fig.update_traces(selectedpoints=temp)

    return fig

@app.callback(
    [Output('table', 'columns'),
     Output('table', 'data')],
    [Input('map', 'selectedData'),
     Input('selected-column','value'),
     Input('sort','value')])
def display_selection(selection,column,ascending):
    if not selection:
        raise PreventUpdate

    indicies =  [ x['customdata'][0] for x in selection['points'] ]
    temp = data.loc[ data.CSDUID.isin(indicies)]
    if ascending == 'False':
        temp.sort_values([column,'Geography'],ascending=[False,True],inplace=True)
    else:
        temp.sort_values([column,'Geography'], ascending=True, inplace=True)
    return table_update(temp,column)

app.run_server(debug=True, use_reloader=False)