# Inspiration
#https://www.microprediction.com/blog/popular-timeseries-packages
#https://microprediction.github.io/timeseries-elo-ratings/html_leaderboards/overall.html

import streamlit as st
#import configparser
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#import holidays
from aeon.forecasting.trend import TrendForecaster
from statsmodels.tsa.seasonal import seasonal_decompose
#from fbprophet import Prophet
#from sklearn.metrics import mean_squared_error, r2_score
#https://pykalman.github.io/
#from pykalman import KalmanFilter
#import pmdarima as pm #https://pypi.org/project/pmdarima/
#from pmdarima.model_selection import train_test_split

#import xgboost as xgb
#from sklearn.model_selection import TimeSeriesSplit, GridSearchCV

if "shared" not in st.session_state:
   st.session_state["shared"] = True

st.set_page_config(
    page_title="Data Science @ Spaulding Ridge | Chris DeAngelis, 2023",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'http://spauldingridge.com',
        #'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# Built by Chris DeAngelis, CFA | cdeangelis@spauldingridge.com"
    }
)

st.title('Forecasting Demo')
st.header('Securely connect to your data and use this flexible forecasting tool')
st.write('Apply filters, see model transparency, explainability, and accuracy')

with st.expander("Instructions", expanded=False):
    st.caption("1. Select level to forecast: channel, business vertical, etc.")
    st.caption("2. Apply any filters to incorporate in the analysis")
    st.caption("3. Optional: Try and enhance the forecast using external, macroeconomic variables")

with st.expander("Sample Data Preview", expanded=True):
    try:
        verticals = st.multiselect(
            "Choose Business Verticals", ['A','B','C'], ['B']
        )
        if not verticals:
            st.error("Please select at least one business vertical.")
        else:
            st.write("#####")# Qty (Units)", df.sort_index())

            #data = data.T.reset_index()
            #data = pd.melt(data, id_vars=["index"]).rename(
            #    columns={"index": "year", "value": "Gross Agricultural Product ($B)"}
            #)
           # chart = (
           #     alt.Chart(df)
           #     .mark_area(opacity=0.3)
           #     .encode(
           #         x="Year:T",
           #         y=alt.Y("Net Invoice Amt ($M):Q", stack=None),
           #         color="Product Segment:N",
           #     )
           # )
            #st.altair_chart(chart, use_container_width=True)
    finally:
        st.write("")

df = pd.read_csv(
    "https://raw.githubusercontent.com/selva86/datasets/master/AirPassengers.csv",
    header=0,
    names=["time", "passengers"],
    index_col='time', 
    parse_dates=True
)
df = pd.read_csv(
   'https://raw.githubusercontent.com/Chris-DeAngelis/SpauldingRidge/main/supermarket_sales%20-%20Sheet1.csv',
   usecols = ['Branch','City','Customer type','Gender','Product line','Unit price','Quantity','Total','Date','Time','Payment','gross income'],
   parse_dates = ['Date']
)
#df = df[['Date: Ship','Qty']]
st.dataframe(df)#df.style.highlight_max(axis=1))
#st.write(df.head())
#df = df[df['Item: Parent'] == 'DSE233194']
# df.set_index('Date: Ship', inplace=True)
# df.sort_index(inplace=True)
# df.dropna(inplace=True)
# df.fillna(0, inplace=True)
# #df['Qty'].fillna(0, inplace=True)

