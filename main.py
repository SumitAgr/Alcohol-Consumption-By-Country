import pandas as pd
import plotly.graph_objects as go

dataset = pd.read_csv('total-alcohol-consumption-per-capita-litres-of-pure-alcohol.csv')

fig = go.Figure(data = go.Choropleth(
    locations = dataset['Entity'],
    z = dataset['Alcohol consumption'],
    locationmode = 'country names',
    text = dataset['Entity'],
    colorscale = 'Oranges',
    autocolorscale = False,
    reversescale = False,
    marker_line_color = 'black',
    marker_line_width = 0.5,
    colorbar_title = 'Total Alcohol Consumption <br> Per Capita by Country (2016)',
))

fig.update_layout(
    title_text = "Total Alcohol Consumption Per Capita by Country (2016)",
    geo = dict(
        showframe = False,
        showcoastlines = False,
        projection_type = 'equirectangular'
    ),
    annotations = [dict(
        x = 0.55,
        y = 0.1,
        xref = 'paper',
        yref = 'paper',
        text = 'Source: <a href="https://datacatalog.worldbank.org/dataset/world-development-indicators">\
            World Bank</a>',
        showarrow = False
    )]
)

fig.show()