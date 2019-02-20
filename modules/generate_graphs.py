import plotly as py
import plotly.graph_objs as go
import pandas as pd
from datetime import datetime as dt
from datetime import timedelta as td
from modules.config import VERBOSE


def generate_html_graphs():
    py.offline.init_notebook_mode(connected=True)
    df = pd.read_csv("./csv_data/releng_hardware_data.csv")

    layout = go.Layout(
        title="RelEng Hardware",
        yaxis=dict(title="Pending Tasks"),
        xaxis=dict(rangeselector=dict(buttons=list([
            dict(count=1,
                 label='1d',
                 step='day',
                 stepmode='backward'),
            dict(count=7,
                 label='1w',
                 step='day',
                 stepmode='backward'),
            dict(count=1,
                 label='1m',
                 step='month',
                 stepmode='backward'),
            dict(count=3,
                 label='3m',
                 step='month',
                 stepmode='backward'),
            dict(count=6,
                 label='6m',
                 step='month',
                 stepmode='backward'),
            dict(count=1,
                 label='1y',
                 step='year',
                 stepmode='backward'),
            dict(step='all')])),
            rangeslider=dict(visible=False),
            type='date',
        ),
    )
    data = []
    for entry in df:
        if entry == "date":
            pass
        else:
            data.append(go.Scattergl(
                x=df["date"],
                y=df[entry],
                name=entry,
                fill="tozeroy",
                hoverlabel=dict({"namelength": -1}))
            )

    fig = dict(data=data, layout=layout)

    one_day = [dt.now() - td(1), dt.now()]
    # Set default default graph view to 1 day.
    fig['layout']['xaxis'].update(range=one_day)

    if VERBOSE:
        print("Rebuilding Graph Data.")

    py.offline.plot(fig, include_plotlyjs="cdn", filename="./templates/index.html", auto_open=True)
