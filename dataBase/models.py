
from pydantic import BaseModel
from datetime import date

class MalFunction(BaseModel):
    id: int
    description: str
    creator: str
    date: date
    status: int

    
