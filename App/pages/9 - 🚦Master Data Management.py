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
# initialize list of lists
data = [['Brian', 'Joesphson', '32 S Drury Lane, VA 27343', '(253)234-2122','mysupplyparts.com',True],
        ['Sally', 'Fields', '1232 N Hampton, NY 22340', '(153)256-0010','petfood.com',True]]
  
# Create the pandas DataFrame
df = pd.DataFrame(data, columns=['First Name','Last Name','Address','Phone #','Website','Mark For Review'])

df = pd.DataFrame(
    [  {"First Name": ["Brian","Jason","Sally","Briana","Keely","Jake","Myles","Greg"]},
       {"Last Name": ["Brian","Jason","Sally","Briana","Keely","Jake","Myles","Greg"]}#,
#        {"Address": ["Brian","Jason","Sally","Briana","Keely","Jake","Myles","Greg"]},
#        {"Phone #": ["Brian","Jason","Sally","Briana","Keely","Jake","Myles","Greg"]},
#        {"Website": ["Brian","Jason","Sally","Briana","Keely","Jake","Myles","Greg"]},
#        {"Mark For Review": ["Brian","Jason","Sally","Briana","Keely","Jake","Myles","Greg"]}
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
