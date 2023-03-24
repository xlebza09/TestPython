from operator import index
import tkinter as tk
from tkinter import ttk
import functions as func
from TestExecution import Start
from GlobalVars import defaultFont
temp = func.readJsonFile()

default_font:tuple = defaultFont

def chooseRoom(AgrRoot:tk.Tk):
    global temp
    names:list = []

    root = AgrRoot
    selectTest:tk.Listbox
    errorText:tk.Label
    goButton:tk.Button

    def loadTest():
        try:
            Start(root, selectTest.curselection()[0], selectTest)
            errorText.destroy()
            goButton.destroy()
            
        except IndexError:
            errorText.config(text=u"Вы не выбрали тест!")

    for i in range(len(temp)):
        names.append(temp[i]['name'])

    errorText = tk.Label(text=u"", font=("Comic Sans MS", 16), fg="#ff0000", bg= root['bg'])
    errorText.place(x=0, y=270)

    selectTest = tk.Listbox(listvariable= tk.Variable(value=names), font=("Comic Sans MS", 10))
    selectTest.place(x=140, y=15)
    # selectTest.bind("<<ListboxSelect>>", selectTestSelected)

    goButton = tk.Button(text=u"Загрузить тест", command=loadTest)
    goButton.place(x=140, y=220, width=90,height=45)

