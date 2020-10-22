import dash_core_components as dcc


def year_slider(year_column):
    """

    :param year_column:
    :return:
    """
    return dcc.Slider(
        min=year_column.min(),
        max=year_column.max(),
        marks={str(year): str(year) for year in year_column.unique()},
        value=year_column.min(),
        step=None,
        id="year-slider"
    )
