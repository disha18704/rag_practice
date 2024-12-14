import streamlit as st
import requests

def get_llm_response(input_text):
    essay_response = requests.post("http://localhost:8000/essay/invoke", json= {'input':{'topic': input_text}})
    print(essay_response.text)
    print(essay_response.status_code)  # Prints status code



    return essay_response.json()['output']



st.title('Langchain Demo with openai llama2 api')
input_text = st.text_input("Write a essay on")
# input_text1 = st.text_input("Write a poem on")

if input_text:
    st.write(get_llm_response(input_text))

