# Even better, save your credentials permanently using the 'tools' module:
# import plotly.tools as tls
# tls.set_credentials_file(username='dshields', api_key='5kd72wj4if')


# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api

import plotly.plotly as py
import plotly.graph_objs as go

from datetime import datetime
x = [
    datetime(year=2013, month=10, day=04),
    datetime(year=2013, month=11, day=05),
    datetime(year=2013, month=12, day=06)
]

data = [
    go.Scatter(
        x=x,
        y=[1, 3, 6]
    )
]
plot_url = py.plot(data, filename='python-datetime')




# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api

import plotly.plotly as py
import plotly.graph_objs as go

data = [
    go.Scatter(
        x=['2013-10-04 22:23:00', '2013-11-04 22:23:00', '2013-12-04 22:23:00'],
        y=[1, 3, 6]
    )
]
plot_url = py.plot(data, filename='date-axes')







import plotly.plotly as py
import plotly.graph_objs as go

import datetime

def to_unix_time(dt):
    epoch =  datetime.datetime.utcfromtimestamp(0)
    return (dt - epoch).total_seconds() * 1000

x = [
    datetime.datetime(year=2013, month=10, day=04),
    datetime.datetime(year=2013, month=11, day=05),
    datetime.datetime(year=2013, month=12, day=06)
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


