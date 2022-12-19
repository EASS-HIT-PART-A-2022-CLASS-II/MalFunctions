from pydantic import BaseModel

class MalFunctionDto(BaseModel):
    id: int
    date: str
    description: str
    status: str

    def __init__(self,id_int,date_int,description_int,status_int):
        super().__init__(id=id_int,date=date_int,description=description_int,status=status_int)



    
