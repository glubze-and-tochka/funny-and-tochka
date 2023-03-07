from sqlalchemy import Boolean, Column, Integer, String

from src.database import Base 

class JokesDB(Base):
    __tablename__ = "generates"

    id = Column(Integer, primary_key=True, index=True)
    input = Column(String)
    output = Column(String)