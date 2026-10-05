


# def change():
#     metka['text'] = 'Черная метка'
#     metka['bg'] = 'black'
#
# window = Tk()
# metka = Label(text='Привет всем!', bg='darkred', fg='lightcoral', width=15, height=5)
# metka.pack()
# knopka = Button(text='Изменить метку', width=15, height=3)
# knopka.config(command=change)
# knopka.pack()
# window.mainloop()

# a = 128512
#
# def change():
#     global a
#     a += 1
#     metka['text'] = chr(a)
#
#
# window = Tk()
# metka = Label(text=chr(a), font='Arial 64')
# metka.pack()
# knopka = Button(text='Следующий смайлик', width=30, height=3)
# knopka.config(command=change)
# knopka.pack()
#
# window.mainloop()


# window = Tk()
# frame_top = Frame(window)
# frame_bottom = Frame(window)
# frame_top.pack()
# frame_bottom.pack()
# metka1 = Label(frame_top, text='Метка 1', bg='red')
# metka1.pack(side=LEFT)
# metka2 = Label(frame_top, text='Метка 2', bg='yellow')
# metka2.pack(side=LEFT)
# metka3 = Label(frame_bottom, text='Метка 3', bg='green')
# metka3.pack(side=LEFT)
# metka4 = Label(frame_bottom, text='Метка 4', bg='blue')
# metka4.pack(side=LEFT)
#
# window.mainloop()


# def read():
#     name = e.get()
#     print(name)
#     e.delete(0, END)
#
#
# def read2():
#     town = e2.get()
#     print(town)
#     e2.delete(0, END)
#
# window = Tk()
# f1 = Frame(window)
# f1.pack()
# f2 = Frame(window)
# f2.pack()
# m = Label(f1, text='Введите имя:', bg='grey', fg='white', font='Courier 18 bold')
# m.pack(side=LEFT)
# e = Entry(f1, width=50, bg='grey', fg='white', font='Courier 18 bold')
# e.pack(side=LEFT)
# b = Button(f1, text='Ввод', bg='grey', fg='white', font='Courier 18 bold', command=read)
# b.pack(side=LEFT)
#
# m2 = Label(f2, text='Введите город:', bg='grey', fg='white', font='Courier 18 bold')
# m2.pack(side=LEFT)
# e2 = Entry(f2, width=50, bg='grey', fg='white', font='Courier 18 bold')
# e2.pack(side=LEFT)
# b2 = Button(f2, text='Ввод', bg='grey', fg='white', font='Courier 18 bold', command=read2)
# b2.pack(side=LEFT)
#
#
#
# window.mainloop()

# from tkinter import *
# import time
#
# window = Tk()
# month = time.strftime('%B')
# year = time.strftime('%Y')
# day = time.strftime('%d')
#
# match month:
#     case 'January':
#         month = 'Января'
#     case 'February':
#         month = 'Февраля'
#     case 'March':
#         month = 'Марта'
#     case 'April':
#         month = 'Апреля'
#     case 'May':
#         month = 'Мая'
#     case 'June':
#         month = 'Июня'
#     case 'July':
#         month = 'Июля'
#     case 'August':
#         month = 'Августа'
#     case 'September':
#         month = 'Сентября'
#     case 'October':
#         month = 'Октября'
#     case 'November':
#         month = 'Ноября'
#     case 'December':
#         month = 'Декабря'
#
# m = Label(text=f'{day} {month} {year}', font='Verdana 24 bold')
# m.pack()
#
# window.mainloop()

# часы

from tkinter import *
import time

def tick():
    t = time.strftime('%H:%M:%S')
    m.config(text=t)
    m.after(1000, tick)

def bg_color():
    m['bg'] = v1.get()

def fg_color():
    m['fg'] = v2.get()

def font():
    m['font'] = v3.get()

def size():
    m['height'] = v4.get()

window = Tk()
m = Label(font='Verdana 16', bg='lightblue', fg='black')
m.pack()
v1 = StringVar()
v1.set('lightblue')

v2 = StringVar()
v2.set('black')

v3 = StringVar()
v3.set('Verdana 16')

c1 = Checkbutton(text='Переключатель цвета фона', variable=v1, onvalue='salmon', offvalue='lightblue', command=bg_color)
c1.pack()

c2 = Checkbutton(text='Переключатель цвета текста', variable=v2, onvalue='white', offvalue='black', command=fg_color)
c2.pack()

c3 = Checkbutton(text='Переключатель шрифта', variable=v3, onvalue='Arial 16', offvalue='Verdana 16', command=font)
c3.pack()

v4 = IntVar()
v4.set(1)

c4 = Checkbutton(text='Переключатель высоты', variable=v4, onvalue=3, offvalue=1, command=size)
c4.pack()


tick()
window.mainloop()

# from tkinter import *
#
# window = Tk()
# kvas = 'квас'
# tea = 'чай'
# coffee = 'кофе'
#
# drink = StringVar(value=coffee)
#
# m = Label(text='Выберите любимый напиток')
# m.pack()
#
# m2 = Label(textvariable=drink, bg='salmon')
# m2.pack()
#
# b1 = Radiobutton(text=kvas, value=kvas, variable=drink)
# b1.pack()
#
# b2 = Radiobutton(text=tea, value=tea, variable=drink)
# b2.pack()
#
# b3 = Radiobutton(text=coffee, value=coffee, variable=drink)
# b3.pack()
#
#
# window.mainloop()