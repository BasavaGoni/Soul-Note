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

st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://th.bing.com/th/id/R.4e8048922a137863c3918ca6a2b83bae?rik=N82vq8qNxd%2bm8g&riu=http%3a%2f%2fwww.superiorwallpapers.com%2fdownload%2ftwo-hearts-in-a-vector-and-design-wallpaper-5120x3200.jpg&ehk=VAUWTBl0KEXvGzpLWJa0vdRcEt3zFhBJMpHQrwARJTQ%3d&risl=&pid=ImgRaw&r=0");
        background-attachment: fixed;
        background-size: cover;
    }
    .stTextArea textarea, .stTextInput input {
        text-align: left; 
    }
    label {
        text-align: left;
        float: left; 
        margin-bottom: -15px; /* Adjust this value as needed */
    }
    div.stTextInput > label, div.stTextArea > label {
        margin-top: -15px; /* Adjust this value as needed */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.header("🐦Soul Note🐦")
st.subheader("🤖 Generated a message for your love")


From = st.text_input("From")
To = st.text_input("To")
Topic = st.text_input("Topic")



if st.button("Generate"):
    tweets = tweet_chain.invoke({"From" : From, "To" : To, "Topic" : Topic})
    st.write(tweets.content)
