from tkinter import *


def draw_circle():
    color = color_entry.get()
    out_color = outline_color_entry.get()
    canvas.create_oval(50,50,150,150, outline=out_color, fill=color)

def draw_triangle():
    color = color_entry.get()
    out_color = outline_color_entry.get()
    canvas.create_polygon(50,150,100,50,150,150, outline=out_color, fill=color)

def draw_square():
    color = color_entry.get()
    out_color = outline_color_entry.get()
    canvas.create_rectangle(50,50,150,150, outline=out_color, fill=color)

def clear_canvas():
    canvas.delete('all')


def change_fon():
    color = fon_color_entry.get()
    canvas.config(bg=color)


window = Tk()
window.title('Рисование фигур')
window.geometry('400x650')
canvas = Canvas(width = 300, height = 200)
canvas.pack()

color_var = StringVar(value='blue')

circle_button = Button(text='Окружность', command=draw_circle)
circle_button.pack(pady=10)

triangle_button = Button(text='Треугольник', command=draw_triangle)
triangle_button.pack(pady=10)

square_button = Button(text='Квадрат', command=draw_square)
square_button.pack(pady=10)

clear_button = Button(text='Очистить', command=clear_canvas)
clear_button.pack(pady=10)

# blue_radio = Radiobutton(text='Синий', variable=color_var, value='blue')
# blue_radio.pack(pady=10)
#
# red_radio = Radiobutton(text='Красный', variable=color_var, value='red')
# red_radio.pack(pady=10)
#
# black_radio = Radiobutton(text='Черный', variable=color_var, value='black')
# black_radio.pack(pady=10)
Label(text='Цвет заливки').pack()
color_entry = Entry()
color_entry.pack(pady=10)
color_entry.insert(0, 'blue')

Label(text='Цвет обводки').pack()
outline_color_entry = Entry()
outline_color_entry.pack(pady=10)
outline_color_entry.insert(0, 'black')

Label(text='Цвет фона').pack()
fon_color_entry = Entry()
fon_color_entry.pack(pady=10)
fon_color_entry.insert(0, 'white')

Button(text='Изменить цвет фона', command=change_fon).pack()

window.mainloop()