import streamlit as st
from pages import utils
import os, pickle

# @st.cache
def app():
    st.markdown("## Do refer to the resources provided below!")
    resources = [
        {
            "Name": "Resume-building",
            "Description": "Start building your resume with this cool templates",
            "link": "https://novoresume.com"
        },
        {
            "Name": "Aptitude",
            "Description": "Work on your Problem solving skills",
            "link": "https://www.indiabix.com/"
        },
        {
            "Name": "Courses",
            "Description": "Attend some courses to get started with your area of interests",
            "link": "https://www.udemy.com/"
        },
        {
            "Name": "Programming",
            "Description": "To get started with hands-on coding visit this link",
            "link": "https://www.hackerrank.com/"
        },
        {
            "Name": "Data Structures and Algorithms",
            "Description": "Click below link for solving DSA problems",
            "link": "http://paste/link.here"
        },
        {
            "Name": "Brainstorming Puzzles",
            "Description": "Strain your brain with this puzzles",
            "link": "https://www.geeksforgeeks.org/puzzles/"
        },
        {
            "Name": "Scholarships",
            "Description": "You can avail some scholarships to get started with various exciting technologies",
            "link": "https://www.udacity.com/scholarships"
        },

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

    

