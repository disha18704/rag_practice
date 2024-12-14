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

prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessage(content="You are a helpful assistant. Provide detailed and relevant answers to the user's query."),
        HumanMessage(content="{question}")
    ]
)

# my streamlit framework
st.title("Langchain Demo With LLama3.2 API")
input_text = st.text_input("Search the topic you want")

# open ai llm call
llm = OllamaLLM(model = "llama3.2:latest")

# output_parser = StrOutputParser()

# chain

# chain = LLMChain(llm=llm)

# if input_text:
#     response = llm.invoke(input_text)
#     st.write(response)


# if input_text:
#     # Use the prompt template to format the input
#     formatted_prompt = prompt.format_messages(question=input_text)
    
#     # Generate a response using the LLM
#     response = llm.invoke(formatted_prompt)
    
#     # Display the response
#     st.write(response)

if input_text:
    # Manually construct the prompt
    manual_prompt = (
        "You are a helpful assistant. Provide detailed and relevant answers to the user's query.\n"
        f"User: {input_text}"
    )
    
    # Generate a response
    response = llm.invoke(manual_prompt)
    
    # Display the response
    st.write(response)


