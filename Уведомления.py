


# def got():
#     if s.get() == '0':
#         m['text'] = f'Режим: Фокус'
#     elif s.get() == '1':
#         m['text'] = f'Режим: Идеи'
#     elif s.get() == '2':
#         m['text'] = f'Режим: Отдых'
#     else:
#         m['text'] = f'Режим: не выбран'
#
#
# window = Tk()
# window.title('Режим мастерской')
# window.geometry('520x420')
#
# f = Frame()
# f.pack(anchor='n')
#
# s = StringVar(value=0)
#
# rb1 = Radiobutton(f, text='Фокус', value=0, variable=s)
# rb1.pack(anchor='w')
# rb1 = Radiobutton(f, text='Идеи', value=1, variable=s)
# rb1.pack(anchor='w')
# rb1 = Radiobutton(f, text='Отдых', value=2, variable=s)
# rb1.pack(anchor='w')
#
#
# b = Button(text='Включить')
# b.config(command=got)
# b.pack()
#
# m = Label(text='Режим: не выбран')
# m.pack()
#
# window.mainloop()
# from tkinter import *
#
# def plan():
#     n = level.get()
#     m['text'] = f'План: {n} мин'
#
#
#
# window = Tk()
# window.title('Запас времени')
# window.geometry('520x420')
#
# level = Scale(from_=5, to=60, resolution=5, orient='horizontal')
# level.pack()
#
# b = Button(text='Запланировать')
# b.config(command=plan)
# b.pack()
#
# m = Label(text='План: не задан')
# m.pack()
#
#
# window.mainloop()

# from tkinter import *
#
#
# def add():
#     text = e.get().strip()
#     if not text:
#         return
#
#     l.insert(END, text)
#     e.delete(0, END)
#     n = l.size()
#     m['text'] = f'Идей: {n}'
#
#
# def delete():
#     selected = l.curselection()
#     if not selected:
#         return
#
#     l.delete(selected[0])
#     l.selection_clear(0, END)
#     n = l.size()
#     m['text'] = f'Идей: {n}'
#
#
#
# window = Tk()
# window.title('Без лишнего')
# window.geometry('520x480')
#
# e = Entry()
# e.pack()
#
# b = Button(text='Добавить')
# b.config(command=add)
# b.pack()
#
# l = Listbox()
# l.pack()
#
# b2 = Button(text='Удалить')
# b2.config(command=delete)
# b2.pack()
#
# m = Label(text='Идей: 0')
# m.pack()
#
# window.mainloop()

from tkinter import *


def check():
    t = text.get('1.0', END)

    if t == '\n':
        m['text'] = 'Символов: 0 | Строк: 0'
        return

    symb = len(t) - 1
    lines = t.count('\n')

    m['text'] = f'Символов: {symb} | Строк: {lines}'


def clear():
    text.delete(1.0, END)
    m['text'] = 'Символов: 0 | Строк: 0'


window = Tk()
window.title('Черновик под лупой')
window.geometry('620x500')

text = Text(width=30, height=8)
text.pack()

f = Frame()
f.pack()

b1 = Button(f, text='Проверить')
b1.config(command=check)
b1.pack(side=LEFT)

b2 = Button(f, text='Очистить')
b2.config(command=clear)
b2.pack(side=LEFT)

m = Label(text='Символов: 0 | Строк: 0')
m.pack()



window.mainloop()