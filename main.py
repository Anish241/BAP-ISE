import dash
from dash import dcc, html
import pandas as pd

data = pd.read_csv('24_cleaned.csv')

df = pd.DataFrame(data)

# Create a Dash app
app = dash.Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div(children=[
    html.H1(children='Sample Dashboard'),

    # Table
    html.Div(children=[
        html.H2(children='Data Table'),
        dcc.Graph(
            id='table',
            figure={
                'data': [{
                    'type': 'table',
                    'header': {
                        'values': df.columns
                    },
                    'cells': {
                        'values': df.values.T
                    }
                }]
            }
        )
    ]),

    # Bar chart
   # plot numeber of peoople in each Internship Organization
    html.Div(children=[
        html.H2(children='Number of People in Each Internship Organization'),
        dcc.Graph(
            id='bar-chart',
            figure={
                'data': [{
                    'x': df['Internship Organization'].value_counts().index,
                    'y': df['Internship Organization'].value_counts().values,
                    'type': 'bar'
                }],
                'layout': {
                    'title': 'Number of People in Each Internship Organization'
                }
            }
        )
    ]),

    # Pie chart
    html.Div(children=[
        html.H2(children='Number of People in Each Internship Organization'),
        dcc.Graph(
            id='pie-chart',
            figure={
                'data': [{
                    'labels': df['Internship Organization'].value_counts().index,
                    'values': df['Internship Organization'].value_counts().values,
                    'type': 'pie'
                }],
                'layout': {
                    'title': 'Number of People in Each Internship Organization'
                }
            }
        )
    ]),
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)