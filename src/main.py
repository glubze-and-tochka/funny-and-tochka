"""
this script run web service with reload property
"""

from fastapi import FastAPI, Request, Form, Depends, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from transformers import pipeline

import src.models as models
from src.database import SessionLocal, engine


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="src/templates/")

def get_db():
    """
    create database
    """
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()

shutnik = pipeline('text-generation',
                    model="abletobetable/gpt-short-jokes",

                    num_beams=10,
                    early_stopping=True,
                    no_repeat_ngram_size=2,
                    num_return_sequences=3, # num_means>=num_return_sequences
                    top_k=50,
                    top_p=0.95,
                    temperature=0.6,
                    # min_length=10,
                    max_length=20, #80

                    tokenizer='sberbank-ai/rugpt3small_based_on_gpt2'
                )

@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    """
    make home page and link for accessing enerator page
    """
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/generate/")
def generate(request: Request, database: Session = Depends(get_db)):
    """
    makes database query
    """
    jokes = database.query(models.JokesDB).all()
    return templates.TemplateResponse("template.html", {"request": request, "jokes_list": jokes})

@app.post("/generate/add")
def add(request: Request, text : str = Form(...), database: Session = Depends(get_db)):
    """
    generate joke and add ner row in database
    """

    result : str = shutnik(text)[0]['generated_text']

    new_row = models.JokesDB(input=text, output=result)

    database.add(new_row)
    database.commit()

    url = app.url_path_for("generate")
    return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)

@app.get("/delete/{joke_id}")
def delete(request: Request, joke_id: int, database: Session = Depends(get_db)):
    """
    delete joke from database
    """
    joke = database.query(models.JokesDB).filter(models.JokesDB.id == joke_id).first()
    database.delete(joke)
    database.commit()

    url = app.url_path_for("generate")
    return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)