with st.expander("Macroeconomics Data Preview", expanded=False):
    #@st.cache(ttl=600)
    evaluate = st.checkbox(
    "Use external macroeconomic data to influence forecast", value=True#, help=readme["tooltips"]["choice_eval"]
    )
    df = pd.DataFrame(
    [
        {"Index": "ABI", "Description (Double Click to Expand)": "The Architecture Billings Index (ABI) is a leading economic indicator of demand for non-residential construction activity. This includes both commercial and industrial buildings. A positive ABI can be a sign of strength or recovery in the broader economy, while a negative ABI can signal weakness or a coming downturn.", "Link": "https://www.aia.org/resources/10046-the-architecture-billings-index", "Activate": True},
        {"Index": "Dodge", "Description (Double Click to Expand)": "The Dodge Momentum Index is a 12-month leading indicator of non-residential construction spending; focused specifically on patterns in the commercial and institutional segments. The Dodge Momentum Index uses first issued planning or prior to start information as a leading indicator of future construction spending. This is different from other indices in the market. It is used to determine future construction spending and demand for construction products and services, making it a useful tool for manufacturers, construction professionals, and economists.","Link": "https://www.construction.com/news/December-22-Starts", "Activate": True},
        {"Index": "Housing", "Description (Double Click to Expand)": "As provided by the Census, start occurs when excavation begins for the footings or foundation of a building. All housing units in a multifamily building are defined as being started when this excavation begins. Beginning with data for September 1992, estimates of housing starts include units in structures being totally rebuilt on an existing foundation.", "Link": "https://www.census.gov/construction/nrc/index.html","Activate": False},
        {"Index": "Labor", "Description (Double Click to Expand)": "The unemployment rate represents the number of unemployed as a percentage of the labor force. Labor force data are restricted to people 16 years of age and older, who currently reside in 1 of the 50 states or the District of Columbia, who do not reside in institutions (e.g., penal and mental facilities, homes for the aged), and who are not on active duty in the Armed Forces. This rate is also defined as the U-3 measure of labor underutilization. The series comes from the 'Current Population Survey (Household Survey)'", "Link": "https://www.bls.gov/ces/","Activate": False},
        {"Index": "Finance", "Description (Double Click to Expand)": "Gross domestic product (GDP), the featured measure of U.S. output, is the market value of the goods and services produced by labor and property located in the United States.For more information, see the Guide to the National Income and Product Accounts of the United States (NIPA) and the Bureau of Economic Analysis.", "Link": "https://www.bea.gov/data/gdp/gross-domestic-product","Activate": False},
        {"Index": "Prices", "Description (Double Click to Expand)": "Median Consumer Price Index (CPI) is a measure of core inflation calculated the Federal Reserve Bank of Cleveland and the Ohio State University. Median CPI was created as a different way to get a 'Core CPI' measure, or a better measure of underlying inflation trends. To calculate the Median CPI, the Cleveland Fed analyzes the median price change of the goods and services published by the BLS. The median price change is the price change that's right in the middle of the long list of all of the price changes. This series excludes 49.5% of the CPI components with the highest and lowest one-month price changes from each tail of the price-change distribution resulting in a Median CPI Inflation Estimate.According to research from the Cleveland Fed, the Median CPI provides a better signal of the inflation trend than either the all-items CPI or the CPI excluding food and energy. According to newer research done at the Cleveland Fed, the Median CPI is even better at PCE inflation in the near and longer term than the core PCE.", "Link": "https://www.clevelandfed.org/indicators-and-data/median-cpi","Activate": False},
    ]
    )
    #df = load_data()
edited_df = st.experimental_data_editor(df, use_container_width = True) # 👈 An editable dataframe
favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")
st.dataframe(df, use_container_width=True)
#df.set_index('Date: Ship')
        #st.table(df.head()) 

    #     verticals = st.multiselect(
    #         "Choose Business Verticals", list(set(df['Cust: Channel'])), ['TRADITIONAL']
    #     )
    #     if not verticals:
    #         st.error("Please select at least one business vertical.")
    #     else:

    #         data = df[df['Cust: Channel'].isin(verticals)]['Qty'].astype('float')
    #         data /= 1000000.0
    #         #data = data / 1000000.0
    #         st.write("### Qty (Units)", df.sort_index())
    # finally:
    #     st.write("")

with st.expander("Model Settings", expanded=False):
    option_macro = st.checkbox("Use Macroeconomic Data", label_visibility="visible")
    option_freq = st.radio("Forecast Interval", ('Weekly','Monthly','Quarterly'), horizontal=True, label_visibility="visible")
    option_units = st.radio("Forecast Units", ('Sales ($USD)','Units'), horizontal=True, label_visibility="visible")

# sales = df.copy()
# if option_units == 'Sales ($USD)':
#     sales.rename(columns = {'Date: Ship':'ds', 'Sales: Parent':'y'}, inplace = True)
# else:
#     sales.rename(columns = {'Date: Ship':'ds', 'Units':'y'}, inplace = True)
# sales_tidy = sales[['ds','y']]
# sales_tidy.fillna(0, inplace = True)

#train = sales_tidy
# if option_freq == 'Weekly':
#     train = sales_tidy.set_index("ds").resample("W").sum()
# elif option_freq == 'Monthly':
#     train = sales_tidy.set_index("ds").resample("M").sum()
# else:
#     train = sales_tidy.set_index("ds").resample("Q").sum()    
# train['ds'] = train.index
with st.expander("Forecast Interpretation", expanded=False):
    temp = st.checkbox("Placeholder", label_visibility="visible")
    
with st.expander("Model Performance & Error Analysis", expanded=False):
    temp = st.checkbox("Placeholder", label_visibility="visible")
    
with st.expander("Model Seasonality & Factor Analysis", expanded=False):
    temp = st.checkbox("Placeholder", label_visibility="visible")

with st.expander("Export Forecast Data", expanded=False):
    temp = st.checkbox("Placeholder", label_visibility="visible")

with st.expander("What-If Analysis", expanded=False):
    temp = st.checkbox("Placeholder", label_visibility="visible")


##########################################################
# Aeon
# forecaster = TrendForecaster()
# forecaster.fit(df['passengers'])
# TrendForecaster()

# pred = forecaster.predict(fh=[1, 2, 3])
# print(pred)
##########################################################
# Decomposing the time series into trend, seasonality, and residuals
# decomposition = seasonal_decompose(df, model='additive', period = 1)

# # Plotting the decomposed components
# trend = decomposition.trend
# seasonality = decomposition.seasonal
# residuals = decomposition.resid

# fig = plt.figure(figsize=(10,8))

# plt.subplot(411)
# plt.plot(df, label='Original')
# plt.legend(loc='upper left')

