import streamlit as st

st.set_page_config(page_title="Automatic Tag Generator")

# Login Page
st.title("🔐 Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):

    st.success("Login Successful!")

    st.title("🏷️ Dashboard")

    st.metric("Total Inputs", "120")
    st.metric("Generated Tags", "850")

    st.subheader("Quick Actions")

    st.button("Generate New Tags")
    st.button("View History")
    st.button("Export Tags")