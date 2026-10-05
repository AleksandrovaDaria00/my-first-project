# import datetime

# t = datetime.datetime.now()
# print(f'Текущее время: {t}')
#
# t1 = datetime.date.today()
# print(f'Сегодня: {t1}')
#
# date = t1.strftime('%d.%m.%y')
# print(f'Сегодня: {date}')

# if m == 1:
#     ru = 'января'
# elif m == 2:
#     ru = 'февраля'
# elif m == 3:
#     ru = 'марта'
# elif m == 4:
#     ru = 'апреля'
# elif m == 5:
#     ru = 'мая'
# elif m == 6:
#     ru = 'июня'
# elif m == 7:
#     ru = 'июля'
# elif m == 8:
#     ru = 'августа'
# elif m == 9:
#     ru = 'сентября'
# elif m == 10:
#     ru = 'октября'
# elif m == 11:
#     ru = 'ноября'
# elif m == 12:
#     ru = 'декабря'

# date1 = t1.strftime('%d %B %Y')

# ru = ''
# m = t1.month # храним номер месяца в m
# s = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
#
# month_ru = s[m - 1]
#
# print(f'Сегодня: {t1.day} {month_ru} {t1.year} года.')

# import math

# print('Число\tКвадратный корень\tКубический корень')
# print('=' * 45)
#
# for i in range(2, 10):
#     k = math.sqrt(i)
#     k3 = i ** (1/3)
#     print(f'{i:>5}\t{k:>17.4f}\t{k3:>17.4f}')

# {i:>5}\t{k:>17.4f}\t{k3:>17.4f}') это выравнивание читается как:
# переменную i двигаем к правому краю на 5 символов, переменную k двигаем к правому краю на 17 символов,
# .4f это округление вещественного числа до 4х знаков после запятой (точки)

import random

# name = ['Маша', 'Марат', 'Ашот', 'Аюр', 'Снежана']
# job = ['строитель', 'доставщик', 'балерина', 'школьник', 'двоечник', 'космонавт']
# rnd_name = random.randint(0,4)
# rnd_job = random.randint(0,5)
# age = random.randint(5,25)
# print(f'Меня зовут {name[rnd_name]} мне {age} лет, я {job[rnd_job]}')

# name = []
# job = []
#
# names = int(input('Сколько имен введете? '))
# jobs = int(input('Сколько профессий введете? '))
#
# for i in range(names):
#     name.append(input('Введите имя: '))
#
# for i in range(jobs):
#     job.append(input('Введите профессию: '))
#
# rnd_name = random.randint(0,names - 1)
# rnd_job = random.randint(0,jobs - 1)
# age = random.randint(5,30)
# print(f'Меня зовут {name[rnd_name]}, я {job[rnd_job]}, мне {age} лет')

# chr возвращает по коду числа его значение, ord - из символа его код

# print(chr(68))
# print(ord('3'))

# for i in range(256):
#     print(f'Символ {chr(i)} код символа {i}')

# alf = 'abcdefghijklmnopqrstuvwxyz'
#
# for i in alf:
#     print(f'Код символа {i} - {ord(i)}')

# f = {'яблоко', 'банан', 'манго'}
# f2 = {'груша', 'апельсин', 'манго'}
# f3 = f.union(f2)
# f.add('мандарин')
# f.discard('банан')
# print(f3)
# print('яблоко' in f)
# f4 = f.intersection(f2) # пересечения
# print(f2.issubset(f)) # подмножество ли ?

# что произошло, что со мной это сделало, где произошло

# what = {'вторжение инопланетян', 'убегающая собачка', 'дети в песочнице', 'извержение вулкана', 'прилет самолета'}
# me = {'опоздал на урок', 'задержался в классе', 'нагрубил учителю', 'не выучил стих', 'прогулял урок'}
# where = {'дома', 'на улице', 'в лифте', 'у бабушки', 'в центре города'}
#
# what_rnd = random.choice(list(what))
# me_rnd = random.choice(list(me))
# where_rnd = random.choice(list(where))
#
# print(f'Я {me_rnd}, потому что {what_rnd} {where_rnd} изменило мои планы')

# d = {'name': 'Алиса', 'age': 15}
# d2 = {'school': 'Школа 1194', 'pet': 'Паркер'}
# d.update(d2)
# del d['age']
# print(d)
# if 'age' in d:
#     print('yes')
# else:
#     print('no')

# for k, v in d.items():
#     print(k, v)

# d = {
#     'name': 'Алексей',
#     'ages': 30,
#     'prof': 'программист',
#     'hobb': ['туризм', 'велосипед', 'чтение'],
#     'educ': 'МГУ',
#     'lang': ['русский', 'английский']
# }
#
# for k, v in d.items():
#     if isinstance(v, list):
#         v = ', '.join(v)
#     print(f'{k}\t{v}')

t = {
    'кошка': 'cat',
    'собака': 'dog',
    'книга': 'book',
    'яблоко': 'apple',
    'солнце': 'sun',
    'вода': 'water',
    'дерево': 'tree',
    'цветок': 'flower',
    'машина': 'car',
    'дом': 'house',
    'cat': 'кошка',
    'dog': 'собака',
    'book': 'книга',
    'apple': 'яблоко',
    'sun': 'солнце',
    'water': 'вода',
    'tree': 'дерево',
    'flower': 'цветок',
    'car': 'машина',
    'house': 'дом'
}

# w = input('Введите слово: ')
# if w in t:
try:
    w = input('Введите слово: ').lower()
    print(f'Перевод слова {w}: {t[w]}')
except KeyError:
    print('Слова нет в словаре')

# s = []
# for x in range(1, 10):
#     s.append(x**2)
# print(s)
#
# s1 =[x**2 for x in range(1, 10) if x > 3] # что делаем, с кем, какие условия
# print(s1)
#
# even = []
# for x in range(20):
#     if x % 2 == 0:
#         even.append(x)
# print(even)
#
# even1 = [x for x in range(1, 20) if x % 2 == 0]
# print(even1)

# words = ['яблоко', 'груша', 'арбуз']
# up = []
# for x in words:
#     up.append(x.upper())
# up = [x.upper() for x in words]
# print(up)

# f = [i[0] for i in words]
# # for i in words:
# #     f.append(i[0])
# print(f)

import math

# words = ['апельсин', 'груша', 'арбуз', 'абрикос', 'мандарин']
# # n = [1, 3, 5, 6, 9, 12, 14]
# # f = [len(i) for i in words]
# # f = [str(i) for i in n]
# # f = [math.sqrt(i) for i in n if i < 10]
# f = [x for x in words if x.startswith('а')]
# print(f)