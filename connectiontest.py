import streamlit as st
from gspread_pandas import Spread,Client
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_info(
    st.secrets["connections.gsheets"],
    scopes = scope)

client = Client(scope=scope,creds=credentials)
spreadsheetname = "weight"

spread = Spread(spreadsheetname,client = client)

# Check the connection
st.write(spread.url)

sh = client.open(spreadsheetname)
worksheet_list = sh.worksheets()

# Functions 
@st.cache()
# Get our worksheet names
def worksheet_names():
    sheet_names = []   
    for sheet in worksheet_list:
        sheet_names.append(sheet.title)  
    return sheet_names

# Get the sheet as dataframe
def load_the_spreadsheet(name):
    worksheet = sh.worksheet(name)
    df = DataFrame(worksheet.get_all_records())
    return df

dataframe = load_the_spreadsheet(spreadsheetname)
st.dataframe(dataframe)