from fastapi import FastAPI, HTTPException
import random
import os
import json
from uuid import uuid4
from mangum import Mangum
#from pydantic import BaseModel

app = FastAPI()
handler = Mangum(app)

ITEMS_FILE = "itemslist.json"
ITEMS_LIST = []

#DB check json file
if os.path.exists(ITEMS_FILE) == False:
    open(ITEMS_FILE, "w") 
else:
    if os.stat(ITEMS_FILE).st_size == 0:
         with open(ITEMS_FILE, "w") as f: 
            json.dump(ITEMS_LIST, f)
    else:
        with open(ITEMS_FILE, "r") as f:
            ITEMS_LIST = json.load(f) 
   
# root
# list all the ITEMS
# get ITEM by index zip la
# add the ITEM
# get random ITEM
# delete the ITEM
# cd Documents/Python-API/FastApi 
# uvicorn main:app --reload
# python3 -m pip install mangum

#root
# local http://127.0.0.1:8000/
@app.get("/")
async def Home():
    return {"message" : "Benvindo"}

# list of the items
# local http://127.0.0.1:8000/list-items
@app.get("/list-items")
async def list_items():
    return {
            "ITEMS": ITEMS_LIST
            }

#get item by index
@app.get("/get-byindex/{index}")
async def get_byindex(index: int):
    if index <0 or index >= len(ITEMS_LIST):
        raise HTTPException(404, f"Index {index} is out of range")
    else:
        return {
                "Index": index,
                "ITEM" : ITEMS_LIST[index],
                }
    
#get random item - 1
@app.get("/get-random-item")
async def get_random_item():
        x = len(ITEMS_LIST)-1
        index = random.randint(0,x)
        return {
                "Index": index,
                "Item" : ITEMS_LIST[index],
                }
#get random item - 2
@app.get("/get-random-item2")
async def get_random_item2():
        return random.choice(ITEMS_LIST)

#add the item
@app.post("/add-item")
async def add_item(title: str):
     ID_ITEM = uuid4().hex
     payload = { "Title" : title,
                "ID" : ID_ITEM,
                "type": "animals",
                }
     controler = 0
     for i in range(len(ITEMS_LIST)): 
          if ITEMS_LIST[i]["Title"] == title:
             controler = controler +1

     if controler > 0:
            raise HTTPException(409, f"ITEMS '{title}' exists.")
     else:
            ITEMS_LIST.append(payload)
            with open(ITEMS_FILE, "w") as f: 
                    json.dump(ITEMS_LIST, f)
     return {f"ITEM '{title}' was added."}

#update the item
@app.put("/update-item")
async def update_item(index:int, new_title:str):
     old_title = ITEMS_LIST[index]["Title"]
     ITEMS_LIST[index]["Title"] = new_title
     with open(ITEMS_FILE, "w") as f: 
        json.dump(ITEMS_LIST, f)
     return{f"Item {old_title} was updated to {new_title}"}
    
#delete the item
@app.delete("/delet-item")
async def delet_item(title: str):
     controler_del = 0
     for n in range(len(ITEMS_LIST)):
        if(ITEMS_LIST[n]["Title"] == title):
            del ITEMS_LIST[n]
            controler_del=controler_del+1
            with open(ITEMS_FILE, "w") as f: 
                json.dump(ITEMS_LIST, f)
            return {f"ITEM {title} was removed"}
     if controler_del == 0:
          return {f"ITEM {title} doesn't exist."}
          




     
                