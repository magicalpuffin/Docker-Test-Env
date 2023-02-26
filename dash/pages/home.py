import dash
from dash import html, dcc

dash.register_page(
    __name__,
    path='/',
    redirect_from=['/home'],
    title='Home'
)

layout = html.Div(
    [
        dcc.Markdown('''
        # CSS Testing
        # H1
        ## H2
        ### H3
        #### H4
        Normal Text
        *Italic*
        **Bold**
        ***Italic and Bold***
        '''),
    ]
)