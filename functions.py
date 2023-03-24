from json import dump, load
from tkinter import Text

a = 10
def readJsonFile():
    with open("data.json", "r", encoding="utf-8") as f:
        return load(f)

def writeJsonFile(data):
    finished = dump(data)
    with open ("data.json", "w") as f:
        f.write(finished)

def getTextField(field:Text):
    return field.get("1.0",'end-1c')