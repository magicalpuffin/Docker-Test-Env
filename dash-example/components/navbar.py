import dash_bootstrap_components as dbc
from dash import html
import dash

def navbar():
    layout = dbc.NavbarSimple([
        dbc.NavLink("Home", href="/"),
        dbc.NavLink("Graph1", href="/graph1"),
        dbc.NavLink("Graph2", href="/graph2"),
    ], links_left= True)
    return layout