# plt.subplot(412)
# plt.plot(trend, label='Trend')
# plt.legend(loc='upper left')

# plt.subplot(413)
# plt.plot(seasonality, label='Seasonality')
# plt.legend(loc='upper left')

# plt.subplot(414)
# plt.plot(residuals, label='Residuals')
# plt.legend(loc='upper left')

# plt.tight_layout()
# plt.show()
# st.pyplot(fig)
##########################################################
# # Load/split your data
# train, test = train_test_split(df['Qty'], train_size=150)

# # Fit your model
# model = pm.auto_arima(train, seasonal=True, m=12)

# # make your forecasts
# forecasts = model.predict(test.shape[0])  # predict N steps into the future

# # Visualize the forecasts (blue=train, green=forecasts)
# x = np.arange(df['Qty'].shape[0])
# plt.plot(x[:150], train, c='blue')
# plt.plot(x[150:], forecasts, c='green')
# plt.show()
# fig = plt.figure()
# #sns.pairplot(df, hue="SKU") 
# st.pyplot(fig)
##########################################################
#st.write(df.head())



# X = np.array([[4, 5, 6, 1, 0, 2], [3.1, 3.5, 1.0, 2.1, 8.3, 1.1]]).T
# y = np.array([1, 6, 7, 1, 2, 3])

# model = xgb.XGBRegressor()
# param_search = {'max_depth' : [3, 5]}

# tscv = TimeSeriesSplit(n_splits=2)
# gsearch = GridSearchCV(estimator=model, cv=tscv,
#                         param_grid=param_search)
# gsearch.fit(X, y)

# from orbit.utils.dataset import load_iclaims #https://github.com/uber/orbit
# from orbit.models import DLT
# from orbit.diagnostics.plot import plot_predicted_data

# from kats.consts import TimeSeriesData #https://github.com/facebookresearch/Kats
# from kats.models.prophet import ProphetModel, ProphetParams

# NEW IMPORT
# from typing import Any, Dict, List
# from streamlit_prophet.lib.dataprep.clean import clean_df
# from streamlit_prophet.lib.dataprep.format import (
#     add_cap_and_floor_cols,
#     check_dataset_size,
#     filter_and_aggregate_df,
#     format_date_and_target,
#     format_datetime,
#     print_empty_cols,
#     print_removed_cols,
#     remove_empty_cols,
#     resample_df,
# )
# from streamlit_prophet.lib.dataprep.split import get_train_set, get_train_val_sets
# from streamlit_prophet.lib.exposition.export import display_links, display_save_experiment_button
# from streamlit_prophet.lib.exposition.visualize import (
#     plot_components,
#     plot_future,
#     plot_overview,
#     plot_performance,
# )
# from streamlit_prophet.lib.inputs.dataprep import input_cleaning, input_dimensions, input_resampling
# from streamlit_prophet.lib.inputs.dataset import (
#     input_columns,
#     input_dataset,
#     input_future_regressors,
# )
# from streamlit_prophet.lib.inputs.dates import (
#     input_cv,
#     input_forecast_dates,
#     input_train_dates,
#     input_val_dates,
# )
# from streamlit_prophet.lib.inputs.eval import input_metrics, input_scope_eval
# from streamlit_prophet.lib.inputs.params import (
#     input_holidays_params,
#     input_other_params,
#     input_prior_scale_params,
#     input_regressors,
#     input_seasonality_params,
# )
# from streamlit_prophet.lib.models.prophet import forecast_workflow
# from streamlit_prophet.lib.utils.load import load_config#, load_image
    
    
# # Correlation matrix
# st.markdown(
# "### Correlation Matrix"
# )
# #st.write(macro_df.head())
# fig, ax = plt.subplots()
# sns.heatmap(macro_df.corr(), cmap="YlGnBu", annot=True)
# st.write(fig)

# Build model
# datasets, models, forecasts = forecast_workflow(
#         config,
#         use_cv,
#         make_future_forecast,
#         evaluate,
#         cleaning,
#         resampling,
#         params,
#         dates,
#         datasets,
#         df,
#         date_col,
#         target_col,
#         dimensions,
#         load_options,
#     )

# report = plot_overview(
#             make_future_forecast, use_cv, models, forecasts, target_col, cleaning, readme, report
#         )

# report = plot_performance(
#             use_cv, target_col, datasets, forecasts, dates, eval, resampling, config, readme, report
#         )

# report = plot_components(
#             use_cv,
#             make_future_forecast,
#             target_col,
#             models,
#             forecasts,
#             cleaning,
#             resampling,
#             config,
#             readme,
#             df,
#             report,
#         )

# report = plot_future(models, forecasts, dates, target_col, cleaning, readme, report)

# Load logo
def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(https://www.spauldingridge.com/wp-content/uploads/2023/05/logo-dark-051523-278x23.png);
                background-repeat: no-repeat;
                padding-top: 120px;
                background-position: 20px 20px;
            }
            [data-testid="stSidebarNav"]::before {
                content: "";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 100px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
add_logo()
