import dash
import dash_daq  as daq
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import pickle

url = "https://raw.githubusercontent.com/mpHarm88/blackbox/master/data/online_shoppers_intention.csv"
df = pd.read_csv(url).dropna()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children="Customer Revenue Predictor",
            style={
                "textAlign": "center"}
            ),
    html.H3(children="By Mikio Harman",
            style={
                "textAlign": "center"
            }),
    html.Div([
    html.Div([
        html.Div([
            html.H5('Administrative', style={"textAlign": "center"}),
            daq.Knob(
                id='my-slider1',
                min=0,
                value=3,
                max=30,
                size=200,
                style={"textAlign": "center"}
                )  ,
            html.Div(id='slider-output-container1', style={"textAlign": "center"}),
            html.H5("Administrative Duration", style={"textAlign": "center"}),
            dcc.Slider(
                    id = "my-slider2",
                    min=0,
                    max=3500,
                    step=1,
                    value=-80
                ),
            html.Div(id='slider-output-container2', style={"textAlign": "center"}),
            html.H5("Informational", style={"textAlign": "center"}),
            dcc.Slider(
                    id = "my-slider3",
                    min=-0,
                    max=25,
                    step=1,
                    value=-1
                ),
            html.Div(id='slider-output-container3', style={"textAlign": "center"}),
        ], className="six columns"),

        html.Div([
             html.H5("Special Day"),
            dcc.RadioItems(
                    id = "my-slider4",
                    options=[
                        {'label': 'True', 'value': 1},
                        {'label': 'False', 'value': 0},
                        ],
                    value=1
                )  ,
        html.Div(id='slider-output-container4', style={"textAlign": "center"}),
            html.H5("Page Values", style={"textAlign": "center"}),
            daq.Knob(
                id='my-slider5',
                min=0,
                value=3,
                max=370,
                size=200,
                style={"textAlign": "center"}
                )  ,
            html.Div(id='slider-output-container5', style={"textAlign": "center"}), 

            html.H5("Bounce Rates", style={"textAlign": "center"}),
            dcc.Slider(
                    id = "my-slider6",
                    min=-5,
                    max=10,
                    step=0.5,
                    value=-3
                ),
            html.Div(id='slider-output-container6', style={"textAlign": "center"})   
        ], className="six columns"),
    ], className="row")
])
    
    ])

@app.callback(
    dash.dependencies.Output('slider-output-container1', 'children'),
    [dash.dependencies.Input('my-slider1', 'value')])
def update_output(value):
    return f"You have selected {value}"

@app.callback(
    dash.dependencies.Output('slider-output-container2', 'children'),
    [dash.dependencies.Input('my-slider2', 'value')])
def update_output(value):
    return f"You have selected {value}"

@app.callback(
    dash.dependencies.Output('slider-output-container3', 'children'),
    [dash.dependencies.Input('my-slider3', 'value')])
def update_output(value):
    return f"You have selected {value}"

@app.callback(
    dash.dependencies.Output('slider-output-container5', 'children'),
    [dash.dependencies.Input('my-slider5', 'value')])
def update_output(value):
    return f"You have selected {value}"

@app.callback(
    dash.dependencies.Output('slider-output-container6', 'children'),
    [dash.dependencies.Input('my-slider6', 'value')])
def update_output(value):
    return f"You have selected {value}"

server = app.server
if __name__ == "__main__":
    app.run_server(debug=True)
