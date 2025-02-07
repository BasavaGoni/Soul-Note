from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import LLMChain
from langchain import PromptTemplate

import streamlit as st
import os

os.environ['GOOGLE_API_KEY'] = st.secrets['GOOGLE_API_KEY']

# Create prompt template for generating tweets

From = """
        Write a Romantic Message {From} to {To} for the topic {Topic}. It should not be long, Just 4 lines.
        It should be cute and expressive. Dont include any vulgar. Should be smiling message.
        """
msg = PromptTemplate(template = From, input_variables = ['From', 'To', 'Topic'])

# Initialize Google's Gemini model
gemini_model = ChatGoogleGenerativeAI(model = "gemini-1.5-flash-latest")

# Create LLM chain using the prompt template and model
tweet_chain = msg | gemini_model


import streamlit as st

st.header("🐦Soul Note🐦")

st.subheader("🤖 Generated a message for your love")

From = st.text_input("From")
To = st.text_input("To")
Topic = st.text_input("Topic")

if st.button("Generate"):
    tweets = tweet_chain.invoke({"From" : From, "To" : To, "Topic" : Topic})
    st.write(tweets.content)
    
import streamlit as st

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("https://th.bing.com/th/id/R.5a567e90fd0eae9cedea8fb2dab8c46c?rik=pbpkh2frp%2fRh5g&riu=http%3a%2f%2fwww.pixelstalk.net%2fwp-content%2fuploads%2f2016%2f03%2fTwo-little-red-heart-wallpaper-HD-photo.jpg&ehk=KFvG4f%2fOtOodX9Esw6gPYdv8R%2flpl%2beCWyj%2bVZEFMYE%3d&risl=&pid=ImgRaw&r=0");
        background-attachment: fixed;
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Rest of your Streamlit app code
