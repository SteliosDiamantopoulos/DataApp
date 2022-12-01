import streamlit as st
import pandas as pd

@st.experimental_memo
def load_data():
    DB=pd.read_excel('OpenIssuesDataBase.xlsx')
    return (DB)



st.checkbox("Use container width", value=False, key="use_container_width")
df = load_data()
st.dataframe(df, use_container_width=st.session_state.use_container_width)