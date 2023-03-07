from fastapi import FastAPI, Request, Form, Depends, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from transformers import AutoConfig, pipeline
import uvicorn

app = FastAPI()

from sqlalchemy.orm import Session

import src.models as models

from src.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates/")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

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

@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

# @app.get("/")
# def home(request: Request):
#     result = 'type the beginning of the joke'
#     return templates.TemplateResponse("test_item.html", {"request": request, 'result': result})

@app.get("/generate/")
def generate(request: Request, db: Session = Depends(get_db)):
    jokes = db.query(models.JokesDB).all()
    return templates.TemplateResponse("template.html", {"request": request, "jokes_list": jokes})

# @app.post("/", response_class=HTMLResponse)
# def post_form(request: Request, some_text : str = Form(...)):
    
#     result : str = shutnik(some_text)[0]['generated_text']

#     return templates.TemplateResponse("test_item.html", {"request": request, 'result': result})

@app.post("/generate/add")
def add(request: Request, text : str = Form(...), db: Session = Depends(get_db)):

    result : str = shutnik(text)[0]['generated_text']

    new_row = models.JokesDB(input=text, output=result)

    db.add(new_row)
    db.commit()

    url = app.url_path_for("generate")
    return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)

@app.get("/delete/{joke_id}")
def delete(request: Request, joke_id: int, db: Session = Depends(get_db)):
    joke = db.query(models.JokesDB).filter(models.JokesDB.id == joke_id).first()
    db.delete(joke)
    db.commit()

    url = app.url_path_for("generate")
    return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)