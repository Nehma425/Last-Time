import streamlit as st
from PIL import Image

# Set page configuration
st.set_page_config(page_title='Happy Birthday Ayah', layout='wide')

# Center-align the title using HTML
st.markdown("""
    <h1 style='text-align: center;'>Ayah's 19th Birthday</h1>
""", unsafe_allow_html=True)

# Define page selector
page = st.sidebar.selectbox("Aspect Selector", ["Intro page", "Early Years", "Early Teens", "Late Teens"])

# Intro page
if page == "Intro page":
    st.markdown("Happy Birthday, Ayah!")
    st.markdown("Ayah is turning 19 today, and we all want to celebrate her")
    st.markdown("Happy Birthday, Ayah! 🎉 Today marks another chapter in the beautiful story of your life, a story that has been filled with love, laughter, and countless memories. As you celebrate this special day, I want you to know just how incredibly proud I am to be your parent.")

    st.markdown("From the moment you came into this world, you brought boundless joy and happiness into our lives. Your kindness, creativity, and zest for life continue to inspire everyone around you. Watching you grow and flourish into the remarkable person you are today has been one of the greatest blessings of my life.")

    st.markdown("On your birthday, I hope you take a moment to reflect on all the wonderful experiences you've had and the amazing adventures that lie ahead. May this year be filled with laughter, love, and endless opportunities for you to chase your dreams and achieve greatness.")

    st.markdown("Never forget how much you are loved and cherished, not just today, but every single day. You are truly a gift, and I'm grateful for the privilege of being your parent. Happy Birthday, Ayah! Here's to another incredible year ahead! 🎂🎈")
    myImage = Image.open("Ayah0.jpg")  
    st.image(myImage)
### #######################################
    
elif page == 'Early Years':
    st.markdown("Looking back on your early years, Ayah, I'm filled with nostalgia and gratitude for all the precious moments we've shared. From your first steps to your first words, every milestone has been a joy to witness. As you celebrate your 19th birthday, know that you're surrounded by love and support every step of the way. Happy Birthday, Ayah! 🎂🎉")
    myImage = Image.opem("Ayah1.jpg")
    st.image(myImage)
    myImage = Image.open("Ayah2.jpg")  
    st.image(myImage)
    myImage = Image.open("Ayah3.jpg")  
    st.image(myImage)
    myImage = Image.open("Ayah4.jpg")  
    st.image(myImage)

elif page == 'Early Teens':
    st.markdown("As you enter your early teens, Ayah, I want you to know how much you've grown and matured over the years. Your journey from childhood to adolescence has been filled with remarkable milestones and achievements. I'm so proud of the person you're becoming, and I can't wait to see what the future holds for you. Happy Birthday, Ayah! 🎂🌟")
    myImage = Image.open("Ayah8.jpg")  
    myImage = Image.open("ayah9.JPG")  
    st.image(myImage)
    myImage = Image.open("ayahmom.JPG")  
    st.image(myImage)
    myImage = Image.open("ayaybro.JPG")  
    st.image(myImage)
elif page == 'Late Teens':
    st.markdown("In your late teens now, Ayah, you stand on the brink of adulthood, ready to embark on new adventures and challenges. As you navigate this exciting phase of your life, remember to stay true to yourself and follow your heart. Your resilience and determination inspire us all, and I have no doubt that you'll achieve great things. Happy Birthday, Ayah! 🎈🌟")
    myImage = Image.open("Ayah5.jpg")  
    st.image(myImage)
    myImage = Image.open("Ayah6.jpg")  
    st.image(myImage)
    myImage = Image.open("Ayah7.jpg")  
    st.image(myImage)
