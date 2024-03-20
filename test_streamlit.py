from streamlit_gsheets import GSheetsConnection

def import_nutritional_database_streamlit():
    # Create a connection object.
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read(worksheet="Foglio7")
    return df
    


