from fastapi import FastAPI, Request, Form, Depends
from typing import Optional
from pydantic import BaseModel
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from schemas import MyForm
from enum import Enum
import uvicorn

from transformers import AutoConfig, pipeline

app = FastAPI()

templates = Jinja2Templates(directory="templates/")

@app.get("/", response_class=HTMLResponse)
def redirect_fastapi(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.get("/new_form", response_class=HTMLResponse)
def post_form(request: Request):
    result = "Type the begging of the joke"
    return templates.TemplateResponse("test_item.html", {"request": request, 'result': result})


@app.post("/new_form", response_class=HTMLResponse)
def post_form(request: Request, form_data : MyForm = Depends(MyForm.as_form)):
    # print(form_data)

    start_tokens = form_data.start_tokens

    model_folder = 'small_gpt'

    generation_config = AutoConfig.from_pretrained(f'{model_folder}/config.json')

    shutnik = pipeline('text-generation', 
                        model=model_folder,

                        num_beams=10,
                        early_stopping=True, 
                        no_repeat_ngram_size=2, 
                        num_return_sequences=3 ,   # num_means>=num_return_sequences
                        top_k=50, 
                        top_p=0.90, 
                        temperature=0.6,
                        # min_length=10,
                        max_length=20, #80

                        tokenizer='sberbank-ai/rugpt3small_based_on_gpt2',
                        config = generation_config
                    )
    
    result = shutnik(start_tokens)[0]['generated_text']

    return templates.TemplateResponse("test_item.html", {"request": request, 'result': result})