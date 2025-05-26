
import streamlit as st
from openai import OpenAI
import os

# Password protection
password = st.text_input("Enter password to continue:", type="password")
if password != "priyav@1983!":
    st.warning("Incorrect password.")
    st.stop()

# Branding header
st.image("https://i.imgur.com/M7o9m0B.png", use_container_width=True)
st.markdown("## 🧠 Vivek Leadership Coach")
st.markdown("**Your personalized leadership AI – trained on 75+ books including biographies, strategy, and emotional intelligence.**")
st.markdown("---")

# Chat setup
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

query = st.text_input("Ask your leadership question:")
submit = st.button("Submit")

if submit and query:
    st.markdown("Generating answer from Vivek's RAG library...")
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a leadership coach trained on 75+ books, including biographies and strategy classics."},
            {"role": "user", "content": f"{query}"}
        ]
    )
    answer = response.choices[0].message.content
    st.markdown("### Answer")
    st.write(answer)
