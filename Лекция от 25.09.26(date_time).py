from datetime import datetime, date, time, timedelta

# d = date(2024, 12, 31)
# print(d)
#
# t = time(12, 31, 16)
# print(t)
#
# dt = datetime.combine(d, t)
# print(dt)
#
# d = date.today() # дата сейчас
# print(d)
#
# # t = datetime.now().replace(microsecond=0)
#
# #dat = input('Введите число в формате (дд.мм.гг): ')
# # datte = datetime.strptime(dat, '%d %m %Y')
#
# dt = datetime.now().replace(microsecond=0)
# # dtt = dt.timetuple()
# # for i in dtt:
# #     print(i)
#
# dtt = dt.isocalendar()
# print(dtt)
# print(dt.weekday())
# print(dt.isoweekday())
# days = ('Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс')
# print(days[dt.weekday()])


# birthday = input('Введите дату рождения ("дд.мм.гг"): ')
#
# birthday = datetime.strptime(birthday, '%d.%m.%Y').date()
# dt_now = date.today()
# year_ = dt_now.year
# birthday = birthday.replace(year=year_)
# # print(birthday, dt_now, year_)
# if birthday < dt_now:
#     birthday = birthday.replace(year=year_ + 1)
# res = birthday - dt_now
# if res.days == 0:
#     print('С Днем Рождения!')
# else:
#     print(f'До Вашего дня рождения {res.days} дн.')


