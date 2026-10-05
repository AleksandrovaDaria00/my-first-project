from tkinter import *
from tkinter import messagebox as mb

# window = Tk() # создаем окно (оконные приложения состоят из окна)
# lb = Listbox(width=15, height=7)
# lb.pack()
#
# days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
#
# # lb.insert(0, 'Понедельник') # вставка, на 0 место
# # lb.insert(1, 'Вторник')
# # lb.insert(2, 'Среда')
# # lb.insert(3, 'Четверг')
# # lb.insert(4, 'Пятница')
# # lb.insert(5, 'Суббота')
# # lb.insert(6, 'Воскресенье')
#
# for day in days:
#     lb.insert(END, day)
#
# window.mainloop()

def add_item():
    if s.get() == '0':
        l1.insert(END, e.get())
        e.delete(0, END)
    else:
        if validate_phone():
            l2.insert(END, e.get())
            e.delete(0, END)
            mb.showinfo('Добавление номера', 'Номер телефона успешно добавлен')


def del_item():
    if s.get() == '0':
        l1.delete(ANCHOR)
    else:
        l2.delete(ANCHOR)


def save():
    try:
        with open('phones.txt', 'w') as f:
            for i in range(l1.size()):
                f.write(f'{l1.get(i)} : {l2.get(i)}\n')
        mb.showinfo('Сохранение', 'Контакты успешно сохранены')
    except Exception as e:
        mb.showerror('Ошибка!', f'Произошла ошибка: {e}')


def load():
    try:
        with open('phones.txt', 'r') as f:
            l1.delete(0, END)
            l2.delete(0, END)
            for line in f:
                name, _, phone = line.partition(' : ')
                l1.insert(END, name)
                l2.insert(END, phone)
        mb.showinfo('Загрузка', 'Контакты успешно загружены')
    except FileNotFoundError:
        mb.showerror('Ошибка!', 'Файл не найден!')
    except Exception as e:
        mb.showerror('Ошибка!', f'Произошла ошибка: {e}')


def validate_phone():
    number = e.get()
    if len(number) == 10 and number.isdigit() and number.startswith('9'):
       # mb.showinfo('Проверка', 'Номер телефона прошел проверку')
        return True
    else:
        mb.showerror('Ошибка', 'Номер должен быть десятизначным, состоящим только из цифр и начинающимся с "9".')
        return False

window = Tk()
s = StringVar(value=0)
f1 = Frame()
f1.pack(side=LEFT)
m1 = Label(f1, text='Имена')
m1.pack()
l1 = Listbox(f1)
l1.pack()

f2 = Frame()
f2.pack(side=LEFT)
m2 = Label(f2, text='Телефоны')
m2.pack()
l2 = Listbox(f2)
l2.pack()

f3 = Frame()
f3.pack(side=LEFT)

radio1 = Radiobutton(f3, text='Имя', value=0, variable=s)
radio1.pack()
radio2 = Radiobutton(f3, text='Телефон', value=1, variable=s)
radio2.pack()
e = Entry(f3)
e.pack()
b1 = Button(f3, text='Добавить', command=add_item)
b1.pack()
b2 = Button(f3, text='Удалить', command=del_item)
b2.pack()
b3 = Button(f3, text='Сохранить', command=save)
b3.pack()
b4 = Button(f3, text='Загрузить', command=load)
b4.pack()


window.mainloop()
