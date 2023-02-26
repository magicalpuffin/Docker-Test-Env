import dash
from dash import html, dcc, dash_table
from dash import callback, Input, Output

import pandas as pd
import numpy as np
import plotly.graph_objects as go

dash.register_page(
    __name__,
    path='/graph2',
    title='Graph 2'
)

df = pd.read_csv('data/temp.csv')

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x= df['linspace100'],
        y= df['linspace200'],
        mode= 'markers'
    )
)

layout = html.Div([
    html.H1('Graph 2'),
    dcc.Dropdown(
        options= df.columns,
        value= df.columns[0],
        id= 'graph2-dropdown',
    ),
    dcc.Graph(figure= fig, id= 'graph2-fig'),
])

@callback(
    Output('graph2-fig', 'figure'),
    Input('graph2-dropdown', 'value')
)
def update_table(df_col):
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x= df['linspace100'],
            y= df[df_col],
            mode= 'markers',
        )
    )

    return fig