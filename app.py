from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd

app = Dash()

colors = {
    'background': '#ede8d0',
    'text': '#000000'
}

df = pd.read_csv('data/combined_data.csv', parse_dates=['date'])

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Soul Food: Pink Morsel Sales',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    dcc.RadioItems(
        ['north', 'east', 'south', 'west', 'all'],
        'north',
        id='region-picker',
        style={
            'textAlign': 'center',
            'color': colors['text']
        },
        inline=True
    ),

    dcc.Graph(
        id='sales_graph'
    )
])

@callback(
    Output('sales_graph', 'figure'),
    Input('region-picker', 'value'))
def update_graph(region):
    if region == 'all':
        dff = df.copy()
        fig = px.line(dff, x="date", y="sales", title=f"Pink Morsel Sales for all regions")
    else:
        dff = df[df['region'] == region]
        fig = px.line(dff, x="date", y="sales", title=f"Pink Morsel Sales for the {region}ern region")

    fig.update_layout(
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text']
    )

    return fig

if __name__ == '__main__':
    app.run()
