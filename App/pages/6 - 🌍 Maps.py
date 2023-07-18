import streamlit as st
import altair as alt
from vega_datasets import data
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


boroughs = alt.topo_feature(data.londonBoroughs.url, 'boroughs')
tubelines = alt.topo_feature(data.londonTubeLines.url, 'line')
centroids = data.londonCentroids.url

background = alt.Chart(boroughs).mark_geoshape(
  stroke='white',
  strokeWidth=2
).encode(
        color=alt.value('#eee'),
    ).properties(
        width=700,
        height=500
    )

labels = alt.Chart(centroids).mark_text().encode(
  longitude='cx:Q',
  latitude='cy:Q',
  text='bLabel:N',
  size=alt.value(8),
        opacity=alt.value(0.6)
    ).transform_calculate(
        "bLabel", "indexof (datum.name,' ') > 0  ? substring(datum.name,0,indexof(datum.name, ' ')) : datum.name"
    )

line_scale = alt.Scale(domain=["Bakerloo", "Central", "Circle", "District", "DLR",
                               "Hammersmith & City", "Jubilee", "Metropolitan", "Northern",
                               "Piccadilly", "Victoria", "Waterloo & City"],
                           range=["rgb(137,78,36)", "rgb(220,36,30)", "rgb(255,206,0)",
                                  "rgb(1,114,41)", "rgb(0,175,173)", "rgb(215,153,175)",
                                  "rgb(106,114,120)", "rgb(114,17,84)", "rgb(0,0,0)",
                                  "rgb(0,24,168)", "rgb(0,160,226)", "rgb(106,187,170)"])

lines = alt.Chart(tubelines).mark_geoshape(
  filled=False,
  strokeWidth=2
    ).encode(
        alt.Color(
            'id:N',
            legend=alt.Legend(
                title=None,
                orient='bottom-right',
                offset=0
            ),
            scale=line_scale
        )
    )

chart = background + labels + lines
st.altair_chart(chart, theme="streamlit", use_container_width=True)

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
