import uvicorn
from fastapi import FastAPI
from langserve import add_routes
from geminiClient import GeminiModel
from langchain.schema.runnable import RunnableLambda

app = FastAPI()
model = GeminiModel()

add_routes(app, RunnableLambda(model.getGeminiResponseKor), path="/parse-invoice")

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)