import plotly.express as px

DEFAULT_PARAMS = dict(
    lat="lat",
    lon="lon",
    center=dict(
        lat=46.560,
        lon=-66.112

    ),
    size='log_std',
    size_max=25,
    opacity=0.8,
    zoom=5,
    hover_name='Geography',
    custom_data=['CSDUID']
)


def figure_factory(data, topic, geo=None, **kwargs):
    """Returns A Plotly MapBox dictionary

    Basic Mapbox for displaying New Brunswick Data
    :param data: A pandas DataFrame,
    :param topic: str, A Column Name in data,
    :param geo: A GeoJSON FeatureCollection,
    :return: fig: Plotly MapBox
    """

    params = DEFAULT_PARAMS.copy()

    for key, value in kwargs.items():
        params[key] = value

    params['color'] = topic

    fig = px.scatter_mapbox(data, **params)
    if geo:
        fig.update_layout(
            mapbox={'layers': [{
                'source': geo,
                'type': "fill", 'below': "traces", 'color': "#dedede",
                'opacity': 0.3
            }]}

        )
    fig.update_layout(mapbox_style="carto-positron")
    fig.update_layout(uirevision='same')
    return fig



