import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import pickle

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children="Tester Predictor",
            style={
                "textAlign": "center"}
            ),
    
    ])

server = app.server
if __name__ == "__main__":
    app.run_server(debug=True)
