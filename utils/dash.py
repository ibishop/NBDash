import dash_core_components as dcc
import dash_html_components as html


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

def print_selection(point):


    return


def buttons(columns):
    """

    :param columns: str array columns of a data
    :return:
    """
    return dcc.Dropdown(
                id='selected-column',
                options=[{'label': i, 'value': i} for i in columns],
                value=columns[0]
            )