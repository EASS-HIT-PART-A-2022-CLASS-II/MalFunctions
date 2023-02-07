import mysql.connector
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json


from models import MalFunction

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
        cnx = mysql.connector.connect(user='root', password='1542',host='mysql_service')
        cursor = cnx.cursor()
        return cursor,cnx
    except Exception as e:
        return "Failed to create connection Error: {0}".format(e)




def createDB():
    cursor,cnx = conn()
    cursor.execute("CREATE DATABASE malfunctions")
    cnx = mysql.connector.connect(user='root', password='1542',host='mysql_service',database='malfunctions')
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
    cnx = mysql.connector.connect(user='root', password='1542',host='mysql_service',database='malfunctions')
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
async def addMal(mal: MalFunction):
    cursor,cnx = conn()
    cnx = mysql.connector.connect(user='root', password='1542',host='mysql_service',database='malfunctions')
    cursor = cnx.cursor()
    cursor.execute(f'''
    INSERT INTO `malfunctions`.`list` (`description`, `created_by`, `date`, `status`) VALUES ('{mal.description}', '{mal.creator}', '{mal.date}', '{mal.status}');
     ''')
    cnx.commit()
    return "Added"

@app.delete("/delMal/{id}")
async def delMal(id : int):
    cursor,cnx = conn()
    cnx = mysql.connector.connect(user='root', password='1542',host='mysql_service',database='malfunctions')
    cursor = cnx.cursor()
    cursor.execute(
           f'''
           DELETE FROM list WHERE id = {id}
           ''' 
        )
    cnx.commit()
    return "Removed"

@app.post("/editMal")
async def editMal(mal: MalFunction):
    cursor,cnx = conn()
    cnx = mysql.connector.connect(user='root', password='1542',host='mysql_service',database='malfunctions')
    cursor = cnx.cursor()
    cursor.execute(
            f'''
            UPDATE `malfunctions`.`list` SET `description` = '{mal.description}',
             `created_by` = '{mal.creator}',
              `date` = '{mal.date}',
               `status` = '{mal.status}' 
               WHERE (`id` = '{mal.id}');
            '''
        )
    cnx.commit()
    return "Edited"








