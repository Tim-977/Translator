from tkinter import *  
from tkinter import scrolledtext  
  
def copy():
    txt.clipboard_clear()
    txt.clipboard_append(txt.get(1.0, END))

def put():
    lbl.configure(text=txt.get("1.0", END))


window = Tk()  
window.title("Добро пожаловать в приложение PythonRu")  
# window.geometry('400x250')
lbl = Label(window, text = "Тут будет текст")
lbl.grid(column=1, row=0)
txt = scrolledtext.ScrolledText(window, width=40, height=10)
txt.insert(INSERT, 'Текстовое поле')
txt.grid(column=0, row=0)
copybtn = Button(window, text = 'Copy', command=copy)
copybtn.grid(column=0, row=1)
second = Button(window, text = 'Text', width = 40, height = 15, bg = 'cyan', command=put)
second.grid(column=0, row=2)

window.mainloop()
