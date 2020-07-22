# First go at a Python program that does something
# Calculates the date of easter for any range of years prompted, obviously using the Gregorian calendar
# writes them to file and three lists then charts them using Plotly https://plot.ly/
#Big snag is the empty range of impossible dates in the chart y axis DJS 02/04/2016
import datetime
import time
import math
import plotly
print (plotly.__version__ ) # version >1.9.4 required
from plotly.graph_objs import Scatter, Layout
start_time = time.time()
print ("Starts ",datetime.datetime.now().time())
f = open('easter.txt', 'w')
easteryear = []
eastermon = []
easterday = []
def easter(year):   # Anon algorithm of 1876 (or close to it) https://en.wikipedia.org/wiki/Computus#Anonymous_Gregorian_algorithm
    a = year % 19
    b = math.floor (year / 100)
    c = year % 100
    d = math.floor (b / 4)
    e = b % 4
    f = math.floor ((b + 8) / 25)
    g = math.floor ((b - f + 1) / 3)
    h = (19*a + b - d - g + 15) % 30
    i = math.floor (c / 4)
    k = c % 4
    L = (32 + 2*e + 2*i - h - k) % 7
    m = math.floor ((a + 11*h + 22*L) / 451)
    month = math.floor ((h + L - 7*m + 114) / 31)
    day = ((h + L - 7*m + 114) % 31) + 1
    return year,month,day
startyear = int(input("Enter the start year YYYY:"))
endyear = int(input("Enter the end year YYYY:"))
endyear += 1   # due to the way range works
for x in range (startyear,endyear):
    yyyymondd = easter(x)
    f.write(str(yyyymondd))
    f.write('\n')
    easteryear.append(yyyymondd[0])
    eastermon.append(yyyymondd[1])
# Yes this is poor, wanted to use datetimes but that had lots of downsides
#    easterday.append((yyyymondd[1] * 100) + yyyymondd[2])
    easterday.append(str(yyyymondd[1]).zfill(2) + str(yyyymondd[2]).zfill(2))
f.close()
plotly.offline.plot({
"data": [
    Scatter(x=easteryear, y=easterday,mode = 'markers')
],
"layout": Layout(
    title="Dates of Easter by Year",
    xaxis=dict(title= "Year",
               showticklabels = True,
               dtick=int((endyear-startyear)/10)
               ),
    yaxis=dict(title = "Month & Day",
                showticklabels = True,
                dtick=3,
                tickfont=dict(
                family='Arial, sans-serif',
                size=7,
                color='black'),
               )
)
})
print("Ends   ",datetime.datetime.now().time())
print("Took    %s seconds" % (time.time() - start_time))
