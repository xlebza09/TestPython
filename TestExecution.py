
import tkinter as tk
from GlobalVars import defaultFont
"""
quest_text:tk.Label
textField:tk.Text
optionWidgets:list
doneButton:tk.Button
"""
root:tk.Tk
index:int = -1

quest_lable:tk.Label
doneButton:tk.Button
write:tk.Text
options:object

default_font:tuple = defaultFont

testInfo:object
curTask:object
curTaskIndex:int

def Start(AgrRoot:tk.Tk, AgrIndex:int, objToDelete):
    objToDelete.destroy()

    global root
    global index

    global doneButton

    root = AgrRoot
    index = AgrIndex

    






    doneButton = tk.Button(font=default_font, text=u"Готово")
    doneButton.place(x=156, y=350)

    quest_lable = tk.Label(text="null", font=("Comic Sans MS", 30))
    quest_lable.place(x=156, y=30)



"""
curQuestIndex:int = 0
testInfo:object = func.readJsonFile()[index]
curQuest:object = testInfo['questions'][curQuestIndex]
questAmount:int = len(testInfo['questions'])


def UpdateCurQuest():
    global curQuest
    curQuest = {"Hello":"how are you"}

UpdateCurQuest() """