import streamlit as st

def home():
    Ridwan_Darwis = '[Muh. Ridwan Darwis](https://www.linkedin.com/in/ridwandarwis)'
    Rizqi_Rivah = '[Muhamad Rizqi Rivah](https://www.linkedin.com/in/rizqirivah-7b0210272/)'

    st.subheader('Final Project Data Enthusiast')
    st.image('FP.png', caption='Meet Our Teams!', use_column_width=None)
    st.write('**Lets Connect With Our Team on Linkedin:**')
    st.markdown(Ridwan_Darwis, unsafe_allow_html=True)
    st.markdown(Rizqi_Rivah, unsafe_allow_html=True)