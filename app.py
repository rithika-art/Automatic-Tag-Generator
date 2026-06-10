import streamlit as st

st.set_page_config(page_title="Automatic Tag Generator")

st.title("🔐 Login Page")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):

    if username == "admin" and password == "admin123":
        st.success("Login Successful!")
        st.balloons()

        st.title("🏷️ Dashboard")
        st.write("Welcome to Automatic Tag Generator")

    else:
        st.error("Invalid Username or Password")