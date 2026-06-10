import streamlit as st

st.set_page_config(page_title="Automatic Tag Generator")

page = st.sidebar.selectbox(
    "Navigation",
    ["Login", "Dashboard", "Tag Generator"]
)

if page == "Login":

    st.title("🔐 Login")

    st.text_input("Username")
    st.text_input("Password", type="password")

    st.button("Login")

elif page == "Dashboard":

    st.title("🏷️ Dashboard")

    st.metric("Total Inputs", "120")
    st.metric("Generated Tags", "850")

elif page == "Tag Generator":

    st.title("🏷️ Tag Generator")

    text = st.text_area("Enter Text")

    st.button("Generate Tags")