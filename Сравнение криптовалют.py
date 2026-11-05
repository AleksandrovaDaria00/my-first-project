from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import requests


def update_currency_label(event):
    code = combobox.get()
    name = cryptocurrencies[code][0]
    name_currency.config(text=name)


def exchange():
    code = combobox.get()
    if code:
        try:
            coin_id = cryptocurrencies[code][1]

            response = requests.get('https://api.coingecko.com/api/v3/simple/price', params={'ids': coin_id, 'vs_currencies': 'usd'}, timeout=10)

            response.raise_for_status()
            data = response.json()

            if coin_id in data and 'usd' in data[coin_id]:
                exchange_rate = data[coin_id]['usd']
                mb.showinfo('Курс криптовалюты',f'1 {code} = {exchange_rate:,.2f} USD')
            else:
                mb.showerror('Ошибка', 'Курс криптовалюты не найден')

        except Exception as e:
            mb.showerror('Ошибка', f'Произошла ошибка: {e}')

    else:
        mb.showwarning('Внимание', 'Выберите криптовалюту')


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

# Пропишем необходимые цвета в отдельные переменные для удобства
BG = '#10251F'
CARD = '#1B382D'
ACCENT = '#54D6A0'
WHITE = '#F1FAF5'
GRAY = '#A0B9AC'


root = Tk()
root.title('Курсы криптовалют')
root.geometry('550x420')
root.config(bg=BG)

# Сделаем заголовок
header = Label(root, text='$ Курсы популярных криптовалют', font=('Arial', 22, 'bold'), bg=BG, fg=ACCENT)
header.pack(pady=(25, 5))

# Добавим подзаголовок
subtitle = Label(root, text='КУРСЫ КРИПТОВАЛЮТ В USD', font=('Arial', 9), bg=BG, fg=GRAY)
subtitle.pack(pady=(0, 25))

card = Frame(root, bg=CARD, padx=25, pady=20)
card.pack(padx=25, fill='x')

label_1 = Label(card, text='ВЫБЕРИТЕ КРИПТОВАЛЮТУ', font=('Arial', 10, 'bold'), bg=CARD, fg=GRAY)
label_1.pack(anchor='w', pady=(0, 10))

popular_cryptocurrencies = list(cryptocurrencies.keys())

combobox = ttk.Combobox(card, values=popular_cryptocurrencies, state='readonly', font=('Arial', 12))
combobox.pack(fill='x', pady=(0, 5))

combobox.bind('<<ComboboxSelected>>', update_currency_label)

name_currency = Label(card, text='', font=('Arial', 10), bg=CARD, fg=ACCENT)
name_currency.pack(pady=(5, 20))

label_2 = Label(card, text='ЦЕЛЕВАЯ ВАЛЮТА', font=('Arial', 10, 'bold'), bg=CARD, fg=GRAY)
label_2.pack(anchor='w', pady=(0, 10))

target_currency = Label(card, text='USD | Доллар США', font=('Arial', 12, 'bold'), bg='#26374B', fg=WHITE, pady=10)
target_currency.pack(fill='x')

button = Button(card, text='ПОЛУЧИТЬ КУРС', command=exchange, font=('Arial', 11, 'bold'), bg='#087F83', fg=WHITE, pady=12)
button.pack(fill='x', pady=(25, 5))


root.mainloop()

