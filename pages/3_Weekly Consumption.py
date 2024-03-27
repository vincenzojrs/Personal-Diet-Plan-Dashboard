import streamlit as st
st.set_page_config(layout='wide')
st.title('Weekly Consumption and Expense')
st.header('The quantity to be bought for each food, weekly')

from weekly_consumption import Week_Consumption

weekly_consumption = Week_Consumption().df.iloc[:,[0, -2, -1]]
st.dataframe(weekly_consumption, use_container_width = True)
st.write("Each week you spend {}€ for groceries :smile:".format(weekly_consumption['weekly_expense'].sum()))
