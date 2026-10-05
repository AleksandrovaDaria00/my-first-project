def write_to_file(filename, data):
    try:
        with open(filename, 'a') as file:
            file.write(data + '\n')
            print('Данные успешно сохранены.')
    except IOError:
        print('Ошибка при записи файла.')

print('Создание Дневника погоды')
while True:
    date = input('Введите дату (или слово "выход" для завершения): ')
    if date.lower() == 'выход':
        break
    t = input('Введите температуру: ')
    d = input('Осадки (да/нет): ')
    data = f'{date}: Температура: {t}, осадки {d}'

    write_to_file('weather.txt', data)



