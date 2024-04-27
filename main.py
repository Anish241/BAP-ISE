import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import os

data = pd.read_csv('./Dataset/24_cleaned.csv')
data1 = pd.read_csv('./Dataset/25_cleaned.csv')

df = pd.DataFrame(data)

# Create a Dash app
app = dash.Dash(__name__, url_base_pathname='/')

# serve local static files
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

# Define the layout of the dashboard
main_layout = html.Div(children=[
    html.Link(
        rel='stylesheet',
        href='/static/styles.css'
    ),
    html.Div(className='redirect-button', children=[
        html.A(html.Button('Go to 2025'), href='/2025')
    ], style={'margin': '20px', 'text-align': 'center'}),
    html.H1(children='Research Internship Placements of 2024 Batch - SPIT', style={'textAlign': 'center', 'color': '#FFFFFF'}),
    # Table
    html.Div(className='data-table', children=[
        html.H2(children='Data Table', style={'textAlign': 'center', 'color': '#FFFFFF', 'fontWeight': 'bold'}),
        html.Div(
            className='table-scroll',
            children=html.Table(
                id='table',
                children=[
                    html.Thead(
                        html.Tr([html.Th(col, style={'fontWeight': 'bold', 'border': '1px solid #FFFFFF'}) for col in df.columns])
                    ),
                    html.Tbody([
                        html.Tr([
                            html.Td(df.iloc[i][col], style={'border': '1px solid #FFFFFF'}) for col in df.columns
                        ]) for i in range(len(df))  # Display all rows
                    ])
                ],
                style={'width': '100%', 'margin': 'auto', 'textAlign': 'center', 'borderCollapse': 'collapse', 'border': '1px solid #FFFFFF'}
            ),
            style={'height': '300px', 'overflowY': 'scroll'}
        )
    ], style={'margin': '20px', 'text-align': 'center', 'background-color': '#2c3e50', 'border-radius': '10px'}),
    
    # Bar chart
    html.Div(className='graph-container', children=[
        html.H2(children='Number of People in Each Internship Organization', style={'textAlign': 'center', 'color': '#FFFFFF'}),
        dcc.Graph(
            id='bar-chart',
            figure={
                'data': [{
                    'x': df['Internship Organization'].value_counts().index,
                    'y': df['Internship Organization'].value_counts().values,
                    'type': 'bar',
                    'marker': {'color': '#3498db'}  # Blue color for bars
                }],
                'layout': {
                    'title': 'Number of People in Each Internship Organization',
                    'plot_bgcolor': '#2c3e50',  # Dark background color
                    'paper_bgcolor': '#2c3e50',  # Dark background color
                    'font': {'color': '#FFFFFF'},  # White color for text
                    'height': '400px'  # Increased height
                }
            }
        )
    ], style={'margin': '20px', 'text-align': 'center', 'background-color': '#34495e', 'border-radius': '10px', 'height': '500px'}),

    # Pie chart
    html.Div(className='graph-container', children=[
        html.H2(children='Number of People in Each Internship Organization', style={'textAlign': 'center', 'color': '#FFFFFF'}),
        dcc.Graph(
            id='pie-chart',
            figure={
                'data': [{
                    'labels': df['Internship Organization'].value_counts().index,
                    'values': df['Internship Organization'].value_counts().values,
                    'type': 'pie',
                    'marker': {'colors': ['#3498db', '#e74c3c', '#2ecc71', '#f39c12', '#9b59b6']}  # Set custom colors
                }],
                'layout': {
                    'title': 'Number of People in Each Internship Organization',
                    'plot_bgcolor': '#2c3e50',  # Dark background color
                    'paper_bgcolor': '#2c3e50',  # Dark background color
                    'font': {'color': '#FFFFFF'}  # White color for text
                }
            }
        )
    ], style={'margin': '20px', 'text-align': 'center', 'background-color': '#34495e', 'border-radius': '10px'}),

    # Pie chart for IITs
    html.Div(className='graph-container', children=[
        html.H2(children='Number of Students in Each IIT', style={'textAlign': 'center', 'color': '#FFFFFF'}),
        dcc.Graph(
            id='iit-pie-chart',
            figure={
                'data': [{
                    'labels': df[df['IsIIT'] == True]['Internship Organization'].value_counts().index,
                    'values': df[df['IsIIT'] == True]['Internship Organization'].value_counts().values,
                    'type': 'pie',
                    'marker': {'colors': ['#3498db', '#e74c3c', '#2ecc71', '#f39c12', '#9b59b6']}  # Set custom colors
                }],
                'layout': {
                    'title': 'Number of Students in Each IIT',
                    'plot_bgcolor': '#2c3e50',  # Dark background color
                    'paper_bgcolor': '#2c3e50',  # Dark background color
                    'font': {'color': '#FFFFFF'}  # White color for text
                }
            }
        )
    ], style={'margin': '20px', 'text-align': 'center', 'background-color': '#34495e', 'border-radius': '10px'}),

    # Pie chart for non-IIT organizations
    html.Div(className='graph-container', children=[
        html.H2(children='Number of Students in Each Non-IIT Organization', style={'textAlign': 'center', 'color': '#FFFFFF'}),
        dcc.Graph(
            id='non-iit-pie-chart',
            figure={
                'data': [{
                    'labels': df[df['IsIIT'] == False]['Internship Organization'].value_counts().index,
                    'values': df[df['IsIIT'] == False]['Internship Organization'].value_counts().values,
                    'type': 'pie',
                    'marker': {'colors': ['#3498db', '#e74c3c', '#2ecc71', '#f39c12', '#9b59b6']}  # Set custom colors
                }],
                'layout': {
                    'title': 'Number of Students in Each Non-IIT Organization',
                    'plot_bgcolor': '#2c3e50',  # Dark background color
                    'paper_bgcolor': '#2c3e50',  # Dark background color
                    'font': {'color': '#FFFFFF'}  # White color for text
                }
            }
        )
    ], style={'margin': '20px', 'text-align': 'center', 'background-color': '#34495e', 'border-radius': '10px'}),

    # Bar chart for IITs vs Other Organizations
    html.Div(className='graph-container', children=[
        html.H2(children='Placement in IITs vs Other Organizations', style={'textAlign': 'center', 'color': '#FFFFFF'}),
        dcc.Graph(
            id='iit-bar-chart',
            figure={
                'data': [{
                    'x': ['IITs', 'Other Organizations'],
                    'y': [df[df['IsIIT'] == True].shape[0], df[df['IsIIT'] == False].shape[0]],
                    'type': 'bar',
                    'marker': {'color': ['#3498db', '#e74c3c']}  # Blue for IITs, Red for other organizations
                }],
                'layout': {
                    'title': 'Placement in IITs vs Other Organizations',
                    'plot_bgcolor': '#2c3e50',  # Dark background color
                    'paper_bgcolor': '#2c3e50',  # Dark background color
                    'font': {'color': '#FFFFFF'}  # White color for text
                }
            }
        )
    ], style={'margin': '20px', 'text-align': 'center', 'background-color': '#34495e', 'border-radius': '10px', 'height': '400px'}),

    # Button to redirect to /2025
 html.Div(className='redirect-button', children=[
        html.A(html.Button('Go to 2025'), href='/2025')
    ], style={'margin': '20px', 'text-align': 'center'})
],
 id = 'content'
)

