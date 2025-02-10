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

st.markdown(
    """
    <style>
    .background {
        background-image: url("https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExMHFpYjRrNDI0eDJxNmNpOXMxdmNxYmxtNTV5aGZsZmh3aHFjeXBuayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/vmYEXxc5vq7Zu/giphy.gif");
        background-size: cover;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -1;
        opacity: 0.2;  /* Adjust the opacity to your preference */
    }
    .container {
        position: relative;
        z-index: 1;
    }
    </style>
    <div class="background"></div>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="container">', unsafe_allow_html=True)

st.header("🐦Soul Note🐦")
st.subheader("🤖 Generated a message for your love")

From = st.text_input("From")
To = st.text_input("To")
Topic = st.text_input("Topic")

if st.button("Generate"):
    tweets = tweet_chain.invoke({"From": From, "To": To, "Topic": Topic})
    st.write(tweets.content)

st.markdown('</div>', unsafe_allow_html=True)
