import os
import streamlit as st
import numpy as np
from PIL import  Image

# Custom imports 
from multipage import MultiPage
from pages import admin_login, predictor, learning_resources # import your pages here

# Create an instance of the app 
app = MultiPage()

# Title of the main page
display = Image.open('Logo.png')
display = np.array(display)
col1, col2 = st.columns(2)
col1.image(display, width = 200)
col2.title("Placement Predictor Application")

# Add all your application here
app.add_page("Placement Predictor", predictor.app)
app.add_page("Admin Section",admin_login.app)
app.add_page("Learning Resources", learning_resources.app)

# The main app
app.run()
