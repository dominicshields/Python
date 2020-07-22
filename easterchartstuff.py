x = [
    datetime(year=2013, month=10, day=4),
    datetime(year=2013, month=11, day=5),
    datetime(year=2013, month=12, day=6)
]
plotly.offline.plot({
"data": [
    Scatter(x=[1, 2, 3, 4], y=[4, 1, 3, 7])
],
"layout": Layout(
    title="hello world"
)
})