another_layout = html.Div(children=[
    html.Link(
        rel='stylesheet',
        href='/static/styles.css'
    ),
    html.Div(className='redirect-button', children=[
        html.A(html.Button('Go to 2024'), href='/')
    ], style={'margin': '20px', 'text-align': 'center'}),
    html.H1(children='Research Internship Placements of 2025 Batch - SPIT', style={'textAlign': 'center', 'color': '#FFFFFF'}),
    # Table
    html.Div(className='data-table', children=[
        html.H2(children='Data Table', style={'textAlign': 'center', 'color': '#FFFFFF', 'fontWeight': 'bold'}),
        html.Div(
            className='table-scroll',
            children=html.Table(
                id='table',
                children=[
                    html.Thead(
                        html.Tr([html.Th(col, style={'fontWeight': 'bold', 'border': '1px solid #FFFFFF'}) for col in data1.columns])
                    ),
                    html.Tbody([
                        html.Tr([
                            html.Td(data1.iloc[i][col], style={'border': '1px solid #FFFFFF'}) for col in data1.columns
                        ]) for i in range(len(data1))  # Display all rows
                    ])
                ],
                style={'width': '100%', 'margin': 'auto', 'textAlign': 'center', 'borderCollapse': 'collapse', 'border': '1px solid #FFFFFF'}
            ),
            style={'height': '300px', 'overflowY': 'scroll'}
        )
    ], style={'margin': '20px', 'text-align': 'center', 'background-color': '#2c3e50', 'border-radius': '10px'}),
        html.Div(className='graph-container', children=[
        html.H2(children='Number of Students from Each Class', style={'textAlign': 'center', 'color': '#FFFFFF'}),
        dcc.Graph(
            id='class-bar-graph',
            figure={
                'data': [
                    {
                        'x': data1['Class'].unique(),
                        'y': data1['Class'].value_counts().values,
                        'type': 'bar',
                        'marker': {'color': '#3498db'}  # Blue color for bars
                    }
                ],
                'layout': {
                    'title': 'Number of Students from Each Class',
                    'xaxis': {'title': 'Class'},
                    'yaxis': {'title': 'Number of Students'},
                    'plot_bgcolor': '#2c3e50',  # Dark background color
                    'paper_bgcolor': '#2c3e50',  # Dark background color
                    'font': {'color': '#FFFFFF'},  # White color for text
                    'height': 400  # Set the height of the graph
                }
            }
        )
    ], style={'margin': '20px', 'text-align': 'center', 'background-color': '#34495e', 'border-radius': '10px'}),
    html.Div(className='graph-container', children=[
        html.H2(children='Number of People in Each Internship Organization', style={'textAlign': 'center', 'color': '#FFFFFF'}),
        dcc.Graph(
            id='pie-chart',
            figure={
                'data': [{
                    'labels': data1['Internship Organization'].value_counts().index,
                    'values': data1['Internship Organization'].value_counts().values,
                    'type': 'pie',
                    'marker': {'colors': ['#3498db', '#e74c3c', '#2ecc71', '#f39c12', '#9b59b6']}  # Set custom colors
                }],
                'layout': {
                    'title': 'Number of People in Each Internship Organization',
                    'plot_bgcolor': '#2c3e50',  # Dark background color
                    'paper_bgcolor': '#2c3e50',  # Dark background color
                    'font': {'color': '#FFFFFF'}  # White color for text
                }
            }
        )
    ], style={'margin': '20px', 'text-align': 'center', 'background-color': '#34495e', 'border-radius': '10px'}),
    html.Div(className='graph-container', children=[
        html.H2(children='Number of Students in Each IIT', style={'textAlign': 'center', 'color': '#FFFFFF'}),
        dcc.Graph(
            id='iit-pie-chart',
            figure={
                'data': [{
                    'labels': data1[data1['IsIIT'] == True]['Internship Organization'].value_counts().index,
                    'values': data1[data1['IsIIT'] == True]['Internship Organization'].value_counts().values,
                    'type': 'pie',
                    'marker': {'colors': ['#3498db', '#e74c3c', '#2ecc71', '#f39c12', '#9b59b6']}  # Set custom colors
                }],
                'layout': {
                    'title': 'Number of Students in Each IIT',
                    'plot_bgcolor': '#2c3e50',  # Dark background color
                    'paper_bgcolor': '#2c3e50',  # Dark background color
                    'font': {'color': '#FFFFFF'}  # White color for text
                }
            }
        )
    ], style={'margin': '20px', 'text-align': 'center', 'background-color': '#34495e', 'border-radius': '10px'}),
        html.Div(className='graph-container', children=[
        html.H2(children='Number of Students in Each NON IIT Organization', style={'textAlign': 'center', 'color': '#FFFFFF'}),
        dcc.Graph(
            id='iit-pie-chart',
            figure={
                'data': [{
                    'labels': data1[data1['IsIIT'] == False]['Internship Organization'].value_counts().index,
                    'values': data1[data1['IsIIT'] == False]['Internship Organization'].value_counts().values,
                    'type': 'pie',
                    'marker': {'colors': ['#3498db', '#e74c3c', '#2ecc71', '#f39c12', '#9b59b6']}  # Set custom colors
                }],
                'layout': {
                    'title': 'Number of Students in Each NON IIT Organization',
                    'plot_bgcolor': '#2c3e50',  # Dark background color
                    'paper_bgcolor': '#2c3e50',  # Dark background color
                    'font': {'color': '#FFFFFF'}  # White color for text
                }
            }
        )
    ], style={'margin': '20px', 'text-align': 'center', 'background-color': '#34495e', 'border-radius': '10px'}),
], id = 'content1')

@app.callback(
    Output('content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    if pathname == '/':
        return main_layout
    elif pathname == '/2025':
        return another_layout
    else:
        return '404 - Page not found'
    
# configure paths 
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id="content",children=main_layout)
])




# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
