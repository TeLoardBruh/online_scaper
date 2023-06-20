import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame({
        "lat" : [11.5400445],
        "lon" : [104.95696239350958]
    })

st.map(df)