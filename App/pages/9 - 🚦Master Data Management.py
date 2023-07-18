import streamlit as st
import pandas as pd
import requests

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

df = pd.DataFrame(
    [
       {"Customer: First Name": ["Brian","Jason","Sally","Briana","Keely","Jake","Myles","Greg"]},
       {"Customer: Last Name": ["Brian","Jason","Sally","Briana","Keely","Jake","Myles","Greg"]},
       {"Customer: Address": ["Brian","Jason","Sally","Briana","Keely","Jake","Myles","Greg"]},
       {"Customer: Phone #": ["Brian","Jason","Sally","Briana","Keely","Jake","Myles","Greg"]},
       {"Customer: Website": ["Brian","Jason","Sally","Briana","Keely","Jake","Myles","Greg"]},
       {"Primary Customer Flag": ["Brian","Jason","Sally","Briana","Keely","Jake","Myles","Greg"]},
       {"Mark For Review": ["Brian","Jason","Sally","Briana","Keely","Jake","Myles","Greg"]}
   ]
)
edited_df = st.data_editor(df, 
                           num_rows='dynamic',
                           use_container_width=True) # 👈 An editable dataframe

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
