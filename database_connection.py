from streamlit_gsheets import GSheetsConnection
import gspread
from google.oauth2 import service_account
import streamlit as st

def import_nutritional_database(cloud = False):
    if cloud == False:
        conn = st.connection("gsheets", type=GSheetsConnection)
        df = conn.read(worksheet="nutritional_database",
                       ttl="60m",
                       usecols=[0,1,2,3,4,5,6,7,8,9,10,11,12],
                       nrows=100)
        df.dropna(how='all', inplace = True)
        return df
    elif cloud == True:
        pass
        
#         scope = ["https://www.googleapis.com/auth/spreadsheets",
#                  "https://www.googleapis.com/auth/drive"] 
#         
#         
#         credentials = service_account.Credentials.from_service_account_info(
#             st.secrets["connections.gsheets"],
#             scopes=,)
#         conn = connect(credentials=credentials)
#         client=gspread.authorize(credentials)
#         
#         sheet_id = '1BT_p4ZjOyufPGYCMtcdahqll5imSHz1av0yE__NlP5U'
#         csv_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"
#         database_df = pd.read_csv(csv_url, on_bad_lines='skip')
#         database_df = database_df.astype(str)
#         sheet_url = st.secrets["private_gsheets_url"] #this information should be included in streamlit secret
#         sheet = client.open_by_url(sheet_url).sheet1
#         sheet.update([database_df.columns.values.tolist()] + database_df.values.tolist())
#         st.success('Data has been written to Google Sheets')
#         

def import_weight_database():
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read(worksheet="weight",
                   ttl="60m",
                   usecols=[0,1,2,3],
                   nrows=1000)
    df.dropna(how='all', inplace = True)
    return df
