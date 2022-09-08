from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
import random
from time import sleep



def clicked():
    global first
    global second
    btn.destroy()
    lbl.configure(text='ВЫБОР РЕЖИМА', font = ("Arial Bold", 30))
    lbl.grid(column=0, row=0, columnspan=2)
    first = Button(window, text="Зашифровать", width = 26, height = 5, fg = 'white', bg = 'black', command=once)
    first.grid(column=0, row=1)
    second = Button(window, text="Расшифровать", width = 26, height = 5, fg = 'white', bg = 'black', command=twice)
    second.grid(column=1, row=1)


def once():
    def stfun():
        forst['state'] = DISABLED
        txt['state'] = DISABLED
        keyscroll.insert(INSERT, seed)
        keyscroll.insert(INSERT, '\n')
        for i in txt.get():
            keyscroll.insert(INSERT, d[i])
        keyscroll['state'] = DISABLED
        keyscroll.clipboard_clear()
        keyscroll.clipboard_append(keyscroll.get(1.0, END))
        lbl.configure(text="СКОПИРОВАНО", bg = 'royalblue', fg = 'white', font = ("Arial Bold", 20))

    first.destroy()
    second.destroy()
    d = dict([])
    lst1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
            'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
            'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'А', 'Б', 'В',
            'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М',
            'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч',
            'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', 'а', 'б', 'в',
            'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м',
            'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч',
            'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', ' ', '0', '1',
            '2', '3', '4', '5', '6', '7', '8', '9', ',', '.', '?',
            '!', '`', '~', "'", '"', '@', '№', '#',
            ';', '$', '%', '^', ':', '(', ')', '-', '_', '+',
            '=', '*', '/', '\\', '|', '{', '}', '[', ']']
    lst2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
            'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
            'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'А', 'Б', 'В',
            'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М',
            'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч',
            'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', 'а', 'б', 'в',
            'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м',
            'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч',
            'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', ' ', '0', '1',
            '2', '3', '4', '5', '6', '7', '8', '9', ',', '.', '?',
            '!', '`', '~', "'", '"', '@', '№', '#',
            ';', '$', '%', '^', ':', '(', ')', '-', '_', '+',
            '=', '*', '/', '\\', '|', '{', '}', '[', ']']

    seed = ''
    i = 0
    while(len(lst2)):
        x = random.randint(0, len(lst2) - 1)
        seed += str(x) + ' '
        d[lst1[i]] = lst2[x]
        lst2.pop(x)
        i += 1
#     print("Введите сообщение:")
    lbl.configure(text="ВВЕДИТЕ СООБЩЕНИЕ", font = ("Arial Bold", 19))
    keyscroll = scrolledtext.ScrolledText(window,width=35,height=35)
    keyscroll.grid(column=0, row=3)
    txt = Entry(window, width=47)
    txt.grid(column=0, row=1)
    forst = Button(window, text = 'ПЕРЕВЕСТИ', bg = 'black', fg = 'white', width = 46, command=stfun)
    forst.grid(column=0, row=2)
#     print(seed)

def twice():
    def paste():
        pasteb['state'] = DISABLED
        keyscroll_2['state'] = NORMAL
        keyscroll_2.insert(INSERT, window.clipboard_get())
        keyscroll_2['state'] = DISABLED
    def stfun_2():
        lbl.configure(text="ПЕРЕВЕДЕНО", bg = 'lime', fg = 'white', font = ("Arial Bold", 32))
        keyscroll_3['state'] = DISABLED
        forst_2['state'] = DISABLED
        pasteb['state'] = DISABLED
        res_2 = keyscroll_2.get("1.0",END)
        st = ''
        seed = ''
        f = 1
        for i in res_2:
            if i == '\n':
                f = 0
                continue
            if f:
                seed += i
            else:
                st += i
        i = 0
        n = ''
        output = ''
        flag = True
        try:
            for x in seed:
                if x == ' ':
                    d[lst2[int(n)]] = lst1[i]
                    lst2.pop(int(n))
                    i += 1
                    n = ''
                else:
                    n += x
            for i in st:
                output += d[i]
        except:
#             print(10)
            lbl.configure(text="    ОШИБКА    ", fg = 'white', bg = 'red', font = ("Arial Bold", 32))
            messagebox.showerror('ОШИБКА', 'Некорректный ввод')
            flag = False
        keyscroll_3['state'] = NORMAL
        keyscroll_3.insert(INSERT, output)
        keyscroll_3['state'] = DISABLED
        if output == '' and flag:
            lbl.configure(text="    ОШИБКА    ", fg = 'white', bg = 'red', font = ("Arial Bold", 32))
            messagebox.showerror('ОШИБКА', 'Некорректный ввод')
#             print(output)
#             print(res_2)
    first.destroy()
    second.destroy()
    d = dict([])
    lst1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
            'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
            'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'А', 'Б', 'В',
            'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М',
            'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч',
            'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', 'а', 'б', 'в',
            'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м',
            'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч',
            'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', ' ', '0', '1',
            '2', '3', '4', '5', '6', '7', '8', '9', ',', '.', '?',
            '!', '`', '~', "'", '"', '@', '№', '#',
            ';', '$', '%', '^', ':', '(', ')', '-', '_', '+',
            '=', '*', '/', '\\', '|', '{', '}', '[', ']']
    lst2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
            'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
            'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'А', 'Б', 'В',
            'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М',
            'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч',
            'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', 'а', 'б', 'в',
            'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м',
            'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч',
            'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', ' ', '0', '1',
            '2', '3', '4', '5', '6', '7', '8', '9', ',', '.', '?',
            '!', '`', '~', "'", '"', '@', '№', '#',
            ';', '$', '%', '^', ':', '(', ')', '-', '_', '+',
            '=', '*', '/', '\\', '|', '{', '}', '[', ']']

    lbl.configure(text="ВВЕДИТЕ КЛЮЧ И СООБЩЕНИЕ", font = ("Arial Bold", 13))
    lbl.grid(column=0, row=0, columnspan=1)
    forst_2 = Button(window, text = 'ПЕРЕВЕСТИ', bg = 'black', fg = 'white', width = 19, height = 7, command=stfun_2)
    forst_2.grid(column=1, row=0)
    pasteb = Button(window, text = 'ВСТАВИТЬ ТЕКСТ', width = 40, height = 1, bg = 'gray', fg = 'white', font = ('Arial Bold', 14), command=paste)
    pasteb.grid(column=0, row=1, columnspan=2)
    keyscroll_2 = scrolledtext.ScrolledText(window,width=50,height=15)
#         keyscroll_2 = Entry(window, width=66)
    keyscroll_2.grid(column=0, row=2, columnspan=2)
    keyscroll_2['state'] = DISABLED
    keyscroll_3 = scrolledtext.ScrolledText(window,width=50,height=15)
    keyscroll_3['state'] = DISABLED
    keyscroll_3.grid(column=0, row=3, columnspan=2)
randau = random.randint(0, 1)

window = Tk()  
window.title("Translator")
window.resizable(0,0)
first = Button(window)
second = Button(window)
# window.geometry()
lbl = Label(window, text="Русско-Бабиджонский переводчик by Tima#5732 and Tim#8661" if randau else "Русско-Бабиджонский переводчик by Tim#8661 and Tima#5732", font = ("Arial Bold", 33))  
lbl.grid(column=0, row=0)
btn = Button(window, text="ДАЛЕЕ", width = 200, bg = 'black', fg = 'white', command=clicked)  
btn.grid(column=0, row=1)
window.mainloop()
