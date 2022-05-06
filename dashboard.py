import numpy as np
import pandas as pd
import streamlit as st
import altair as alt
from datetime import datetime
import plotly.express as px


duniarb = pd.read_csv("duniarb.csv")
duniop = pd.read_csv("duniop.csv")
dunipol = pd.read_csv("dunipol.csv")
dcrvarb = pd.read_csv("dcrvarb.csv")
dcrvop = pd.read_csv("dcrvop.csv")
dcrvpol = pd.read_csv("dcrvpol.csv")


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

st.title("Uniswap Daily Swap Volume in USD on different L2s")
st.write("Uniswap is DEX(Decentrailized Exchange) on Ethereum mainnet and it is also available on various L2s such Arbitrum,Optimism and polygon.")
st.write("The advantage of using these L2s over the ethereum mainnet is that the gas fees on L2s are much much lower than ethereum and these L2s also claim to have the same as that  of ethereum. This makes them attractive to the users.This means that the usage of various L@s should slowly be increasing. is this true? let's find out:")
st.subheader("DATA SOURCES:")
st.write("The data for this dashboard has been taken from various subgraphs available on thegraph.com.They are linked at the end of the dashboard")

st.write("now let's compare the swapping volume between different L2s")

st.subheader("UNISWAP-ARBITRUM swapping volume")
st.plotly_chart(figuniarb,use_container_width=True)

