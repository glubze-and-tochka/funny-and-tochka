from fastapi import Form
from pydantic import BaseModel

class MyForm(BaseModel):
    start_tokens : str

    @classmethod
    def as_form(
        cls,
        start_tokens : str = Form(...)
    ):
        return cls(    
            start_tokens = start_tokens
        )
