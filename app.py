import sys

import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import plotly.graph_objs as go

from utils import csv_utils, data_utils, layout_utils

# Add custom Python package
# sys.path.append("\\\\mac\\Home\\Documents\\GitHub\\dash-demo\\utils")
sys.path.append("/Users/acasagrande/Documents/GitHub/dash-demo/utils")


# The app instance
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app = dash.Dash(__name__)

# Get CSV file and fetch data
csv_files = csv_utils.get_files()
data = csv_utils.get_data(csv_files[0])  # pandas DataFrame
# header = data.columns

# Describes what the application looks like
# Dash provides classes for all visual components
# Some Markdown text below
intro_markdown_text = """
Dash is a Python framework and this is a simple Web Application made with *Dash*.\n
Charts are made using sample data taken from the CSV file **%s**.
""" % csv_files[0].name

descr_markdown_text = """
The following fields are available:\n\n
"""
header_map = layout_utils.header()
for idx, elem in enumerate(header_map):
    descr_markdown_text += "%s. **%s** (field=%s)\n" % (idx +
                                                        1, elem[1], elem[0])

# Create a bar chart counting CPEs by geographic area
cat1, series1 = data_utils.aggregate_data_by_field(
    data, field="metadata.REGIONE")  # By region
cat2, series2 = data_utils.aggregate_data_by_field(
    data, field="metadata.PROVINCIA")  # By province
# Different colors for bars in bar chart by their value
# Declare a NumPy array starting from bar heights
y1 = np.array(series1)
y2 = np.array(series2)
color1 = layout_utils.create_color_map(y1)
color2 = layout_utils.create_color_map(y2)
plot1 = go.Bar(x=cat1, y=series1, marker=dict(
    color=color1.tolist()), opacity=0.6)
plot2 = go.Bar(x=cat2, y=series2, marker=dict(
    color=color2.tolist()), opacity=0.6)

# Create a pie chart
pie_labels, pie_values = data_utils.aggregate_data_by_field(
    data, field="metadata.TECNOLOGIA")
pie_chart1 = go.Pie(labels=pie_labels, values=pie_values)

app.layout = html.Div(
    children=[
        html.H1(children="Hello Dash"),
        html.H2(children="This is a simple Dash Web Application"),
        dcc.Markdown(children=intro_markdown_text),
        dcc.Markdown(children=descr_markdown_text),
        html.Div([
            html.Div([
                html.H3("CPEs count by Region"),
                html.P("The following bar chart shows the number of CPEs per Region"),
                dcc.Graph(id="bar-chart-by-region", figure={"data": [plot1]})
            ], className="bar-chart"),
            html.Div([
                html.H3("CPEs count by Province"),
                html.P(
                    "The following bar chart shows the number of CPEs per Province"),
                dcc.Graph(id="bar-chart-by-province", figure={"data": [plot2]})
            ], className="bar-chart")
        ], className="bar-chart-row"),
        html.Div([
            html.H3("CPEs aggregated by Technology"),
            dcc.Graph(id="pie-chart-by-tech", figure={"data": [pie_chart1]})
        ])
    ]
)

# Run the app using python app.py and visit http://127.0.0.1:8050/
if __name__ == "__main__":
    app.run_server(debug=True)
