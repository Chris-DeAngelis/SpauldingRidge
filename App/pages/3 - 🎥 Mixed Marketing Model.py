import streamlit as st
import plotly


# @st.experimental_memo
# def get_chart_23633134():
#     import plotly.express as px
#     import pandas as pd
#     stages = ["Website visit", "Downloads", "Potential customers", "Requested price", "invoice sent"]
#     df_mtl = pd.DataFrame(dict(number=[39, 27.4, 20.6, 11, 3], stage=stages))
#     df_mtl['office'] = 'Montreal'
#     df_toronto = pd.DataFrame(dict(number=[52, 36, 18, 14, 5], stage=stages))
#     df_toronto['office'] = 'Toronto'
#     df = pd.concat([df_mtl, df_toronto], axis=0)
#     fig = px.funnel(df, x='number', y='stage', color='office')

#     tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
#     with tab1:
#         st.plotly_chart(fig, theme="streamlit")
#     with tab2:
#         st.plotly_chart(fig, theme=None)
