# our data
data = [
    {"name": "Ravi", 
     "age": 45,
    "location": "Delhi"},

    {"name": "Amit", 
     "age": 30,
     "location": "Mumbai"},
   
]
 
# open file in write mode
with open("data.txt", "w") as f:
    # for person in data:
    #     f.write(f"Name: {person['name']}, Age: {person['age']}, Location: {person['location']}\n")
    for person in data:
        for key,value in person.items():
            f.write(f"{key}:{value}\n")
        f.write("\n")
