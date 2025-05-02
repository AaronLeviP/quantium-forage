from dash import Dash, html, dcc, Input, Output, callback
from plotly.express import line
import pandas as pd

app = Dash()

DATA_PATH = 'data/combined_data.csv'
COLORS = {
    'background': '#ede8d0',
    'text': '#000000'
}

df = pd.read_csv(DATA_PATH, parse_dates=['date'])

# Header
header = html.H1(
    'Soul Food: Pink Morsel Sales',
    style={
        'textAlign': 'center',
        'color': COLORS['text'],
        'border-radius': '10px'
    }
)

# region picker
region_picker = dcc.RadioItems(
    ['north', 'east', 'south', 'west', 'all'],
    'north',
    id='region_picker',
    style={
        'textAlign': 'center',
        'color': COLORS['text']
    },
    inline=True
)

# visualizer
visualizer = dcc.Graph(
    id='sales_graph'
)

app.layout = html.Div(
    [
        header,
        visualizer,
        region_picker,
    ],
    style={
        'background-color': COLORS['background']
    }
)

@callback(
    Output('sales_graph', 'figure'),
    Input('region_picker', 'value'))
def update_graph(region):
    if region == 'all':
        dff = df.copy()
        fig = line(dff, x="date", y="sales", title=f"Pink Morsel Sales for All Regions")
    else:
        dff = df[df['region'] == region]
        fig = line(dff, x="date", y="sales", title=f"Pink Morsel Sales for the {region.capitalize()}ern Region")

    fig.update_layout(
        plot_bgcolor=COLORS['background'],
        paper_bgcolor=COLORS['background'],
        font_color=COLORS['text']
    )

    return fig

if __name__ == '__main__':
    app.run(debug=True)
