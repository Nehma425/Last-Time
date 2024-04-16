import streamlit as st
import pandas as pd
import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl
from datetime import datetime as dt
from numerize.numerize import numerize
from PIL import Image


# Set page configuration
st.set_page_config(page_title= Happy Birthday Ayah', layout='wide')

# Center-align the title using HTML
st.markdown("""
    <h1 style='text-align: center;'>Ayah's 19th Birthday</h1>
""", unsafe_allow_html=True)

# Add additional markdown content
st.markdown("Ayah is turning 19 today, and we all want to celebrate her")
st.markdown("Happy Birthday, Ayah! 🎉 Today marks another chapter in the beautiful story of your life, a story that has been filled with love, laughter, and countless memories. As you celebrate this special day, I want you to know just how incredibly proud I am to be your parent.

From the moment you came into this world, you brought boundless joy and happiness into our lives. Your kindness, creativity, and zest for life continue to inspire everyone around you. Watching you grow and flourish into the remarkable person you are today has been one of the greatest blessings of my life.

On your birthday, I hope you take a moment to reflect on all the wonderful experiences you've had and the amazing adventures that lie ahead. May this year be filled with laughter, love, and endless opportunities for you to chase your dreams and achieve greatness.

Never forget how much you are loved and cherished, not just today, but every single day. You are truly a gift, and I'm grateful for the privilege of being your parent. Happy Birthday, Ayah! Here's to another incredible year ahead! 🎂🎈")

# Define page selector
page = st.sidebar.selectbox("Aspect Selector", ["Intro page", "Early Years", "Early Teens", "Late Teens"])


# Intro page
if page == "Intro page":
    st.markdown("Happy Birthday, Ayah! 🎉 Today marks another chapter in the beautiful story of your life, a story that has been filled with love, laughter, and countless memories. As you celebrate this special day, I want you to know just how incredibly proud I am to be your parent.

From the moment you came into this world, you brought boundless joy and happiness into our lives. Your kindness, creativity, and zest for life continue to inspire everyone around you. Watching you grow and flourish into the remarkable person you are today has been one of the greatest blessings of my life.

On your birthday, I hope you take a moment to reflect on all the wonderful experiences you've had and the amazing adventures that lie ahead. May this year be filled with laughter, love, and endless opportunities for you to chase your dreams and achieve greatness.

Never forget how much you are loved and cherished, not just today, but every single day. You are truly a gift, and I'm grateful for the privilege of being your parent. Happy Birthday, Ayah! Here's to another incredible year ahead! 🎂🎈")

    myImage = Image.open("Ayah1.png")  
    st.image(myImage)
  ### #######################################
    
elif page == 'Early Years':

    myImage = Image.open("Ayah2.png")  
    st.image(myImage)
    myImage = Image.open("Ayah3.png")  
    st.image(myImage)

