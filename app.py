import streamlit as st

from auth import validate_signup
from database import add_user, check_user, create_table
from pages_dashboard import show_dashboard

st.set_page_config(page_title="Pakistan House Price Prediction")

create_table()

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user = ""


def show_signup():
    st.title("Signup")
    username = st.text_input("Username", key="su_username")
    email = st.text_input("Email", key="su_email")
    password = st.text_input("Password", type="password", key="su_password")
    confirm = st.text_input("Confirm password", type="password", key="su_confirm")

    if st.button("Create account"):
        error = validate_signup(username.strip(), email.strip(), password, confirm)
        if error:
            st.error(error)
        elif add_user(username.strip(), email.strip(), password):
            st.success("Account created. Now open the Login page.")
        else:
            st.error("This username or email already exists.")


def show_login():
    st.title("Login")
    username = st.text_input("Username", key="li_username")
    password = st.text_input("Password", type="password", key="li_password")

    if st.button("Login"):
        if not username.strip() or not password:
            st.error("Please enter your username and password.")
        elif check_user(username.strip(), password):
            st.session_state.logged_in = True
            st.session_state.user = username.strip()
            st.rerun()
        else:
            st.error("Wrong username or password.")


if not st.session_state.logged_in:
    choice = st.sidebar.radio("Account", ["Login", "Signup"])
    if choice == "Signup":
        show_signup()
    else:
        show_login()
else:
    st.sidebar.write(f"Hello, {st.session_state.user}")
    page = st.sidebar.radio("Menu", ["Home", "Data Overview", "Prediction"])
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.user = ""
        st.rerun()
    show_dashboard(page)