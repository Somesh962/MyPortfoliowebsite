import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1,col2 = st.columns(2)

with col1:
    st.image("images/mypic2.png",width=450)


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

col3,empty_col,col4 = st.columns([1.5,0.5,1.5])

with col3:  # This is used to display the header for 1st 10 items from Excel.
    for index, row in df[:10].iterrows(): # Iterrows is method which gives access to rows which can iterate over the rows.
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f"[Source Code]({row['url']})")

with col4: # This is used to display the header for next  10 items from  Excel.
    for index, row in df[10:].iterrows():
        st.header(row['title'])     # This method is used to display the header
        st.write(row['description']) # This method is used to display the description
        st.image("images/" + row['image']) # This method is used to display the image.
        st.write(f"[Source Code]({row['url']})")  # To call it dynamically from Github, we can use the fstring

