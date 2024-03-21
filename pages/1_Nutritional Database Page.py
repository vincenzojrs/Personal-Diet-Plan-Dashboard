import streamlit as st
from database_connection import import_nutritional_database

st.title('Nutritional Database Page')
st.write('The database from Google Sheet where the app retrieve information from. It mainly contains nutritional information regarding food I usually eat')
df = import_nutritional_database()
st.dataframe(df)