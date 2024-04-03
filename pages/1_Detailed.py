import streamlit as st
import pandas as pd

from authentication import create_form, logout_button 

class Webpage:
    def _page_config(self):
        st.set_page_config(layout = 'wide', page_title = 'Enzo devi dimagrire', page_icon = ':pig:')
        st.title('Detailed diet')
        create_form()
        logout_button()        

    def _page_data(self):
        from main import Monday, Tuesday, Wednesday, Thursday, Friday
        monday_dataframe = Monday.summary(verbose = True)
        tuesday_dataframe = Tuesday.summary(verbose = True)
        wednesday_dataframe = Wednesday.summary(verbose = True)
        thursday_dataframe = Thursday.summary(verbose = True)
        friday_dataframe = Friday.summary(verbose = True)
        #thursday_dataframe = Thursday.summary(verbose = True)
        return monday_dataframe, tuesday_dataframe, wednesday_dataframe, thursday_dataframe, friday_dataframe

    def _page_content(self):
        monday_dataframe, tuesday_dataframe, wednesday_dataframe, thursday_dataframe, friday_dataframe = self._page_data()

        tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
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
            st.subheader("Meal nutrients")
            st.dataframe(tuesday_dataframe[2], use_container_width = True)
                    
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
            st.subheader("Meal nutrients")
            st.dataframe(wednesday_dataframe[2], use_container_width = True)

        with tab4:
            st.subheader("Thursdays' diet")
            st.dataframe(thursday_dataframe[0], use_container_width = True)
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Daily nutrients")
                st.dataframe(thursday_dataframe[1], use_container_width = True)
            with col2:
                st.subheader("Macronutrients contribution")
                st.dataframe(thursday_dataframe[-1].T, use_container_width = True)
            st.subheader("Meal nutrients")
            st.dataframe(thursday_dataframe[2], use_container_width = True)
                    
        with tab5:
            st.subheader("Fridays' diet")
            st.dataframe(friday_dataframe[0], use_container_width = True)
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Daily nutrients")
                st.dataframe(friday_dataframe[1], use_container_width = True)
            with col2:
                st.subheader("Macronutrients contribution")
                st.dataframe(friday_dataframe[-1].T, use_container_width = True)
            st.subheader("Meal nutrients")
            st.dataframe(friday_dataframe[2], use_container_width = True)

    def __init__(self):
        self._page_config()
        self._page_data()
        self._page_content()

webpage = Webpage()