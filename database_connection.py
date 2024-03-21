from streamlit_gsheets import GSheetsConnection
import streamlit as st

def import_nutritional_database():
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read(worksheet="Foglio7",
                   ttl="60m",
                   usecols=[0,1,2,3,4,5,6,7,8,9,10,11,12],
                   nrows=100)
    df.dropna(how='all', inplace = True)
    return df

def import_weight_database():
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read(worksheet="weight",
                   ttl="60m",
                   usecols=[0,1,2,3],
                   nrows=1000)
    df.dropna(how='all', inplace = True)
    return df
