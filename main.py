import streamlit as st
import pandas

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

df = pandas.read_csv("data.csv", sep=";") # This function used to read the csv file in which can access data in rows

col3,col4 = st.columns(2)

with col3:  # This is used to display the header for 1st 10 items from Excel.
    for index, row in df[:10].iterrows(): # Iterrows is method which gives access to rows which can iterate over the rows.
        st.header(row['title'])

with col4: # This is used to display the header for next  10 items from  Excel.
    for index, row in df[:10].iterrows():
        st.header(row['title'])

