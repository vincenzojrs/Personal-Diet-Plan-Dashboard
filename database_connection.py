from oauth2client.service_account import ServiceAccountCredentials
from streamlit_gsheets import GSheetsConnection
from google.oauth2 import service_account
import streamlit as st
import gspread

def connect_nutritional_database():
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read(worksheet="nutritional_database",
                    ttl="60m",
                    usecols=[0,1,2,3,4,5,6,7,8,9,10,11,12],
                    nrows=100)
    df.dropna(how='all', inplace = True)
    return df

def connect_weight_database(mode: str = 'read', data = None):
    if mode == 'read':
        conn = st.connection("gsheets", type=GSheetsConnection)
        df = conn.read(worksheet="weight",
                    ttl="60m",
                    usecols=[0,1,2,3],
                    nrows=1000)
        # Drop rows where all values are missing
        df.dropna(how='all', inplace = True)
        # Inferring missing data using linear interpolation
        df.interpolate(method='linear', inplace=True)
        return df
    elif mode == 'write':
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_dict(st.secrets['gsheets'], scope)
        client = gspread.authorize(creds)
        sh = client.open('PersonalPlan').worksheet('weight_to_update')
        sh.append_row(data)
