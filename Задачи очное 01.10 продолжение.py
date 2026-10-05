# from tkinter import *


# def create_card():
#     if (a := name_entry.get().strip()) and (c := project_entry.get().strip()):
#         if var.get() == 1:
#             metka['text'] = f'{a} / {c} / связь: открыта'
#         else:
#             metka['text'] = f'{a} / {c} / связь: закрыта'
#     else:
#         metka['text'] = 'Ошибка. Заполните имя и проект'
#
# window = Tk()
# window.title('Визитка участника')
# window.geometry('620x520')
#
# f1 = Frame()
# f1.pack()
# name = Label(f1, text='Имя', anchor='w')
# name.pack()
# name_entry = Entry(f1)
# name_entry.pack(pady=5)
# project = Label(f1, text='Проект', anchor='w')
# project.pack()
# project_entry = Entry(f1)
# project_entry.pack()
#
# f2 = Frame()
# f2.pack()
# var = BooleanVar()
# var.set(1)
# sms = Checkbutton(f2, text='Открыт к сообщениям', variable=var, onvalue=1, offvalue=0)
# sms.pack()
# button = Button(f2, text='Собрать карточку', command=create_card)
# button.pack()
# metka = Label(f2, text='Карточка не создана')
# metka.pack()
#
#
#
#
# window.mainloop()
from tkinter import *

count = 0

def add():
    global count
    element = entry.get().strip()
    if not element:
        return
    if var.get() == 0:
        list.insert(END, f'Обычно: {element}')
    else:
        list.insert(END, f'Срочно: {element}')
    count += 1
    entry.delete(0, END)
    metka['text'] = f'Дел: {count}'


def delete():
    global count
    selected = list.curselection()
    if not selected:
        return
    list.delete(selected[0])
    list.selection_clear(0, END)
    count -= 1
    metka['text'] = f'Дел: {count}'


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

window = Tk()
window.title('Очередь с приоритетом')
window.geometry('620x520')

entry = Entry()
entry.pack()

frame = Frame()
frame.pack()

var = IntVar()
var.set(0)

check = Checkbutton(frame, text='Срочно', variable=var, onvalue=1, offvalue=0)
check.pack(side=LEFT)
button = Button(frame, text='Добавить', command=add)
button.pack(side=LEFT)

list = Listbox()
list.pack()

frame2 = Frame()
frame2.pack()
del_b = Button(frame2, text='Удалить', command=delete)
del_b.pack(side=LEFT)
up_b = Button(frame2, text='Вверх', command=upper)
up_b.pack(side=LEFT)

metka = Label(text='Дел: 0')
metka.pack()

window.mainloop()