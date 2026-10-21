from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import time
import pygame

t = 0


def set():
    global t
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


def check():
    global t
    if t:
        now = time.time()
        if now >= t:
            play_snd()
            t = 0
    window.after(10000, check())

def play_snd():
    pygame.mixer.init()
    pygame.mixer.music.load('music.mp3')
    pygame.mixer.music.play()


window = Tk()
window.title('Напоминание')
label = Label(text='Установите напоминание')
label.pack(pady=10)

set_button = Button(text='Установить напоминание', command=set)
set_button.pack()



window.mainloop()