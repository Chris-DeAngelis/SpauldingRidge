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

st.title('Master Data Management & Data Entry Tool')
st.write('See how easily you can review, modify, add, and delete data before submitting')

# initialize list of lists
data = [['Brian', 'Joesphson', '32 S Drury Lane, VA 27343', '(253)234-2122','mysupplyparts.com',True],
        ['Sally', 'Fields', '1232 N Hampton, NY 22340', '(153)256-0010','petfood.com',True]]
  
# Create the pandas DataFrame
df = pd.DataFrame(data, columns=['First Name','Last Name','Address','Phone #','Website','Mark For Review'])

df = pd.DataFrame({
       "First Name": ["Brian","Jason","Sally","Briana","Keely","Jake","Myles","Greg"],
       "Last Name": ["Joesphson","Yuly","Fields","Rimrose","James","Smith","Sitter","Angel"],
       "Address": ['32 S Drury Lane, VA 27343',"1232 N Hampton, NY 22340","12 W River Rd WI 20509","667 James, OH 50455","12 NE Cambell #42, NY 22112","123 W Montrose Ave, PA 20404","1222 Elway Lane, CO 10450","45 Dolly Ave, SC 70454"],
       "Phone #": ["(253)234-2122","425.045.4445","2344432123","1-245-454-0150","(654)-456-0545","(6544)-112-0504","(132)-234-2434","(756)-453-5234"],
       "Website": ["mysupplyparts.com","petfood.com","google.com","espn.com","diageo.com","nfl","snowflake.com","gmail.com"],
       "Mark For Review": [False,True,False,False,True,False,False,False]
})

edited_df = st.data_editor(df, 
                           num_rows='dynamic',
                           use_container_width=True) # 👈 An editable dataframe

# Adding buttons
st.button('Post Results to Database', key=1)
st.button('Clear Changes', key=2)

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
