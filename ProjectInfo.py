import streamlit as st

st.header('List of Missing Data Per Project No')
col1 , col2 ,col3= st.columns(3)
with st.container():
    
    with col1:
        st.subheader('Missing Data Titles')
    with col2:
        st.subheader('ShareButtons')
    with col3:
        st.subheader('Encryption Buttons')
st.write('outside') 