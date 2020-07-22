import plotly.tools as tls
tls.set_credentials_file(username='dshields', api_key='5kd72wj4if')
import plotly
from plotly.graph_objs import Scatter, Layout
import plotly.plotly as py
import plotly.graph_objs as go

from datetime import datetime
x = [
    datetime(year=2013, month=10, day=4),
    datetime(year=2013, month=11, day=5),
    datetime(year=2013, month=12, day=6)
]
plotly.offline.plot({
"data": [
    go.Scatter(
        x=x,
        y=[1, 3, 6]
    )
],
"layout": Layout(
    title="hello world"
)
})
