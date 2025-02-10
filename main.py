import streamlit as st

# Minimal example with background GIF
st.markdown(
    """
    <style>
    .bg {
        background-image: url("https://media.giphy.com/media/3o7bu3XilJ5BOiSGic/giphy.gif");
        background-size: cover;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -1;
        opacity: 0.5;  /* Adjust the opacity to your preference */
    }
    .content {
        position: relative;
        z-index: 1;
    }
    </style>
    <div class="bg"></div>
    """,
    unsafe_allow_html=True
)

# Add your application inputs
st.markdown('<div class="content">', unsafe_allow_html=True)

st.header("🐦Soul Note🐦")
st.subheader("🤖 Generated a message for your love")

From = st.text_input("From")
To = st.text_input("To")
Topic = st.text_input("Topic")

if st.button("Generate"):
    # Replace this with your tweet_chain.invoke function once background is working
    st.write(f"From: {From}, To: {To}, Topic: {Topic}")

st.markdown('</div>', unsafe_allow_html=True)
