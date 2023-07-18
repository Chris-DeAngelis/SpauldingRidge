import streamlit as st
import streamlit.components.v1 as components
import requests
import pandas as pd
#import numpy as np
import pygwalker as pyg

st.set_page_config(
    page_title="Spaulding Ridge | Analytics & AI",
    page_icon=":bar_chart:", #"👋",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'http://spauldingridge.com',
        #'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# Built by Chris DeAngelis, CFA | cdeangelis@spauldingridge.com"
    }
)

df = pd.read_csv(
   'https://raw.githubusercontent.com/Chris-DeAngelis/SpauldingRidge/main/supermarket_sales%20-%20Sheet1.csv',
   usecols = ['Branch','City','Customer type','Gender','Product line','Unit price','Quantity','Total','Date','Time','Payment','gross income'],
   parse_dates = ['Date']
)

gwalker = pyg.walk(df, return_html=True)
# Embed the HTML into the Streamlit app
components.html(gwalker, height=1000, scrolling=True)

def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(https://github.com/Chris-DeAngelis/SpauldingRidge/blob/main/App/SR%20Logo.PNG?raw=true);
                background-repeat: no-repeat;
                padding-top: 50px;
                padding-left: 10px;
                background-position: 50px 50px;
                background-size: 250px 125px;
            }
            [data-testid="stSidebarNav"]::before {
                content: "";
                margin-left: 20px;
                margin-top: 200px;
                font-size: 30px;
                position: relative;
                top: 320px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
add_logo()
