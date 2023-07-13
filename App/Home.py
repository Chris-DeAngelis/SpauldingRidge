import streamlit as st
#from snowflake.sqlalchemy import URL
#from sqlalchemy import create_engine
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
st.markdown(
        """
        ### Use the sidebar to navigate between different business use cases    
        """
)
#st.title('Data Ingestion')
with st.expander("Data Ingestion", expanded=True):
    a = st.multiselect(
             "Select one or more tools:", ['A','B','C'], ['B'],
       key = 1
    )

with st.expander("Data Storage & Transformation", expanded=True):
   b = st.multiselect(
             "Select one or more tools:", ['A','B','C'], ['B'],
       key = 2
    )

with st.expander("Data Catalog & Governance", expanded=True):
    c = st.multiselect(
             "Select one or more tools:", ['A','B','C'], ['C'],
       key = 3
    )

with st.expander("Data Analytics & Publication ", expanded=True):
    d = st.multiselect(
             "Select one or more tools:", ['A','B','C'], ['B'],
       key = 4
    )


#zews_query = st.secrets.credentials.query
#@st.cache_resource(ttl=43200) # Update every 10 minutes = 600
# def connect_snowflake():  
#     '''
#     Function to connect to Snowflake. Returns a connected database object that can be queried.
#     '''
#     engine = create_engine(URL(
#             user=st.secrets.credentials.user,
#             password=st.secrets.credentials.password,
#             account=st.secrets.credentials.account,
#             warehouse=st.secrets.credentials.warehouse,
#             database=st.secrets.credentials.database,
#             schema=st.secrets.credentials.schema
#     ))
#     #cs = ctx.cursor()
#     connection = engine.connect()
#     return connection, engine

# @st.cache_data(ttl=43200) # Update every 10 minutes = 600
# def run_query(query=zews_query):
#     '''
#     Function to run query against Snowflake. This function connects to database, runs query, closes connection, and returns query results in a dataframe.
#     '''  
#     try:
#     	connection, engine = connect_snowflake()
#         #connection.execute(zews_query)
#     	df = pd.read_sql_query(zews_query, engine)
#     finally:
#     	connection.close()
#     	engine.dispose()
#     return df

# # Execute queries for Invoices and Macroeconomic Data
# # Caching data from Snowflake
# df = run_query(query=zews_query)
# st.write(df.head())
# if 'zews_sales' not in st.session_state:
#     st.session_state['zews_sales'] = df

# Caching Macroeconomic data from Snowflake
#@st.cache_data
#run_query(query=macroeconomics_query)

# KPI boxes
# to = todf[(todf['Hospital Attended']==hosp) & (todf['Metric']== 'Total Outstanding')]   
# ch = todf[(todf['Hospital Attended']==hosp) & (todf['Metric']== 'Current Handover Average Mins')]   
# hl = todf[(todf['Hospital Attended']==hosp) & (todf['Metric']== 'Hours Lost to Handovers Over 15 Mins')

#m1.write('')
#m2.metric(label ='Total Outstanding Handovers',value = int(to['Value']), delta = str(int(to['Previous']))+' Compared to 1 hour ago', delta_color = 'inverse')
#m3.metric(label ='Current Handover Average',value = str(int(ch['Value']))+" Mins", delta = str(int(ch['Previous']))+' Compared to 1 hour ago', delta_color = 'inverse')
#m4.metric(label = 'Time Lost today (Above 15 mins)',value = str(int(hl['Value']))+" Hours", delta = str(int(hl['Previous']))+' Compared to yesterday')
#m1.write('')

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "Contact Me",
    ("Email", "LinkedIn", "Github Profile")
)

# Load logo
def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(data:image/png;base64,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);
                #https://www.spauldingridge.com/wp-content/uploads/2023/05/logo-dark-051523-278x23.png);
                background-repeat: no-repeat;
                padding-top: 120px;
                background-position: 20px 20px;
                background-size: 200px 200px;
            }
            [data-testid="stSidebarNav"]::before {
                content: "";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 15px;
                position: relative;
                top: 150px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
add_logo()
