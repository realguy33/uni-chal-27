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
st.write("it appears that there was an increase in swapping volume during november which makes sense since that was near the peak of bullrun")

st.subheader("UNISWAP-OPTIMISM swapping volume")
st.plotly_chart(figuniop,use_container_width=True)

st.subheader("UNISWAP-POLYGON swapping volume")
st.plotly_chart(figunipol,use_container_width=True)

st.subheader("CURVE-ARBITRUM swapping volume")
st.plotly_chart(figcrvarb,use_container_width=True)
st.subheader("CURVE-OPTIMISM swapping volume")
st.plotly_chart(figcrvop,use_container_width=True)

st.subheader("CURVE-POLYGON swapping volume")
st.plotly_chart(figcrvpol,use_container_width=True)

st.subheader("CONCLUSIONS:")
st.write("1- It appears that Uniswap has a lead over Curve in the daily swap volumes on L2s. This is interesting because Curve has a higher TVL(at the moment) than Uniswap.")
st.write("2- This lead shows that users of L2 generally prefer Uniswap as their DEX over Curve")
st.write("3- It seems polygon is the most popular L2 among the users of Uniswap but arbitrum seems to be doing great as well")
st.write("4- the daily swapping volume of L2s may have decreased due to the prevelant market conditions in the recent weeks")
st.write("5- The swapping is still somewhat high despite the recent decrease , this shows that L2s might be slowly picking up in popularity")

st.subheader("data sources-")
st.write("https://thegraph.com/hosted-service/subgraph/convex-community/volume-optimism")
st.write("https://thegraph.com/hosted-service/subgraph/convex-community/volume-arbitrum")
st.write("https://thegraph.com/hosted-service/subgraph/convex-community/volume-matic")
st.write("https://thegraph.com/hosted-service/subgraph/ianlapham/optimism-post-regenesis")
st.write("https://thegraph.com/hosted-service/subgraph/ianlapham/arbitrum-minimal")
st.write("https://thegraph.com/hosted-service/subgraph/ianlapham/uniswap-v3-polygon")

st.write("github repo - https://github.com/realguy33/uni-chal-27/")

