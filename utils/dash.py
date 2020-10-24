import dash_core_components as dcc
import dash_html_components as html
import dash_table


CITY_NAME_COL = 'Geography'
CITY_TYPE_COL = 'Unamed 2:'

def year_slider(year_column):
    """

    :param year_column: Pandas Series
    :return: Dash Slider component, loaded with appropriate values
    """
    return dcc.Slider(
        min=year_column.min(),
        max=year_column.max(),
        marks={str(year): str(year) for year in year_column.unique()},
        value=year_column.min(),
        step=None,
        id="year-slider"
    )


def build_table():
    '''
    Builds basic table component with id

    :return: dash_table component
    '''
    return dash_table.DataTable(
        id='table',
        page_size=14
    )


def table_update(df, column):
    '''
    Returns dash_table children for updating

    :param df: A Pandas DataFrame
    :return: dash_table component
    '''
    cols = [ CITY_NAME_COL ] + [ column ]
    df = df.loc[: ,cols]

    return [{"name": i, "id": i} for i in df.columns],df.to_dict('records')

def geography_searchbar(names):
    '''
    Search Bar to select items by city name

    :param names: List-like, contains names for dropdown menu
    :return:
    '''
    return dcc.Dropdown(
                id='name-search',
                options=[{'label': i, 'value': i} for i in names],
                persistence=True,
                multi=True
            )


def sort_menu():
    return dcc.RadioItems(
        options=[
            {'label': 'Ascending', 'value': "True"},
            {'label': 'Descending', 'value': "False"}
        ],
        value = 'True',
        labelStyle={'display': 'inline-block'}
    )

def buttons(columns):
    """
    Returns dropdown compoenent

    :param columns: str array columns of a data
    :return:
    """
    return dcc.Dropdown(
                id='selected-column',
                options=[{'label': i, 'value': i} for i in columns],
                value=columns[0]
            )