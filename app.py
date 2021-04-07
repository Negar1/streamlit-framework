import pandas as pd
import numpy as np
from datetime import datetime
#import altair as alt
from bokeh.plotting import figure, show
from bokeh.resources import CDN
from bokeh.embed import file_html

import streamlit as st
import streamlit.components.v1 as components
#import python-dotenv as penv

#read data:
st.title('My first app')

url= "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=IBM&interval=15min&slice=year1month1&apikey=demo"

df=pd.read_csv(url)
print (df.head(5))
print (len(df))
df['time']= pd.to_datetime(df['time'])
df['date'] = df['time'].dt.date
df['norm_v']=df['volume']/df['volume'].mean()
#df['date'] = df['time'].dt.strftime('%m-%d')
#df['date']=pd.to_datetime(df['date'])

Open= st.checkbox("IBM: Open", value=False, key=None, help=None)
High= st.checkbox("IBM: High", value=False, key=None, help=None)
Low= st.checkbox("IBM: Low", value=False, key=None, help=None)
Close= st.checkbox("IBM: Close", value=False, key=None, help=None)
Volume= st.checkbox("Volume", value=False, key=None, help=None)


x=df["time"]
yo=df["open"]
yh=df["high"]
yl=df["low"]
yc=df["close"]
yv=df["volume"]
ynv=df["norm_v"]
p = figure(title="IBM plot, 2021, last 30 days", x_axis_type='datetime',
           x_axis_label='date', y_axis_label='IBM')
#Open=True
if Open:
    p.line(x, yo, legend_label="IBM: Open", color='blue')
if High:
    p.line(x, yh, legend_label='IBM: High', color='red')
if Low:
    p.line(x, yl, legend_label='IBM: Low', color='green')
if Close:
    p.line(x, yc, legend_label='IBM: Close', color='purple')
if Volume:
    p.line(x, ynv, legend_label='Volume', color='brown')

#p.multi_line([x,x,x], [yo,yh,yl], legend_label="IBM: Open",#, "IBM: high","IBM: Low"], 
#             color=["green", "blue", "black"], alpha=[1,0.9,0.9], line_width=2)
html = file_html(p, CDN, "IBM plot")
#show(p)

#st.write(html)

st.components.v1.html(html, width=720, height=680, scrolling=False)
#chart_data = df[['low', 'high', 'open', 'close']]

#st.line_chart(chart_data)
