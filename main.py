from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import LLMChain
from langchain import PromptTemplate

import streamlit as st
import os
import time        

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

st.markdown( f""" """, unsafe_allow_html=True )

gif_url = "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExd2M4dGVkNzF1ODJ5bzVhcHdsY3F6dzdrNXo5MDBhdG90d281c25jZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3oKIP6jXimEmTmGyIw/giphy.gif"  # Replace with your GIF URL

def display_gif(gif_url):
    st.markdown(f'<img src="{gif_url}" width="200">', unsafe_allow_html=True)

def hide_gif():
    st.empty()  # Clear the previous GIF display

display_time = 2  # Display GIF for 2 seconds
hide_time = 2  # Hide GIF for 2 seconds

start_time = time.time()

while True:
    elapsed_time = time.time() - start_time

    if elapsed_time % (display_time + hide_time) < display_time:
        display_gif(gif_url)
    else:
        hide_gif()

    time.sleep(0.1)  # Small delay to prevent excessive CPU usage

