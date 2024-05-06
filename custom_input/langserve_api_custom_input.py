'''
This file shows how to use custom input to call your llm model. Here I have targeted a specific use case - Medical Invoice Parsing
The kor schema defines the different entities we want to extract from a medical Invoice, which is used by gemini. The input is the raw text 
collected from invoice post OCR
'''

import uvicorn
from fastapi import FastAPI
from langserve import add_routes
from geminiClient import GeminiModel
from langchain.schema.runnable import RunnableLambda

# defining app and model
app = FastAPI()
model = GeminiModel()

'''
Again calling by routes method but this time using RunnableLambda
RunnableLambda converts a python callable into a Runnable. Wrapping a callable in a RunnableLambda makes the callable usable 
within either a sync or async context. 

Pass your function to RunnableLambda and define your route
'''
add_routes(app, RunnableLambda(model.getGeminiResponseKor), path="/parse-invoice")

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)
