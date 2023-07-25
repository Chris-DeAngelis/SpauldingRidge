import streamlit as st
import requests
import pandas as pd

st.set_page_config(
    page_title="Spaulding Ridge | Analytics & AI",
    page_icon=":bar_chart:", #"👋",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'http://spauldingridge.com',
        #'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# Built by Chris DeAngelis, CFA | cdeangelis@spauldingridge.com"
    }
)

st.write("# Welcome to Spaulding Ridge's Analytics & AI Demonstration Workspace")#:bar_chart::rocket:")

# Load logo
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
