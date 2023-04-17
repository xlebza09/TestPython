import functions as func
from datetime import datetime as dt
def CreatePupil():
    data:list = func.readJsonFile("pupils.json")
    full = input("Введите имя и фамилию, разделяя их пробелами\n")
    name:str =""
    surname:str = ""
    space_index:int
    for i in range(len(full)):
        if (full[i] == " "):
            space_index = i
            break

    for i in range(space_index):
        name += full[i]
    
    for i in range(space_index + 1, len(full)):
        surname += full[i]

    for i in range(len(data)):
        if (name == data[i]['name'] and surname == data[i]['name']):
            print("В системе уже есть такой ученик.")
            CreatePupil()

    pupil_structure:object = {"name": name, "surname": surname, "completedTests":[]}

    data.append(pupil_structure)
    func.writeJsonFile(data, "pupils.json")

def getDate():
    full = dt.now()
    months:list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    second = full.second
    minute = full.minute
    hour = full.hour
    day = full.day
    month = full.month
    str_month = months[month - 1]
    year = full.year
    return {"second":second, "minute":minute, "hour":hour, "day":day, "month":str_month, "year":year}

# date = getDate()
# print(f"It's {date['hour']}:{date['minute']}:{date['second']} of {date['day']} {date['month']}")