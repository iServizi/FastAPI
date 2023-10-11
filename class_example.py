import json

class Animals():
    def __init__(self, raca, peso, cor) -> None:
        self.raca = raca
        self.peso = peso
        self.cor = cor
    
    def display_animal():
        print("")

filename = "rq.txt"

#open the file and read the content
with open(filename) as f_obj:
    content = f_obj.read()

print(content)

with open(filename) as f_obj:
    for line in f_obj:
        print(line.rstrip())

#open the file and write
# filename = "rq.txt"
# with open(filename, "w") as f_obj:
#     f_obj.write("text text text text ")

# #append to the file
# filename = "rq.txt"
# with open(filename, "w") as f_obj:
#     f_obj.write("next line next line next line ")

 
#exception divioson by 0
try: 
 print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# loop until defined break
# while True:
#     x = input("Type q for quit - e")
#     if x == "q":
#         break

#write to the json file
filename = "samle.json"
list1= [1,2,3,4,5]

with open(filename, "w") as json_file:
    json.dump(list1, json_file)

#read json file
with open(filename, "r") as json_file:
    print(json.load(json_file))