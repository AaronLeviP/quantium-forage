from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()
df = pd.read_csv('data/combined_data.csv', parse_dates=['date'])
fig = px.line(df, x="date", y="sales")

app.layout = html.Div(children=[
    html.H1(children='Soul Food: Pink Morsel Sales'),

    dcc.Graph(
        id='sales_graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
