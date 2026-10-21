from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import time
import pygame


def set():
    ren = sd.askstring('Время напоминания', 'Введите время напоминания в формате чч:мм (в 24ч. формате)')
    if ren:
        try:
            hour = int(ren.split(':')[0])
            minute = int(ren.split(':')[1])
            now = datetime.datetime.now()
            print(now)
            dt = now.replace(hour=hour, minute=minute)
            print(dt)
            t = dt.timestamp()
            print(t)
        except Exception as e:
            mb.showerror('Ошибка!', f'Произошла ошибка {e}')


window = Tk()
window.title('Напоминание')
label = Label(text='Установите напоминание')
label.pack(pady=10)

set_button = Button(text='Установить напоминание', command=set)
set_button.pack()



window.mainloop()