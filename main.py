# from schemas import MyForm
from enum import Enum
from typing import Optional

import uvicorn
from fastapi import Depends, FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from transformers import AutoConfig, pipeline

app = FastAPI()

templates = Jinja2Templates(directory="templates/")

shutnik = pipeline('text-generation', 
                    model="abletobetable/gpt-short-jokes",

                    num_beams=10,
                    early_stopping=True, 
                    no_repeat_ngram_size=2, 
                    num_return_sequences=3 ,   # num_means>=num_return_sequences
                    top_k=50, 
                    top_p=0.95, 
                    temperature=0.6,
                    # min_length=10,
                    max_length=20, #80

                    tokenizer='sberbank-ai/rugpt3small_based_on_gpt2'
                )


@app.get("/")
def home(request: Request):
    result = 'type the beginning of the joke'
    return templates.TemplateResponse("test_item.html", {"request": request, 'result': result})



@app.post("/", response_class=HTMLResponse)
def post_form(request: Request, some_text : str = Form(...)):
    
    result : str = shutnik(some_text)[0]['generated_text']

    return templates.TemplateResponse("test_item.html", {"request": request, 'result': result})
