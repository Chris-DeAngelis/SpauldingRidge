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
#st.title('Data Ingestion')
# with st.expander("Data Ingestion", expanded=True):
#     a = st.multiselect(
#              "Select one or more tools:", ['A','B','C'], ['B'],
#        key = 1
#     )

# with st.expander("Data Storage & Transformation", expanded=True):
#    b = st.multiselect(
#              "Select one or more tools:", ['A','B','C'], ['B'],
#        key = 2
#     )

# with st.expander("Data Catalog & Governance", expanded=True):
#     c = st.multiselect(
#              "Select one or more tools:", ['A','B','C'], ['C'],
#        key = 3
#     )

# with st.expander("Data Analytics & Publication ", expanded=True):
#     d = st.multiselect(
#              "Select one or more tools:", ['A','B','C'], ['B'],
#        key = 4
#     )


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

# page_names_to_funcs = {
#     "Main Page": main_page,
#     "Page 2": page2,
#     "Page 3": page3,
# }

# selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
# page_names_to_funcs[selected_page]()

# Load logo
def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(https://github.com/Chris-DeAngelis/SpauldingRidge/blob/main/App/SR%20Logo.PNG?raw=true);
                width: auto;
                height: 250px;
                background-repeat: no-repeat;
                padding-top: 10px;
                background-position: 20px 20px;
            }
            [data-testid="stSidebarNav"]::before {
                content: "";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 20px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
add_logo()
