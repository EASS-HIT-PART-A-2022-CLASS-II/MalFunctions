from pydantic import BaseModel

class MalFunctionDto(BaseModel):
    id: int
    date: str
    description: str
    status: str

       
class Number(BaseModel):
    id: int        
    
