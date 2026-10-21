from tkinter import *
from tkinter import messagebox as mb
import pygame as pg

time_n = ''

pg.mixer.init()
pg.mixer.music.load('music.mp3')


def show_n():
    global time_n

    pg.mixer.music.load('music.mp3')
    pg.mixer.music.play()

    mb.showinfo('Напоминание', time_n)


def go_n():
    global time_n

    time_n = entry_text.get().strip()

    try:
        seconds = int(entry_time.get())

        if not time_n:
            mb.showwarning('Ошибка', 'Введите текст напоминания!')
            return

        if seconds <= 0:
            mb.showwarning('Ошибка', 'Время должно быть больше нуля!')
            return

    except ValueError:
        mb.showwarning('Ошибка', 'Введите время целым числом!')
        return

    window.after(seconds * 1000, show_n)


def stop_m():
    pg.mixer.music.stop()


window = Tk()
window.title('Напоминание')
window.geometry('350x300')

label = Label(window, text='Установите напоминание', font='Arial 16')
label.pack(pady=10)

Label(window, text='Текст напоминания:').pack()

entry_text = Entry(window, width=35)
entry_text.pack(pady=5)

Label(window, text='Время в секундах:').pack()

entry_time = Entry(window, width=15)
entry_time.pack(pady=5)

Button(window, text='Установить напоминание', command=go_n).pack(pady=15)

Button(window, text='Остановить музыку', command=stop_m).pack()

window.mainloop()