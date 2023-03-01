import dash
from dash import html, dcc, dash_table
from dash import callback, Input, Output

import dash_bootstrap_components as dbc

from components.navbar import navbar

app = dash.Dash(
    __name__,
    use_pages= True,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    title= "Docker Dash Example"
)

app.layout = html.Div(
    [
        navbar(),
        html.Div(dash.page_container),
    ]
)

server = app.server

# if __name__ == "__main__":
#     app.run_server(debug=True)
if __name__ == "__main__":
    app.run_server(debug=True, host='0.0.0.0', port= 8080)