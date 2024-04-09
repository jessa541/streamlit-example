import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title='Extinction Dashboard',
                   page_icon='🌎',
                   layout='wide')

df = pd.read_csv('combined_file.csv')

# Clean the data in "Subtotal (threatened spp.)" column
df['Subtotal (threatened spp.)'] = df['Subtotal (threatened spp.)'].str.replace(',', '')

# Convert the cleaned data to integer
df['Subtotal (threatened spp.)'] = pd.to_numeric(df['Subtotal (threatened spp.)'])

#sidebar
st.sidebar.header('Filter Here:')
country = st.sidebar.multiselect(
    'Select Country:',
    options=df['Name'].unique(),
    default=df['Name'].unique()
)

df_selection = df.query(
    'Name == @country'
)

#Mainpage
st.title(':earth_africa: Extinction Dashboard')
st.markdown('##')

#KPIs
total_threatened = df_selection["Subtotal (threatened spp.)"].sum()

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader(f'Total Threatened Species: {total_threatened}')

st.markdown('---')
