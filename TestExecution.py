
import tkinter as tk
from GlobalVars import defaultFont
import functions as func

root:tk.Tk
index:int = -1

quest_lable:tk.Label
doneButton:tk.Button
write:tk.Text
options:list = []

default_font:tuple = defaultFont

testInfo:object
curTask:object
curTaskIndex:int = 0
answerType:str = ""
right_answer = None
right_answer_index:int

answers:list = []
def curTaskUpdate():
    global curTask
    curTask = testInfo['questions'][curTaskIndex]


def AnswerOne():
    if (right_answer_index == 0):
        print("right")
    else:
        print("wrong")

def AnswerTwo():
    if (right_answer_index == 1):
        print("right")
    else:
        print("wrong")
    
def AnswerThree():
    if (right_answer_index == 2):
        print("right")
    else:
        print("wrong")


def UpdateData():
    global right_answer
    global quest_lable
    global answerType
    global right_answer_index

    curTaskUpdate()
    answerType = curTask["answer_type"]
    if (answerType == "write"):
        right_answer = curTask["right_answer"]
    else:
        right_answer_index = curTask["right_answer_index"]
    quest_lable.config(text=curTask['question_text'])

def showOptions():
    global options
    amount:int = len(curTask['answerOptions'])
    match amount:
        case 2:
            options.append(tk.Button(text=curTask["answerOptions"][0], font=default_font, command=AnswerOne))
            options.append(tk.Button(text=curTask["answerOptions"][1], font=default_font, command=AnswerTwo))
            options[0].place(x=0, y=200, width=100,height=50)
            options[1].place(x=100, y=200, width=100,height=50)

        case 3:
            options.append(tk.Button(text=curTask["answerOptions"][0], font=default_font, command=AnswerOne))
            options.append(tk.Button(text=curTask["answerOptions"][1], font=default_font, command=AnswerTwo))
            options.append(tk.Button(text=curTask["answerOptions"][2], font=default_font, command=AnswerThree))
            options[0].place(x=0, y=200, width=100,height=50)
            options[1].place(x=100, y=200, width=100,height=50)
            options[2].place(x=200, y=200, width=100,height=50)

    
def showWrite():
    global write
    write = tk.Text(font=default_font, width=200, height=100)
    write.place(x=100, y=200, width=200, height=100)
    print("but it does")

def showOptionsOrWrite():
    global options
    global write
    if (answerType == "write"):
        print("write")
        showWrite()
        try:
            options[0].destroy()
            options[1].destroy()
        except NameError:
            pass
    else:
        print("opt")
        try:
            write.destroy()
        except NameError:
            pass
        showOptions()

def nextTask():
    global curTaskIndex
    curTaskIndex += 1
    UpdateData()
    showOptionsOrWrite()


def Start(AgrRoot:tk.Tk, AgrIndex:int, objToDelete):
    objToDelete.destroy()

    global root
    global index
    global testInfo
    global curTask
    global curTaskIndex

    global doneButton

    global quest_lable

    root = AgrRoot
    index = AgrIndex

    testInfo = func.readJsonFile()[index]

    curTask = testInfo["questions"][curTaskIndex]

    doneButton = tk.Button(font=default_font, text=u"Готово", command=nextTask)
    doneButton.place(x=156, y=350)

    quest_lable = tk.Label(text="null", font=("Comic Sans MS", 30))
    quest_lable.place(x=156, y=30)


    UpdateData()
    showOptionsOrWrite()

"""
curQuestIndex:int = 0
testInfo:object = func.readJsonFile()[index]
curQuest:object = testInfo['questions'][curQuestIndex]
questAmount:int = len(testInfo['questions'])


def UpdateCurQuest():
    global curQuest
    curQuest = {"Hello":"how are you"}

UpdateCurQuest() """