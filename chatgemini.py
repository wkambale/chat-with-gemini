from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

load_dotenv(".env")

fetched_api_key = os.getenv("API_KEY")
genai.configure(api_key = fetched_api_key)

model = genai.GenerativeModel("gemini-1.5-pro-latest") 
chat = model.start_chat()

def LLM_Response(question):
    response = chat.send_message(question,stream=True)
    return response

st.title("Taxman Bot")

user_quest = st.text_input("Ask a questions on tax:")
btn = st.button("Ask...")

if btn and user_quest:
    result = LLM_Response(user_quest)
    st.subheader("Response: ")
    for word in result:
        st.text(word.text)