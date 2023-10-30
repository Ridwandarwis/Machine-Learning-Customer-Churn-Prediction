import streamlit as st

def home():
    Ridwan_Darwis = '[Muh. Ridwan Darwis](https://www.linkedin.com/in/ridwandarwis)'

    st.subheader('Customer Churn Analysis')
    st.image('FP.png', caption='Muh. Ridwan Darwis', use_column_width=None)
    st.write('**Lets Connect With me on Linkedin:**')
    st.markdown(Ridwan_Darwis, unsafe_allow_html=True)
