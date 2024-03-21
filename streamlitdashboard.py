import streamlit as st

st.set_page_config(layout = 'wide')

from main import Monday, Tuesday, Wednesday, Thursday

monday_dataframe = Monday.summary()

st.title('Enzo devi dimagrire')
st.write('La dieta di Lunedi')
st.dataframe(monday_dataframe)
