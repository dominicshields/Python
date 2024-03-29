import plotly.tools as tls
tls.set_credentials_file(username='dshields', api_key='5kd72wj4if')
import plotly.plotly as py
import plotly.graph_objs as go

import datetime

def to_unix_time(dt):
    epoch =  datetime.datetime.utcfromtimestamp(0)
    return (dt - epoch).total_seconds() * 1000

x = [
    datetime.datetime(year=2013, month=10, day=4),
    datetime.datetime(year=2013, month=11, day=5),
    datetime.datetime(year=2013, month=12, day=6)
]

data = [
    go.Scatter(
        x=x,
        y=[1, 3, 6]
    )
]

layout = go.Layout(
    xaxis = dict(
        range = [
            to_unix_time(datetime.datetime(2013, 10, 17)),
            to_unix_time(datetime.datetime(2013, 11, 20))
        ]
    )
)


fig = go.Figure(data = data, layout = layout)

plot_url = py.plot(fig, filename='python-datetime-custom-ranges')
