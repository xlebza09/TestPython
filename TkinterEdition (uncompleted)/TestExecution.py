
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
answers:list
back:tk.Button


answers:list = []
def curTaskUpdate():
    global curTask
    curTask = testInfo['questions'][curTaskIndex]


def AnswerOne():
    global answers
    answers.append(right_answer_index == 0)
    nextTask()

def AnswerTwo():
    global answers
    answers.append(right_answer_index == 1)
    nextTask()
    
def AnswerThree():
    global answers
    answers.append(right_answer_index == 2)
    nextTask()

def AnswerFour():
    global answers
    answers.append(right_answer_index == 3)
    nextTask()


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
        print(curTask['right_answer_index'])
        right_answer_index = curTask['right_answer_index']
    quest_lable.config(text=curTask['question_text'])

def showOptions():
    global options
    global doneButton
    options.append(tk.Button)
    options.append(tk.Button)
    options.append(tk.Button)
    options.append(tk.Button)
    amount:int = len(curTask['answerOptions'])
    try:
        doneButton.destroy()
    except NameError:
        pass
    
    match amount:
        case 2:
            options[0] = tk.Button(root, text=curTask["answerOptions"][0], font=default_font, command=AnswerOne)
            options[1] = tk.Button(root, text=curTask["answerOptions"][1], font=default_font, command=AnswerTwo)
            options[0].place(x=0, y=200, width=100,height=200)
            options[1].place(x=100, y=200, width=100,height=200)

        case 3:
            options[0] = tk.Button(root, text=curTask["answerOptions"][0], font=default_font, command=AnswerOne)
            options[1] = tk.Button(root, text=curTask["answerOptions"][1], font=default_font, command=AnswerTwo)
            options[2] = tk.Button(root, text=curTask["answerOptions"][2], font=default_font, command=AnswerThree)
            options[0].place(x=10, y=200, width=150,height=200)
            options[1].place(x=160, y=200, width=150,height=200)
            options[2].place(x=310, y=200, width=125,height=200)

        case 4:
            options[0] = tk.Button(root, text=curTask["answerOptions"][0], font=default_font, command=AnswerOne, wraplength=110, justify="left")
            options[1] = tk.Button(root, text=curTask["answerOptions"][1], font=default_font, command=AnswerTwo, wraplength=110, justify="left")
            options[2] = tk.Button(root, text=curTask["answerOptions"][2], font=default_font, command=AnswerThree, wraplength=110, justify="left")
            options[3] = tk.Button(root, text=curTask["answerOptions"][3], font=default_font, command=AnswerThree, wraplength=110, justify="left")
            options[0].place(x=10, y=200, width=150,height=200)
            options[1].place(x=160, y=200, width=150,height=200)
            options[2].place(x=310, y=200, width=150,height=200)
            options[3].place(x=460, y=200, width=125,height=200)


    
def showWrite():
    global write
    try:
        write.place(x=185, y=200, width=200, height=100)
    except NameError:
        write = tk.Text(font=default_font, width=200, height=100)
        write.place(x=185, y=200, width=200, height=100)

def showOptionsOrWrite():
    global options
    global write
    global doneButton
    if (answerType == "write"):
        print("write")
        showWrite()
        doneButton = tk.Button(font=default_font, text=u"Готово", command=nextTask)
        doneButton.place(x=250, y=350)
        try:
            options[0].destroy()
            options[1].destroy()
            options[2].destroy()
            options[3].destroy()
        except NameError:
            pass
    else:
        print("opt")
        try:
            write.place_forget()
        except NameError:
            pass
        showOptions()

def nextTask():
    global answers
    # answers.append(func.getTextField(write) == curTask['right_answer'])
    global curTaskIndex
    global back
    curTaskIndex += 1
    # back['state'] = 'normal'
    UpdateData()
    showOptionsOrWrite()

def previousTask():
    global curTaskIndex
    curTaskIndex -= 1
    # if (curTaskIndex < 0):
    #     back['state'] = 'disabled'
    #     return
    # else:
    #     back['state'] = 'normal'
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
    global back

    global quest_lable

    root = AgrRoot
    index = AgrIndex

    root.geometry("600x400")

    testInfo = func.readJsonFile()[index]

    curTask = testInfo["questions"][curTaskIndex]

    # doneButton = tk.Button(font=default_font, text=u"Готово", command=nextTask)
    # doneButton.place(x=300, y=350)

    quest_lable = tk.Label(text="null", font=("Comic Sans MS", 23), wraplength=700)
    quest_lable.place(x=10, y=30)

    #back = tk.Button(font=default_font, text=u"Назад", command=previousTask)
    #back.place(x=10, y=325, width=120, height=60)

    # if (curTaskIndex == 0):
    #     back['state'] = 'disabled'

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