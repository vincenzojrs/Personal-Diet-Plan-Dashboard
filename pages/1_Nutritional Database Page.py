import streamlit as st
from database_connection import connect_nutritional_database
from authentication import logout_button, create_form

st.set_page_config(layout='wide')
st.title('Nutritional Database Page')
st.write('The database from Google Sheet where the app retrieve information from. It mainly contains nutritional information regarding food I usually eat')

create_form()
logout_button()

df = connect_nutritional_database()
st.dataframe(df, use_container_width = True)