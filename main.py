import tkinter as tk
from ChooseTest import chooseRoom as cr
from GlobalVars import defaultFont
root = tk.Tk()
root.title(u"Программа Тестов")
root.geometry("400x500")
root['bg'] = "#00deff"

hello = "привет"
print(u"".join([hello]))

default_font = defaultFont

def MainMenu():
    goChoose:tk.Button

    def GoToChooseTextRoom():
        mainText.destroy()
        goChoose.destroy()
        cr(root)
        
    
    root.title(u"Главное меню")

    mainText = tk.Label(text=u"Добро пожаловать в Программу Тестов!", font=defaultFont, bg=root['bg'])
    mainText.place(x=0, y=17)

    goChoose = tk.Button(text=u"Загрузить тест", font=default_font, command=GoToChooseTextRoom)
    goChoose.place(x=20, y=200, width=150, height=100)
    root.mainloop(0)

MainMenu()