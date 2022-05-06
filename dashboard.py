import numpy as np
import pandas as pd
import streamlit as st
import altair as alt
from datetime import datetime
import plotly.express as px


duniarb = pd.read_csv("./uni-chal-27/duniarb.csv")
duniop = pd.read_csv("./uni-chal-27/duniop.csv")
dunipol = pd.read_csv("./uni-chal-27/dunipol.csv")
dcrvarb = pd.read_csv("./uni-chal-27/dcrvarb.csv")
dcrvop = pd.read_csv("./uni-chal-27/dcrvop.csv")
dcrvpol = pd.read_csv("./uni-chal-27/dcrvpol.csv")


figuniarb = px.bar(duniarb, x= "uniswapDayDatas_datetime",y = "uniswapDayDatas_volumeUSD") 
figuniarb.update_layout(
    xaxis_title="date",
    yaxis_title="volume",
)
figuniop = px.bar(duniop, x= "uniswapDayDatas_datetime",y = "uniswapDayDatas_volumeUSD") 
figuniop.update_layout(
    xaxis_title="date",
    yaxis_title="volume",
)
figunipol = px.bar(dunipol, x= "uniswapDayDatas_datetime",y = "uniswapDayDatas_volumeUSD") 
figunipol.update_layout(
    xaxis_title="date",
    yaxis_title="volume",
)
figcrvarb = px.bar(dcrvarb,  x= "dailySwapVolumeSnapshots_datetime",y = "dailySwapVolumeSnapshots_volumeUSD")
figcrvarb.update_layout(
    xaxis_title="date",
    yaxis_title="volume",
)
figcrvop = px.bar(dcrvop,  x= "dailySwapVolumeSnapshots_datetime",y = "dailySwapVolumeSnapshots_volumeUSD")
figcrvop.update_layout(
    xaxis_title="date",
    yaxis_title="volume",
)
figcrvpol = px.bar(dcrvpol, x= "dailySwapVolumeSnapshots_datetime",y = "dailySwapVolumeSnapshots_volumeUSD")
figcrvpol.update_layout(
    xaxis_title="date",
    yaxis_title="volume",
)


#stream lit work

st.title("Swapping Volumes in USD on Uniswap on different L2s")
