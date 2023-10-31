import streamlit as st
from Home import home
from main import predict_page, tab



def explore():
    selection = st.sidebar.selectbox(
        ":Yellow[What do you want to know about my project?]",
        ("Home","Make predictions"),
    )
    return selection


if __name__ == "__main__":
    ok = explore()

    if ok == "Make predictions":
        predict_page()
    else:
        home()

    tab()
