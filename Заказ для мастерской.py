from tkinter import *


def col():
    count = 0

    if s.get() == '0':
        count += 100
    elif s.get() == '1':
        count += 160

    if var1.get() and var2.get():
        count += 60
    elif var1.get():
        count += 20
    elif var2.get():
        count += 40
    m['text'] = f'Итого: {count}'



window = Tk()
window.title('Заказ для мастерской')
window.geometry('560x460')

s = StringVar(value=0)
f = Frame()
f.pack()

mal = Radiobutton(f, text='Малый', value=0, variable=s)
mal.pack(anchor='w')
bol = Radiobutton(f, text='Большой', value=1, variable=s)
bol.pack(anchor='w')

var1 = BooleanVar()
var2 = BooleanVar()

yp = Checkbutton(f, text='Упаковка', variable=var1)
yp.pack(anchor='w')
speed = Checkbutton(f, text='Срочно', variable=var2)
speed.pack(anchor='w')

b = Button(text='Рассчитать')
b.config(command=col)
b.pack()

m = Label(text='Итого: —')
m.pack()

window.mainloop()