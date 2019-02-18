import plotly as py
import plotly.graph_objs as go
import pandas as pd


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
            rangeslider=dict(visible=True),
            type='date'
        ),
    )


    windows = go.Scatter(
        x=df["date"],
        y=df["gecko-t-win10-64-ms"],
        mode="lines+markers",
        name="Windows",
        line=dict(
            shape="spline"
        ),
        fill='tozeroy'
    )
    windows_ux = go.Scatter(
        x=df["date"],
        y=df["gecko-t-win10-64-ux"],
        mode="lines+markers",
        name="Windows UX",
        line=dict(
            shape="spline"
        ),
        fill='tozeroy'
    )
    linux = go.Scatter(
        x=df["date"],
        y=df["gecko-t-linux-talos"],
        mode="lines+markers",
        name="Linux",
        line=dict(
            shape="spline"
        ),
        fill='tozeroy'
    )
    linux_beta = go.Scatter(
        x=df["date"],
        y=df["gecko-t-linux-talos-b"],
        mode="lines+markers",
        name="Linux Beta",
        line=dict(
            shape="spline"
        ),
        fill='tozeroy'
    )
    yosemite = go.Scatter(
        x=df["date"],
        y=df["gecko-t-osx-1010"],
        mode="lines+markers",
        name="Yosemite",
        line=dict(
            shape="spline"
        ),
        fill='tozeroy'
    )
    yosemite_beta = go.Scatter(
        x=df["date"],
        y=df["gecko-t-osx-1010-beta"],
        mode="lines+markers",
        name="Yosemite",
        line=dict(
            shape="spline"
        ),
        fill='tozeroy'
    )

    fig = go.Figure(data=[windows, linux, yosemite, windows_ux, linux_beta,
                          yosemite_beta], layout=layout)

    py.offline.plot(fig, filename="./deploy/index.html")
