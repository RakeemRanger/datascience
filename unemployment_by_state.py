import dash
from dash import  html 
from dash import  dcc 
from dash.dependencies import Output, Input
import pandas as pd


app = dash.Dash(__name__)
state_data = pd.read_csv('unemployment_states_2021.csv')
app.layout = html.Div([
    html.H4('This Page is designed to visualize Unemployment Data by State.', style={'margin':'center', 'color':'blue'}),
    html.H6('Select your State of interest from the dropdown menu below; to view data from your respective State.', style={'margin':'center', 'color':'blue'}),
    dcc.Dropdown(id='state_dropdown',style={'backgroundColor':'#696969'}, options=[{'label': state,'value':
    state}
                    for state in 
                    state_data['State'].unique()]),
                    html.Br(),
html.Div(id='report'),



])


@app.callback(Output('report', 'children'), 
            Input('state_dropdown', 'value'))


def display_selected(state):


    
    state_interested = state_data[(state_data['State']== state) ]
    state_interested1 = state_interested['unemployment_rate'].values[0] 
    year = state_data['year'].values[0]
    state_message = 'The unemployment rate for ' + str(state)  + ' in '  + str(year)  + ' was '  + str(state_interested1)
    
    return state_message

if __name__ == '__main__':
    app.run_server(debug=True,)
      
         
