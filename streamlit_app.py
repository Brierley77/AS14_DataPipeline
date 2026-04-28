import streamlit as st
import pandas as pd
import plotly.express as px

st.title("COVID-19 Data Pipeline Dashboard")
st.write("Interactive dashboard powered by your processed dataset.")

# Load data from GitHub raw URL
url = "https://raw.githubusercontent.com/Brierley77/AS14_DataPipeline/main/covid_with_predictions.csv"
df = pd.read_csv(url)

st.subheader("Dataset Preview")
st.dataframe(df.head())

# Plot 1: Confirmed cases
fig1 = px.line(df, x='Date', y='Confirmed', title='Confirmed Cases Over Time')
st.plotly_chart(fig1)

# Plot 2: New cases
fig2 = px.line(df, x='Date', y='NewCases', title='Daily New Cases')
st.plotly_chart(fig2)

# Plot 3: Actual vs Predicted
fig3 = px.line(df, x='Date', y=['NewCases', 'PredictedNewCases'],
               title='Actual vs Predicted New Cases')
st.plotly_chart(fig3)
