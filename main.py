import streamlit as st

st.set_page_config(layout="wide")

col1,col2 = st.columns(2)

with col1:
    st.image("images/mypic2.png")


with col2:
    st.title("Somesh B R")
    content = """
    I am a Python Programmer whose interested in solving  different problems which occurs in day to day life.
    Trying to find solution in the form of code I have completed my Engineering in Cambridge Institute of Technology.
    """
    st.info(content)

content2 = """Below you can find some of the apps and 
        I have built in Python! """

st.write(content2)

