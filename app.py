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
            dcc.Markdown("""
            Represent the number of different types of Administrative pages visited by the visitor in that session
            """, style={"textAlign": "center"}),
            daq.Knob(
                id='my-slider1',
                min=0,
                value=3,
                max=30,
                size=125,
                style={"textAlign": "center"}
                )  ,
            html.Div(id='slider-output-container1', style={"textAlign": "center"}),
            html.H5("Administrative Duration", style={"textAlign": "center"}),
            dcc.Markdown("""
            Total time spent on administrative pages
            """, style={"textAlign": "center"}),
            dcc.Slider(
                    id = "my-slider2",
                    min=0,
                    max=3500,
                    step=1,
                    value=-80
                ),
            html.Div(id='slider-output-container2', style={"textAlign": "center"}),
            html.H5("Informational", style={"textAlign": "center"}),
                        dcc.Markdown("""
            Represent the number of different types of Informational pages visited by the visitor in that session
            """, style={"textAlign": "center"}),
            dcc.Slider(
                    id = "my-slider3",
                    min=-0,
                    max=25,
                    step=1,
                    value=-1
                ),
            html.Div(id='slider-output-container3', style={"textAlign": "center"}),

            html.H5("Visitor Type", style={"textAlign": "center"}),
            dcc.RadioItems(
                id="my-slider7",
                options=[
                    {'label': "Returning Visitor", 'value': 1},
                    {'label': "New Visitor", 'value': 2},
                    {'label': "Other", 'value': 3},
                    ],
                value='1',
                labelStyle={'display': 'inline'}
            ) ,
            html.Div(id='slider-output-container7', style={"textAlign": "center"}),

            html.H5("Operating System", style={"textAlign": "center"}),
            dcc.Markdown("""
            Anonymized operating system data 
            """, style={"textAlign": "center"}),
            dcc.RadioItems(
                id="my-slider14",
                options=[
                    {'label': "1", 'value': 1},
                    {'label': "2", 'value': 2},
                    {'label': "3", 'value': 3},
                    {'label': "4", 'value': 4},
                    {'label': "5", 'value': 5},
                    {'label': "6", 'value': 6},
                    {'label': "7", 'value': 7},
                    {"label": "8", "value": 8}
                    ],
                value='1',
                labelStyle={'display': 'inline'}
            )  ,
            html.Div(id='slider-output-container14', style={"textAlign": "center"}),

            html.H5("Browser", style={"textAlign": "center"}),
            dcc.Markdown("""
            Anonymized browser data
            """, style={"textAlign": "center"}),
            dcc.Dropdown(
                id="my-slider15",
                options=[
                    {'label': 'Browser 1', 'value': 1},
                    {'label': 'Browser 2', 'value': 2},
                    {'label': 'Browser 3', 'value': 3},
                    {'label': 'Browser 4', 'value': 4},
                    {'label': 'Browser 5', 'value': 5},
                    {'label': 'Browser 6', 'value': 6},
                    {'label': 'Browser 7', 'value': 7},
                    {'label': 'Browser 8', 'value': 8},
                    {'label': 'Browser 9', 'value': 9},
                    {'label': 'Browser 10', 'value': 10},
                    {'label': 'Browser 11', 'value': 11},
                    {'label': 'Browser 12', 'value': 12},
                    {'label': 'Browser 13', 'value': 13},
                ],
                value="Browser 1"
            )  ,
            html.Div(id='slider-output-container15', style={"textAlign": "center"}),

            html.H5("Region", style={"textAlign": "center"}),
            dcc.Markdown("""
            Anonymized region data
            """, style={"textAlign": "center"}),
            dcc.Dropdown(
                id="my-slider16",
                options=[
                    {'label': 'Region 1', 'value': 1},
                    {'label': 'Region 2', 'value': 2},
                    {'label': 'Region 3', 'value': 3},
                    {'label': 'Region 4', 'value': 4},
                    {'label': 'Region 5', 'value': 5},
                    {'label': 'Region 6', 'value': 6},
                    {'label': 'Region 7', 'value': 7},
                    {'label': 'Region 8', 'value': 8},
                    {'label': 'Region 9', 'value': 9}
                ],
                value="Region 1"
            )  ,
            html.Div(id='slider-output-container16', style={"textAlign": "center"}),

            html.H5("Informational Duration", style={"textAlign": "center"}),
             dcc.Markdown("""
            Total time spent on product informational pages
            """, style={"textAlign": "center"}),
            daq.Knob(
                id='my-slider17',
                min=0,
                value=3,
                max=50,
                size=75,
                style={"textAlign": "center"}
                )  ,
            html.Div(id='slider-output-container17', style={"textAlign": "center"}),

            html.H5("Weekend", style={"textAlign": "center"}),
            dcc.Markdown("""
            Is it the weekend?
            """, style={"textAlign": "center"}),
            daq.BooleanSwitch(
                id='my-slider13',
                on=False
            ),
            html.Div(id='slider-output-container13', style={"textAlign": "center"}),
                        html.H5("Traffic Type", style={"textAlign": "center"}),
            dcc.Slider(
                    id = "my-slider11",
                    min=1,
                    max=20,
                    marks={i: f"{i}" for i in range(1,21)}
                ),
            html.Div(id='slider-output-container11', style={"textAlign": "center"}) , 

            html.H5("Month", style={"textAlign": "center"}),
            dcc.Dropdown(
                id="my-slider12",
                options=[
                    {'label': 'February', 'value': 1},
                    {'label': 'March', 'value': 2},
                    {'label': 'May', 'value': 3},
                    {'label': 'June', 'value': 4},
                    {'label': 'July', 'value': 5},
                    {'label': 'August', 'value': 6},
                    {'label': 'September', 'value': 7},
                    {'label': 'October', 'value': 8},
                    {'label': 'November', 'value': 9},
                    {'label': 'December', 'value': 10}
                ],
                value="February"
            )  ,
            html.Div(id='slider-output-container12', style={"textAlign": "center"})      
        ], className="six columns"),

        html.Div([
             html.H5("Special Day"),
            dcc.Markdown("""
            "Special Day" feature indicates the closeness of the site visiting time to a specific special day 
            (e.g. Mother’s Day, Valentine's Day) in which the sessions are more likely to be finalized with 
            transaction. The value of this attribute is determined by considering the dynamics of e-commerce 
            such as the duration between the order date and delivery date. For example, for Valentina’s day, 
            this value takes a nonzero value between February 2 and February 12, zero before and after this 
            date unless it is close to another special day, and its maximum value of 1 on February 8
            """, style={"textAlign": "center"}),
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
            dcc.Markdown("""
            "Page Value" feature represents the average value for a web page that a user
             visited before completing an e-commerce transaction
            """, style={"textAlign": "center"}),
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
            dcc.Markdown("""
            "Bounce Rate" feature for a web page refers to the percentage of visitors who enter the site from 
            that page and then leave ("bounce") without triggering any other requests to the analytics server
             during that session
            """, style={"textAlign": "center"}),
            daq.Knob(
                id='my-slider6',
                min=0,
                value=0.043,
                max=0.2,
                size=80,
                style={"textAlign": "center"}
                ),
            html.Div(id='slider-output-container6', style={"textAlign": "center"}), 

            html.H5("Product Related", style={"textAlign": "center"}),
            dcc.Markdown("""
            Represent the number of different types of Informational pages visited by the visitor in that session
            """, style={"textAlign": "center"}),
            dcc.Slider(
                    id = "my-slider8",
                    min=0,
                    max=700,
                    marks={i: f"{i}" for i in range(0,800,100)}
                ),
            html.Div(id='slider-output-container8', style={"textAlign": "center"})   , 

            html.H5("Product Related Duration", style={"textAlign": "center"}),
            dcc.Markdown("""
            Total time spent on product related pages
            """, style={"textAlign": "center"}),
            daq.Knob(
                id='my-slider9',
                min=0,
                value=1196,
                max=70000,
                size=150,
                style={"textAlign": "center"}
                ) ,
            html.Div(id='slider-output-container9', style={"textAlign": "center"})   , 

            html.H5("Exit Rates", style={"textAlign": "center"}),
            dcc.Markdown("""
            "Exit Rate" feature for a specific web page is calculated as for all pageviews to the page, 
            the percentage that were the last in the session
            """, style={"textAlign": "center"}),
            dcc.Slider(
                    id = "my-slider10",
                    min=-5,
                    max=10,
                    step=0.5,
                    value=-3
                ),
            html.Div(id='slider-output-container10', style={"textAlign": "center"})
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

@app.callback(
    dash.dependencies.Output('slider-output-container7', 'children'),
    [dash.dependencies.Input('my-slider7', 'value')])
def update_output(value):
    return f"You have selected {value}"

@app.callback(
    dash.dependencies.Output('slider-output-container8', 'children'),
    [dash.dependencies.Input('my-slider8', 'value')])
def update_output(value):
    return f"You have selected {value}"

@app.callback(
    dash.dependencies.Output('slider-output-container9', 'children'),
    [dash.dependencies.Input('my-slider9', 'value')])
def update_output(value):
    return f"You have selected {value}"

@app.callback(
    dash.dependencies.Output('slider-output-container10', 'children'),
    [dash.dependencies.Input('my-slider10', 'value')])
def update_output(value):
    return f"You have selected {value}"

@app.callback(
    dash.dependencies.Output('slider-output-container11', 'children'),
    [dash.dependencies.Input('my-slider11', 'value')])
def update_output(value):
    return f"You have selected {value}"

@app.callback(
    dash.dependencies.Output('slider-output-container12', 'children'),
    [dash.dependencies.Input('my-slider12', 'value')])
def update_output(value):
    return f"You have selected {value}"

@app.callback(
    dash.dependencies.Output('slider-output-container13', 'children'),
    [dash.dependencies.Input('my-slider13', 'on')])
def update_output(on):
    return f"{on}"

@app.callback(
    dash.dependencies.Output('slider-output-container14', 'children'),
    [dash.dependencies.Input('my-slider14', 'value')])
def update_output(value):
    return f"You have selected {value}"

@app.callback(
    dash.dependencies.Output('slider-output-container15', 'children'),
    [dash.dependencies.Input('my-slider15', 'value')])
def update_output(value):
    return f"You have selected {value}"

@app.callback(
    dash.dependencies.Output('slider-output-container16', 'children'),
    [dash.dependencies.Input('my-slider16', 'value')])
def update_output(value):
    return f"You have selected {value}"

@app.callback(
    dash.dependencies.Output('slider-output-container17', 'children'),
    [dash.dependencies.Input('my-slider17', 'value')])
def update_output(value):
    return f"You have selected {value}"


server = app.server
if __name__ == "__main__":
    app.run_server(debug=True)
