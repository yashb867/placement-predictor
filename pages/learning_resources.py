import streamlit as st
from pages import utils
import os, pickle

# @st.cache
def app():
    st.markdown("## Please refer to the study material provided below!")
    resources = [
        {
            "Name": "Name of topic",
            "Description": "Description about topic",
            "link": "http://paste/link.here"
        },
        {
            "Name": "Name of topic",
            "Description": "Description about topic",
            "link": "http://paste/link.here"
        },
        {
            "Name": "Name of topic",
            "Description": "Description about topic",
            "link": "http://paste/link.here"
        }
    ]
    st.markdown("""---""")
    counter = 1
    for i in resources:
        with st.container():
            st.header(str(counter) + '. ' + i['Name'])
            st.caption(i['Description'])
            st.write(i['link'])
        st.markdown("""---""")
        counter += 1

    

