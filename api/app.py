from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes
import uvicorn
import os 
from langchain.chains import LLMChain
from langchain_ollama.llms import OllamaLLM
from dotenv import load_dotenv


load_dotenv()

app = FastAPI(
    title = "Langchain Server",
    version = "1.0",
    description= "A Simple API Server"
)



llm = OllamaLLM(model= "llama2")

prompt1 = ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words.")
prompt2 = ChatPromptTemplate.from_template("Write me a poem about {topic} for a 5 year old child.")

essay_chain = prompt1|llm
poem_chain = prompt2|llm


add_routes(
    app,
    runnable=essay_chain,
    path = "/essay"
)

add_routes(
    app,
    runnable=poem_chain,
    path = "/poem"
)


if __name__ == "__main__":
    uvicorn.run(app,host="localhost",port=8000)

