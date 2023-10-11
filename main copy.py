from fastapi import FastAPI, HTTPException
import random
import os
import json
from uuid import uuid4
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)

ITEMS_FILE = "itemslist.json"
ITEMS_LIST = []

#DB check json file
if os.path.exists(ITEMS_FILE) == False:
    open(ITEMS_FILE, "w") 
else:
    #print(os.stat(BOOKS_FILE).st_size)
    if os.stat(ITEMS_FILE).st_size == 0:
         with open(ITEMS_FILE, "w") as f: 
            json.dump(ITEMS_LIST, f)
    else:
        with open(ITEMS_FILE, "r") as f:
            ITMES_LIST = json.load(f) 
   
# root
# list all the books
# get book by index 
# add the book
# get random book
# delete the book
# cd Documents/Python-API/FastApi 
# uvicorn main:app --reload
# python3 -m pip install mangum

#root
# http://127.0.0.1:8000/
@app.get("/")
async def Home():
    return {"message" : "Benvindo"}

# list of the books
# http://127.0.0.1:8000/list-books
@app.get("/list-books")
async def list_books():
    #BOOKS_LIST.sort(reverse=False)
    
    return {
            "ITEMS": ITEMS_LIST
            }

#get book by index
@app.get("/get-byindex/{index}")
async def get_byindex(index: int):
    if index <0 or index >= len(ITEMS_LIST):
        raise HTTPException(404, f"Index {index} is out of range")
    else:
        return {
                "Index": index,
                "ITEM" : ITEMS_LIST[index],
                }
    
#get random book - 1
@app.get("/get-random-book")
async def get_random_book():
        x = len(ITEMS_LIST)-1
        index = random.randint(0,x)
        return {
                "Index": index,
                "Book" : ITEMS_LIST[index],
                }
#get random book - 2
@app.get("/get-random-book2")
async def get_random_book2():
        return random.choice(ITEMS_LIST)

#add the book
@app.post("/add-book")
async def add_book(title: str):
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
            #return {f"Book '{title}' exists."}
            raise HTTPException(409, f"ITEMS '{title}' exists.")
     else:
            ITEMS_LIST.append(payload)
            with open(ITEMS_FILE, "w") as f: 
                    json.dump(ITEMS_LIST, f)
     return {f"ITEM '{title}' was added."}

#update the book
@app.put("/update-book")
async def update_book(index:int, new_title:str):
     old_title = ITEMS_LIST[index]["Title"]
     ITEMS_LIST[index]["Title"] = new_title
     with open(ITEMS_FILE, "w") as f: 
        json.dump(ITEMS_LIST, f)
     return{f"Book {old_title} was updated to {new_title}"}
    
#delete the book
@app.delete("/delet-book")
async def delet_book(title: str):
     #n=0
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
          




     
                