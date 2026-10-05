from tkinter import *
from PIL import Image, ImageTk, ImageGrab
from tkinter import filedialog as fd
from tkinter import messagebox as mb

pen_color = 'black'
pen_width = 5

def draw(event):
    x, y = event.x, event.y
    canvas.create_oval(x, y, x + pen_width, y + pen_width, fill=pen_color, outline=pen_color)


def load_image():
    try:
        file_path = fd.askopenfilename(filetypes=[('Image files', '*.png;*.jpg;*.jpeg;*.bnp;*.gif')])
        if file_path:
            image = Image.open(file_path)
            image = image.resize((600, 400))
            image_tk = ImageTk.PhotoImage(image)
            canvas.create_image(0, 0, anchor=NW, image=image_tk)
            canvas.image = image_tk
    except Exception as e:
        mb.showerror('Ошибка!', f'Произошла ошибка {e}.')


def save_image():
    try:
        file_path = fd.asksaveasfilename(defaultextension='.png', filetypes=[('PNG files', '*.png')])
        if file_path:
            x = window.winfo_rootx()
            y = window.winfo_rooty()
            x1 = x + 600
            y1 = y + 400
            ImageGrab.grab().crop((x, y, x1, y1)).save(file_path)
            mb.showinfo('Сохранено', 'Изображение успешно сохранено!')
    except Exception as e:
        mb.showerror('Ошибка!', f'Произошла ошибка {e}.')


def quit1():
    window.destroy()


def set_pen_size():
    global pen_width
    try:
        size = int(e.get())

        if size <= 0:
            mb.showerror('Ошибка!', 'Толщина линии должна быть больше 0!')
            return
        pen_width = size
    except ValueError:
        mb.showerror('Ошибка!', 'Вы ввели не целое число!')


window = Tk()
window.title('Графический редактор')

canvas = Canvas(width=600, height=400)
canvas.pack()
canvas.bind('<B1-Motion>', draw)

colors = ['red', 'green', 'blue', 'black']
for color in colors:
    lbl = Label(bg=color, width=8, height=2)
    lbl.pack(side=LEFT)
    lbl.bind('<Button-1>', lambda e, c=color: globals().update(pen_color=c))

Label(text='Толщина линии:').pack(side=LEFT, padx=5)
e = Entry(width=5)
e.pack(side=LEFT, padx=5)
Button(text='Установить толщину', command=set_pen_size).pack(side=LEFT, padx=5)

menu_bar = Menu(window)
window.config(menu=menu_bar)
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Файл', menu=file_menu)
file_menu.add_command(label='Загрузить изображение', command=load_image)
file_menu.add_command(label='Сохранить изображение', command=save_image)
file_menu.add_separator()
file_menu.add_command(label='Выход', command=quit1)

window.mainloop()