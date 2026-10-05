# def num2(x, n: int) -> None:
#     if n > 1:
#         num2(n - 1)
#     print(n)
#
# def num1(x, n: int) -> None:
#     if n > 1:
#         num2(n - 1)
#     print(n)

# def num(x, n: int) -> None:
#     if n > x:
#         num(x, n - 1)
#     print(n)
#
#
# num(4, 15)

"""
3! = 1 * 2 * 3 = 3 * 2!
2! = 1 * 2     = 2 * 1!
1! = 1
n! = n * (n - 1)!
"""

# def fact(n) -> int:
#     if n == 1:
#         return 1
#     else:
#         return n * fact(n-1)
#
# print(fact(6))

from tkinter import *


def answer(event=None):
    ans = num.get().strip()
    result.configure(text=ans)



root = Tk()
root.title('Старт')
WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()
X = 300
Y = 140

root.geometry(f'{X}x{Y}+{WIDTH // 2 - X // 2}+{HEIGHT// 2 - Y // 2 - 25}')
# root.geometry('300x300+400+200')

prompt = Label(text='Введите значение ', font='Arial 12')
prompt.pack(side=TOP)
# LEFT, RIGHT, BOTTOM
num = Entry(width=5, font='Arial 12', justify='center')
num.pack()

result = Label(text='   ', font='Arial 15', bg='lightgray')
result.pack(pady=10)

btn = Button(text='Выполнить', command=answer)
btn.pack()

num.bind('<Return>', answer)


root.mainloop()