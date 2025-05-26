
import streamlit as st
from openai import OpenAI
import os

# Password protection
password = st.text_input("Enter password to continue:", type="password")
if password != "priyav@1983!":
    st.warning("Incorrect password.")
    st.stop()

st.title("Vivek Leadership Coach 🧠")
st.markdown("Now trained on 75+ leadership and CEO books.")

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
