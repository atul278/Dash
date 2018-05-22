import dash
import dash_core_components as dcc
import plotly.graph_objs as go
import dash_html_components as html
import numpy as np

def func():

	x = np.linspace(0, 20, 100)
	y = np.random.randn(100)
#	print(x.shape[0])
#	print(y.shape[0])
#x	test_1(x.shape[0],y.shape[0]
	app = dash.Dash()
    # print("hi")
	app.layout = html.Div(children=[
    		html.H1(children='Hello Dash'),
	dcc.Graph(
        figure=go.Figure(
            data=[
	        go.Scatter(
        x = x,
        y = y,
        mode = 'lines',
        name = 'lines'
    )
        ],
        layout=go.Layout(
            title='Random line plot',
            showlegend=True,
            legend=go.Legend(
                x=0,
                y=1.0
            ),
#            margin=go.Margin(l=40, r=0, t=40, b=30)
        )
        ),
        style={'height': 300},
        id='my-graph1'
        ),

    dcc.Graph(
        figure=go.Figure(
        data=[
            go.Pie(
                labels=["friends","GOT","HIMYM","Breking bad","House of cards","Suits"],
                values=[95, 98, 80, 97, 95, 93],
                name='Rest of world',
                )
        ],
        layout=go.Layout(
            title='Tv series',
            showlegend=True,
            legend=go.Legend(
                x=0,
                y=1.0
            ),
            margin=go.Margin(l=40, r=0, t=40, b=30)
            )
        ),
        style={'height': 300},
        id='my-graph2'
        )
	])
#	app.run_server(debug=True)
	return x.shape[0],y.shape[0],app

def test_2():
    a,b,app=func()
    print(a,b)
    app.run_server(debug=True)
    assert a==b