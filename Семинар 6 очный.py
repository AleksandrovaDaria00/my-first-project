# name = input()
# number = input()
#
# print(f'Кабинет {number}. Сотрудник: {name}')

# cost = int(input())
#
# if cost < 1000:
#     print('Доставка: 199 рублей')
# elif 1000 <= cost <= 4999:
#     print('Доставка: 99 рублей')
# else:
#     print('Доставка: бесплатно')

# name = input()
# name = name.strip()
#
# if not name:
#     print('Ошибка: пустое имя')
# elif len(name) > 12:
#     print('Ошибка: слишком длинное имя')
# elif '0' in name or '1' in name or '2' in name or '3' in name or '4' in name or '5' in name or '6' in name or '7' in name or '8' in name or '9' in name:
#     print('Ошибка: в имени цифры')
# else:
#     print(f'Имя принято: {name}')

time = input()

try:
    n = int(time)
    if 1 <= n <= 120:
        print(f'Таймер: {n} мин')
    else:
        print('Нужно от 1 до 120 минут')
except:
    print('Это не число')