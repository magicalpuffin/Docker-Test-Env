import dash
from dash import html, dcc

import pandas as pd
import numpy as np
import plotly.graph_objects as go

dash.register_page(
    __name__,
    path='/graph1',
    title='Graph 1'
)

df = pd.read_csv('data/temp.csv')

fig = go.Figure(go.Histogram(x = df['randomnormal']))

layout = html.Div([
    html.H1('Graph 1'),
    dcc.Graph(figure= fig)
])