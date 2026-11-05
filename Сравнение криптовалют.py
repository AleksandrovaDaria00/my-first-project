from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import requests


def update_currency_label(event):
    code = combobox.get()
    name = cryptocurrencies[code]
    name_currency.config(text=name)


def exchange():
    pass


cryptocurrencies = {
    'BTC': ('Биткоин', 'bitcoin'),
    'ETH': ('Эфириум', 'ethereum'),
    'USDT': ('Тезер', 'tether'),
    'BNB': ('Бинанс коин', 'binancecoin'),
    'XRP': ('Рипл', 'ripple'),
    'USDC': ('ЮСД коин', 'usd-coin'),
    'SOL': ('Солана', 'solana'),
    'TRX': ('Трон', 'tron'),
    'DOGE': ('Догикоин', 'dogecoin'),
    'ADA': ('Кардано', 'cardano')
}


root = Tk()
root.title('Курсы криптовалют')
root.geometry('360x300')

label_1 = Label(root, text='Выберите криптовалюту')
label_1.pack(pady=10, padx=10)

popular_cryptocurrencies = list(cryptocurrencies.keys())

combobox = ttk.Combobox(root, values=popular_cryptocurrencies, state='readonly')
combobox.pack(pady=10, padx=10)

combobox.bind('<<ComboboxSelected>>', update_currency_label)

name_currency = Label(root)
name_currency.pack(pady=10)

label_2 = Label(root, text='Целевая валюта: USD')
label_2.pack(pady=10)

Button(root, text='Получить курс', command=exchange).pack(pady=15, padx=10)


root.mainloop()

