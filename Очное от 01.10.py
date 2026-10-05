from tkinter import *


def plus():
    try:
        n = int(e1.get().strip())
        n1 = int(e2.get().strip())
        r = n + n1
        m['text'] = f'Результат: {r}'
    except ValueError:
        m['text'] = 'Ошибка: введите целые числа'


def sub():
    try:
        n = int(e1.get().strip())
        n1 = int(e2.get().strip())
        r = n - n1
        m['text'] = f'Результат: {r}'
    except ValueError:
        m['text'] = 'Ошибка: введите целые числа'

def change():
    p = e1.get()
    e1.delete(0, END)
    e1.insert(0, e2.get())
    e2.delete(0, END)
    e2.insert(0, p)


def save():
    text = m.cget('text')
    if text == 'Результат: —' or text == 'Ошибка: введите целые числа':
        return

    res = int(text.split(':', 1)[1].strip())
    memory['text'] = f'Память: {res}'


def in_e1():
    res = memory.cget('text').split(':', 1)[1].strip()
    if res != 'пуста':
        e1.delete(0, END)
        e1.insert(0, res)

window = Tk()
window.title('Мой калькулятор')
window.geometry('420x320')

m1 = Label(text='Первое число')
m1.pack()
e1 = Entry()
e1.pack()
m2 = Label(text='Второе число')
m2.pack()
e2 = Entry()
e2.pack()

f1 = Frame(window)
f1.pack()

b = Button(f1, text='Сложить')
b.config(command=plus)
b.pack(side=LEFT)
b1 = Button(f1, text='Вычесть')
b1.config(command=sub)
b1.pack(side=LEFT)
m = Label(text='Результат: —')
m.pack()
b3 = Button(text='Поменять местами')
b3.config(command=change)
b3.pack()
memory = Label(text='Память: пуста')
memory.pack()

f2 = Frame()
f2.pack()

b2 = Button(f2, text='В память')
b2.config(command=save)
b2.pack(side=LEFT)
b3 = Button(f2, text='Из памяти')
b3.config(command=in_e1)
b3.pack(side=LEFT)

window.mainloop()
