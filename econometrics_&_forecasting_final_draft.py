# Cleaned-up version of your script, ready for Streamlit
# - All file paths are updated to use relative paths (not /content/)
# - Ready to be uploaded to GitHub and run on Streamlit

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from scipy import stats
import statsmodels.api as sm
from statsmodels.tsa.arima.model import ARIMA
import datetime

import streamlit as st

# -- Function to clean and convert CSVs --
def read_and_convert_csv(filepath):
    df = pd.read_csv(filepath)
    for col in df.columns:
        if df[col].dtype == 'object':
            try:
                numeric_col = pd.to_numeric(df[col], errors='coerce')
                if numeric_col.notna().mean() > 0.8:
                    if (numeric_col.dropna() % 1 == 0).all():
                        df[col] = numeric_col.astype('Int64')
                    else:
                        df[col] = numeric_col.astype(float)
            except:
                pass
    return df

# -- Load all necessary CSVs (ensure these are uploaded to GitHub) --
FinancialLiteracyNational = read_and_convert_csv("Econometrics & Forecasting - Andreea.csv")
TECH = read_and_convert_csv("Econometrics & Forecasting - Shanice (TECH).csv")
HEALTHCARE = read_and_convert_csv("Econometrics & Forecasting - Shanice (HEALTHCARE).csv")
FINANCE = read_and_convert_csv("Econometrics & Forecasting - Shanice (FINANCE).csv")
CONSUMERDISCRETIONARY = read_and_convert_csv("Econometrics & Forecasting - Shanice (CONSUMER DISCRETIONARY).csv")
COMMUNICATIONS = read_and_convert_csv("Econometrics & Forecasting - Ayaka Communication.csv")
AI = read_and_convert_csv("Econometrics & Forecasting - Ayaka AI.csv")

# -- You would continue from here by renaming columns, merging data, and performing analysis as in your original script.
# For Streamlit, you'll want to wrap key actions in st.sidebar, st.selectbox, st.write, st.pyplot, st.plotly_chart etc.

# Example Streamlit visualization:
st.title("Financial Literacy and Sector Analysis")

st.header("Investment by Gender")
fig_gender = plt.figure(figsize=(6,4))
sns.countplot(x='gender', hue='do you invest', data=FinancialLiteracyNational)
plt.title("Investment Interest by Gender")
plt.tight_layout()
st.pyplot(fig_gender)

st.header("Finance Sector Trend")
FINANCE['date'] = pd.to_datetime(FINANCE['date'], errors='coerce')
FINANCE = FINANCE.set_index('date')
finance_resampled = FINANCE['close price'].resample('M').mean()
fig_finance = px.line(finance_resampled, title='Finance Stock Price Over Time')
st.plotly_chart(fig_finance)

# -- Add more sections as needed based on your project structure --
