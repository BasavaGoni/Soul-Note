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

st.header("💕Soul Note💕")

st.subheader("Crafting ❤️💛💚 Messages with 🫀 by 🤖")

From = st.text_input("From") 
To = st.text_input("To") 
Topic = st.text_input("Topic")

if st.button("Spark"):
        tweets = tweet_chain.invoke({"From" : From, "To" : To, "Topic" : Topic})
        st.write(tweets.content)

import streamlit as st

st.markdown( f""" """, unsafe_allow_html=True )
