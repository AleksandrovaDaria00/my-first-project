from tkinter import *

k = 0
t = 0

def add():
    global k
    global t
    element = entry.get().strip()
    if not element:
        return
    if var2.get() == 0:
        time = 15
    elif var2.get() == 1:
        time = 30
    else:
        time = 45
    if var.get() == 0:
        list.insert(END, f'{time} мин | обычно | {element}')
    else:
        list.insert(END, f'{time} мин | срочно | {element}')
    t += time
    k += 1
    entry.delete(0, END)
    metka['text'] = f'Дел: {k} | Время: {t} мин'


def delete():
    global k
    global t
    selected = list.curselection()
    if not selected:
        return
    index = selected[0]
    text = list.get(index)
    if text.startswith('15 мин'):
        t -= 15
    elif text.startswith('30 мин'):
        t -= 30
    elif text.startswith('45 мин'):
        t -= 45
    list.delete(index)
    list.selection_clear(0, END)
    k -= 1
    metka['text'] = f'Дел: {k} | Время: {t} мин'


def upper():
    selected = list.curselection()
    if not selected:
        return
    index = selected[0]
    if index == 0:
        return
    text_first = list.get(index)
    text_second = list.get(index - 1)
    list.delete(index)
    list.insert(index, text_second)
    list.delete(index - 1)
    list.insert(index - 1, text_first)
    list.selection_set(index - 1)


def clear():
    global k
    global t
    list.delete(0, END)
    list.selection_clear(0, END)
    k = 0
    t = 0
    metka['text'] = f'Дел: {k} | Время: {t} мин'


window = Tk()
window.title('План вечера')
window.geometry('680x620')

entry = Entry()
entry.pack()

var = IntVar()
var.set(0)

var2 = IntVar()
var2.set(1)

check = Checkbutton(text='Срочно', variable=var, onvalue=1, offvalue=0)
check.pack()

frame = Frame()
frame.pack()

r1 = Radiobutton(frame, text='15 мин', variable=var2, value=0)
r1.pack(side=LEFT)

r2 = Radiobutton(frame, text='30 мин', variable=var2, value=1)
r2.pack(side=LEFT)

r3 = Radiobutton(frame, text='45 мин', variable=var2, value=2)
r3.pack(side=LEFT)

button = Button(text='Добавить', command=add)
button.pack()

list = Listbox(width=30)
list.pack()

frame2 = Frame()
frame2.pack()

del_b = Button(frame2, text='Удалить', command=delete)
del_b.pack(side=LEFT)

up_b = Button(frame2, text='Вверх', command=upper)
up_b.pack(side=LEFT)

clear_b = Button(frame2, text='Очистить план', command=clear)
clear_b.pack(side=LEFT)

metka = Label(text='Дел: 0 | Время: 0 мин')
metka.pack()

window.mainloop()

