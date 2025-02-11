import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import LLMChain
from langchain import PromptTemplate

import os
os.environ['GOOGLE_API_KEY'] = st.secrets['GOOGLE_API_KEY']

# Create prompt template for generating tweets
From = """
        Write a Romantic Message {From} to {To} for the topic {Topic}. It should not be long, Just 4 lines.
        It should be cute and expressive. Don't include any vulgar. Should be a smiling message.
        """
msg = PromptTemplate(template=From, input_variables=['From', 'To', 'Topic'])

# Initialize Google's Gemini model
gemini_model = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest")

# Create LLM chain using the prompt template and model
tweet_chain = msg | gemini_model

# Streamlit App
st.header("💕Soul Note💕")
st.subheader("Crafting ❤️💛💚 Messages with 🫀 by 🤖")

From = st.text_input("From") 
To = st.text_input("To") 
Topic = st.text_input("Topic")

if st.button("Click Me"):
    tweets = tweet_chain.invoke({"From": From, "To": To, "Topic": Topic})
    st.write(tweets.content)

# Add footer with your name
footer = """
<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #f0f0f0;
    color: black;
    text-align: center;
    padding: 10px 0;
}
</style>
<div class="footer">
    <p>Created by <strong>Your Name</strong></p>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)

st.markdown(f""" """, unsafe_allow_html=True)
