import mysql.connector
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import date




class MalFunctionDto(BaseModel):
    id: int
    description: str
    creator: str
    date: date
    status: int


app = FastAPI()

origins = [
    "http://localhost:8081",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def conn():
    try:
        cnx = mysql.connector.connect(user='root', password='1542',host='mysql')
        cursor = cnx.cursor()
        return cursor,cnx
    except Exception as e:
        return "Failed to create connection Error: {0}".format(e)




def createDB():
    cursor,cnx = conn()
    cursor.execute("CREATE DATABASE malfunctions")
    cnx = mysql.connector.connect(user='root', password='1542',host='mysql',database='malfunctions')
    cursor = cnx.cursor()
    cursor.execute('''
        CREATE TABLE `malfunctions`.`list` (
        `id` INT NOT NULL AUTO_INCREMENT,
        `description` VARCHAR(45) NOT NULL,
        `created_by` VARCHAR(45) NOT NULL,
        `date` DATETIME NOT NULL,
        `status` INT NOT NULL,
        PRIMARY KEY (`id`));
    ''')

    
    cursor.close()
    cnx.close()


def database_exists():
    try:
        cursor,cnx = conn()
        cursor.execute("SHOW DATABASES")
        databases = [row[0] for row in cursor]

        if 'malfunctions' in databases:
            return True
        else:
            return False
    except mysql.connector.Error as err:
        print("Error: {}".format(err))
    finally:
        cursor.close()
        cnx.close()


@app.get("/check")
def check():
    if database_exists():
        return "exists"
    else:
        #create the db because it doesn't exists
        createDB()
        return "created"


@app.get("/getList")
def getList():
    cursor,cnx = conn()
    cnx = mysql.connector.connect(user='root', password='1542',host='mysql',database='malfunctions')
    cursor = cnx.cursor()

    query = 'SELECT * FROM list'
    cursor.execute(query)
    result=[]
    for row in cursor:
        result.append({
            'id': row[0],
            'description': row[1],
            'creator': row[2],
            'date': row[3],
            'status': row[4]
        })

    cursor.close()
    cnx.close()

    return result

@app.post("/addMal")
async def addMal(mal: MalFunctionDto):
    cursor,cnx = conn()
    cnx = mysql.connector.connect(user='root', password='1542',host='mysql',database='malfunctions')
    cursor = cnx.cursor()
    cursor.execute(f'''
    INSERT INTO `malfunctions`.`list` (`description`, `created_by`, `date`, `status`) VALUES ('{mal.description}', '{mal.creator}', '{mal.date}', '{mal.status}');
     ''')
    cnx.commit()
    return mal









# @app.get("/ReadData")
# def ReadData():
#     cursor,cnx = conn()
#     query = 'SELECT * FROM sys_config'
#     cursor.execute(query)
#     result = []
# # Print the results
#     for row in cursor:
#         print(row)
#         result.append(str(row))

# #   Close the cursor and connection
#     cursor.close()
#     cnx.close()

#     return result



