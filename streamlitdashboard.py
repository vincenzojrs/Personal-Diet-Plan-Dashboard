import streamlit as st
import pandas as pd

st.set_page_config(layout = 'wide', page_title = 'Enzo devi dimagrire', page_icon = ':pig:')
st.title('Enzo devi dimagrire')

from main import Monday, Tuesday, Wednesday, Thursday

monday_dataframe = Monday.summary(verbose = True)
tuesday_dataframe = Tuesday.summary(verbose = True)
wednesday_dataframe = Wednesday.summary(verbose = True)

tab1, tab2, tab3 = st.tabs(["Monday", "Tuesday", "Wednesday"])

with tab1:
    st.subheader("Mondays' diet")
    st.dataframe(monday_dataframe[0], use_container_width = True)
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Daily nutrients")
        st.dataframe(monday_dataframe[1], use_container_width = True)
    with col2:
        st.subheader("Macronutrients contribution")
        st.dataframe(monday_dataframe[-1].T, use_container_width = True)
    st.subheader("Meal nutrients")
    st.dataframe(monday_dataframe[2], use_container_width = True)
              
with tab2:
    st.subheader("Tuesdays' diet")
    st.dataframe(tuesday_dataframe[0], use_container_width = True)
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Daily nutrients")
        st.dataframe(tuesday_dataframe[1], use_container_width = True)
    with col2:
        st.subheader("Macronutrients contribution")
        st.dataframe(tuesday_dataframe[-1].T, use_container_width = True)
              
with tab3:
    st.subheader("Wednesdays' diet")
    st.dataframe(wednesday_dataframe[0], use_container_width = True)
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Daily nutrients")
        st.dataframe(wednesday_dataframe[1], use_container_width = True)
    with col2:
        st.subheader("Macronutrients contribution")
        st.dataframe(wednesday_dataframe[-1].T, use_container_width = True)
              
