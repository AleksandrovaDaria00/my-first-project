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

def exchange():
    code = combobox1.get()
    code2 = combobox2.get()
    target_code = combobox3.get()

    if code and code2 and target_code:
        try:
            response1 = requests.get(f'https://open.er-api.com/v6/latest/{code}')
            response1.raise_for_status()
            data1 = response1.json()
            response2 = requests.get(f'https://open.er-api.com/v6/latest/{code2}')
            response2.raise_for_status()
            data2 = response2.json()
            if target_code in data1['rates'] and target_code in data2['rates']:
                exchange_rate1 = data1['rates'][target_code]
                exchange_rate2 = data2['rates'][target_code]
                mb.showinfo('Курс обмена',
                            f'1 {code} = {exchange_rate1:.2f} {target_code}\n'
                            f'1 {code2} = {exchange_rate2:.2f} {target_code}'
                            )
            else:
                mb.showerror('Ошибка',
                            f'Валюта не найдена')
        except Exception as er:
            mb.showerror('Ошибка', er)

    else:
        mb.showwarning('Внимание', 'Введите код валюты')


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