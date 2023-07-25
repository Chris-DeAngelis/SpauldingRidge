import streamlit as st
import requests
from huggingface_hub import hf_hub_download#, login, HfApi, ModelFilter, DatasetFilter
from transformers import pipeline
import pandas as pd

#################### Page Settings ####################
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
#################### Page Content ####################
st.title('Ratings & Reviews Demo')
st.write('Securely connect to your data and use this template for extracting more insights out of your product reviews')

data = pd.read_csv('https://raw.githubusercontent.com/Chris-DeAngelis/SpauldingRidge/main/product_reviews.csv',
                   usecols=['name','dateUpdated','reviews.rating','reviews.text','reviews.title'])#'categories',
st.dataframe(df.head())

#################### Load Pre-trained Sentiment Analysis Model ####################
#model = hf_hub_download(repo_id="nlptown/bert-base-multilingual-uncased-sentiment", filename="tf_model.h5")

# Load pre-trained model
#model = 'bert-base-multilingual-uncased-sentiment'

#specify task
#task = 'sentiment-analysis'

# Instantiate pipeline
#analyzer = pipeline(task, model=model)

# Store output of the analysis
#output = analyzer(input_text)

# Return output
#output


#################### Page Logo ####################
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
