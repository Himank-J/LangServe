'''
This is the minimal and simplest method of using your LLM models with LangServe
The key point here is to understand that with just 20-30 lines of code you have created an API
that is powered by a LLM model, which is the power of LangServe
'''

# imports
import uvicorn
from fastapi import FastAPI
from langserve import add_routes
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

# defining app
app = FastAPI(
    title="Document Parsing Server",
    version="1.0",
    decsription="A simple API Server which accepts medical invoice text as input and extracts valuable information"
)

# llm model 
chatllm = ChatGoogleGenerativeAI(
    model="gemini-pro",
    convert_system_message_to_human=True,
    google_api_key = "<key here>", # input your gemini key
    max_retries=1,
    temperature=0.1,
    max_output_tokens=2048
)

# basic prompt template for summarisation
prompt = ChatPromptTemplate.from_template("Summarize text in less than 100 words: {topic}")

# defining API route - equivalent to POST request at localhost:8000/summarize/invoke
add_routes(
    app,
    prompt|chatllm,
    path="/summarize"
)

# running my server using uvicorn
if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)
