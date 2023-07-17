import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
#import numpy as np
import pygwalker as pyg

st.set_page_config(
    page_title="Data Science @ Spaulding Ridge | Chris DeAngelis, 2023",
    page_icon=":bar_chart:",
    layout="wide"#,
    #initial_sidebar_state="collapsed"
    #menu_items={
    #    'Get Help': 'chris.deangelis@elkay.com'#,
        #'Report a bug': "https://www.extremelycoolapp.com/bug",
        #'About': "# This is a header. This is an *extremely* cool app!"
    #}    
)

df = pd.read_csv(
   'https://raw.githubusercontent.com/Chris-DeAngelis/SpauldingRidge/main/supermarket_sales%20-%20Sheet1.csv',
   usecols = ['Branch','City','Customer type','Gender','Product line','Unit price','Quantity','Total','Date','Time','Payment','gross income'],
   parse_dates = ['Date']
)

gwalker = pyg.walk(df, return_html=True)
# Embed the HTML into the Streamlit app
components.html(gwalker, height=1000, scrolling=True)
