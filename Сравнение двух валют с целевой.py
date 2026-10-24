from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import requests


def update_first_currency_label(event):
    code = combobox1.get()
    name = currencies[code]
    name_currency_first.config(text=name)


def update_second_currency_label(event):
    code = combobox2.get()
    name = currencies[code]
    name_currency_second.config(text=name)


def update_third_currency_label(event):
    code = combobox3.get()
    name = currencies[code]
    name_currency_third.config(text=name)


currencies = {
    'EUR': 'Евро',
    'USD': 'Американский доллар',
    'JPY': 'Японская йена',
    'GBP': 'Британский фунт стерлингов',
    'AUD': 'Австралийский доллар',
    'CAD': 'Канадский доллар',
    'CHF': 'Швейцарский франк',
    'CNY': 'Китайский юань',
    'RUB': 'Российский рубль',
    'KZT': 'Казахстанский тенге',
    'UZS': 'Узбекский сум'
}

root = Tk()
root.title('Курс обмена валют')
root.geometry('360x400')

label_1 = Label(root, text='Базовая валюта')
label_1.pack(pady=10, padx=10)

popular_currencies = ['EUR', 'USD', 'JPY', 'GBP', 'AUD', 'CAD', 'CHF', 'CNY', 'RUB', 'KZT', 'UZS']

combobox1 = ttk.Combobox(root, values=popular_currencies, state='readonly')
combobox1.pack(pady=10, padx=10)
combobox1.bind('<<ComboboxSelected>>', update_first_currency_label)

name_currency_first = Label(root)
name_currency_first.pack()

label_2 = Label(root, text='Вторая базовая валюта')
label_2.pack(pady=10, padx=10)

combobox2 = ttk.Combobox(root, values=popular_currencies, state='readonly')
combobox2.pack(pady=10, padx=10)
combobox2.bind('<<ComboboxSelected>>', update_second_currency_label)

name_currency_second = Label(root)
name_currency_second.pack()

label_3 = Label(root, text='Целевая валюта')
label_3.pack(pady=10, padx=10)

combobox3 = ttk.Combobox(root, values=popular_currencies, state='readonly')
combobox3.pack(pady=10, padx=10)
combobox3.bind('<<ComboboxSelected>>', update_third_currency_label)

name_currency_third = Label(root)
name_currency_third.pack()


Button(text='Получить курс обмена', command=exchange).pack(pady=10, padx=10)


root.mainloop()