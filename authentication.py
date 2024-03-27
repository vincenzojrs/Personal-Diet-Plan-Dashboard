import streamlit as st

def authenticate(username, password):
        return (username == st.secrets["credentials"]["username"] and password == st.secrets["credentials"]["password"])

def logout():
    st.session_state.logged_in = False
    st.rerun()

def create_form():
        with st.sidebar:
                with st.form(key = 'Log-in form', clear_on_submit = True):
                        username = st.text_input("Username")
                        password = st.text_input("Password", type="password")
                        if st.form_submit_button("Login"):
                                if authenticate(username, password):
                                        st.success("Login riuscito!")
                                        st.session_state.logged_in = True
                                else:
                                        st.error("Credenziali non valide")

def logout_button():
        with st.sidebar:
                if st.session_state.get('logged_in'):
                        if st.button("Logout"):
                                logout()


