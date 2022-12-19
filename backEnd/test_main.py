from main import BackEnd
from models import *

def test_backend_functions():
    x = BackEnd.getMalfuntionList()
    assert x == "call malfunction service and get back list of all malfunctions" 

    x = BackEnd.removeMalFunction(5)
    assert x == "send id for remove from DB by malfunction service" 

    #MalFunction = MalFunctionDto(id=1,date="20/12/22",description="fix toilet",status="completed")
    MalFunction = MalFunctionDto(1,"20/12/22","fix toilet","completed")   
    assert MalFunction.id == 1
    assert MalFunction.date == "20/12/22"
    assert MalFunction.description == "fix toilet"
    assert MalFunction.status == "completed"
    x = BackEnd.updateMalFunction(MalFunction)
    assert x == "send updated malfunction to malfunction service for update" 

    x = BackEnd.addMalFunction(MalFunction)
    assert x == "send new dto for register in DB" 

