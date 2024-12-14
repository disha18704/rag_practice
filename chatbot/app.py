from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama.llms import OllamaLLM
from langchain.chains import LLMChain
from langchain.schema.messages import SystemMessage, HumanMessage


import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()



# to track langsmith

os.environ["api_key_lc"] = os.getenv("api_key_lc")
os.environ["LANGCHAIN_TRACING_V2"] = "true"



# prompt = ChatPromptTemplate.from_messages(
#     [
#         SystemMessage(content = "You are a helpful assistant. Provide answers that are relevant to the query to the best of your abilities."),
#         HumanMessage(content= "Question: {question}")
#     ]
# )

# my streamlit framework
st.title("Langchain Demo With LLama3.2 API")
input_text = st.text_input("Search the topic you want")

# open ai llm call
llm = OllamaLLM(model = "llama3.2:latest")

# output_parser = StrOutputParser()

# chain

# chain = LLMChain(llm=llm)

if input_text:
    response = llm.invoke(input_text)
    st.write(response)
