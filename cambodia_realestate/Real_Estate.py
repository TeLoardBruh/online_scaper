import folium
from streamlit_folium import st_folium
import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv('realestate_kh_cleaner2023-06-21.csv')
df

df = df.dropna(subset=['lat', 'lon'])

data_lat_list = df['lat'].to_list()
data_lon_list = df['lon'].to_list()

df = pd.DataFrame(
    {
        'lat': data_lat_list,
        'lon': data_lon_list,
    },
)
st.map(df,zoom=2,use_container_width=True)
