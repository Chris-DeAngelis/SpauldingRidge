import streamlit as st
import pandas as pd
#import numpy as np
import pygwalker as pyg

df = pd.read_csv(
   'https://raw.githubusercontent.com/Chris-DeAngelis/SpauldingRidge/main/supermarket_sales%20-%20Sheet1.csv',
   usecols = ['Branch','City','Customer type','Gender','Product line','Unit price','Quantity','Total','Date','Time','Payment','gross income'],
   parse_dates = ['Date']
)

gwalker = pyg.walk(df)
