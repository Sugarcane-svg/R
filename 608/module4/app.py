
from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px


app = Dash(__name__)

# get url
url = (
    'https://data.cityofnewyork.us/resource/uvpi-gqnh.json?' +
    '$select=boroname,spc_common,health,steward,count(health)' +
    '&$group=boroname,spc_common,health,steward' +
    '&$where=boroname!=\' \' AND spc_common!=\' \' AND health!=\' \'' +
    '&$limit=40000'
).replace(' ', '%20')

# print(url)

# store into data frame
df = pd.read_json(url)


# layout structure
app.layout = html.Div(
    [   # hearder
        html.Div([
            html.H1("2015 Street Tree Census"),
            html.H4("by Jie Zou")

        ]),

        # main dropdown list
        dcc.Dropdown(
            options=['Bronx', 'Brooklyn', 'Manhattan',
                     'Queens', 'Staten Island'],
            placeholder='select a borough',
            id='boro-dropdown'
        ),

        # first question
        html.Div(
            [   # title
                html.Div([
                    html.H3('Question 1'),
                    'what proportion of trees are in good, fair, or poor health according to the \'health\' variable?'
                ]),
                # content
                html.Div([
                    html.Div(dcc.Graph(id='fig1'))
                ])


            ]
        ),

        html.Br(),
        # second question
        html.Div(
            [   # title
                html.Div([
                    html.H3('Question 2'),
                    'Are steward(steward activity measured by the \'steward\' variable) having an impact on the health of trees?'
                ]),
                # content
                html.Div([
                    html.Div(dcc.Graph(id='fig2'))
                ])
            ]
        )
    ]
)

df1 = df.drop('steward', axis=1)  # drop steward for question 1
df2 = df.drop('count_health', axis=1)  # drop count_health for question 2
df2['health'] = pd.factorize(df2['health'].astype('category'))[0]
df2['steward'] = pd.factorize(df2['steward'].astype('category'))[0]


@app.callback(
    Output('fig1', 'figure'),
    Output('fig2', 'figure'),
    Input('boro-dropdown', 'value')
)
def update_graph(value):
    # filter data by selected borough
    df = df1[df1['boroname'] == value]
    
    # get data
    d1 = pd.DataFrame(df.groupby(['spc_common', 'health']).sum()[
        'count_health'] / df1.groupby(['spc_common']).sum()['count_health']).reset_index()

    # plot for the first question
    fig1 = px.bar(d1, x='spc_common', y='count_health',
                  color='health', barmode='stack')

    # do the same for the second data
    d2 = df2[df2['boroname'] == value]

    # calculate the correlation
    dd = d2.groupby(['spc_common']).corr().reset_index()

    # plot for the second question
    fig2 = px.bar(dd, x='spc_common', y='health')

    return fig1, fig2


if __name__ == '__main__':
    app.run_server(debug=True)
