import uvicorn
from fastapi import FastAPI
from langserve import add_routes
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

app = FastAPI(
    title="Document Parsing Server",
    version="1.0",
    decsription="A simple API Server which accepts medical invoice text as input and extracts valuable information"
)

chatllm = ChatGoogleGenerativeAI(
    model="gemini-pro",
    convert_system_message_to_human=True,
    google_api_key = "AIzaSyAhhcxJDyBeA30CUARehzj_B-466tdhBcc",
    max_retries=1,
    temperature=0.1,
    max_output_tokens=2048
)
prompt = ChatPromptTemplate.from_template("Summarize text in less than 100 words: {topic}")

add_routes(
    app,
    prompt|chatllm,
    path="/summarize"
)

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)