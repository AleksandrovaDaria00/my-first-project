def get_number(prompt):
    while True:
        value = input(prompt)
        if value.lstrip('-').isdigit():
            return int(value)
        else:
            print('Это не целое число!')

def add(x, y):
    return x + y

def subtruct(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return 'Ошибка! Деление на ноль.'
    except TypeError:
        return 'Ошибка типа данных.'

def log(result):
    try:
        with open('calculations.txt', 'a') as file:
            file.write(result + '\n')
    except Exception as e:
        print(f'Произошла ошибка: {e}')

# добавляем 5-ю функцию, чтение текстового файла с записанными туда вычислениями

def get_result():
    try:
        with open('calculations.txt', 'r') as file:
            calc = file.readlines()
        if not calc:
            print('История вычислений пуста.')
        else:
            print('История вычислений:')
            for calculations in calc:
                print(calculations.strip())
    except FileNotFoundError:
        print('Файл не найден')
    except Exception as e:
        print(f'Произошла следующая ошибка: {e}')

print('Выберите операцию')
print('1. Сложение')
print('2. Вычитание')
print('3. Умножение')
print('4. Деление')
print('5. Просмотр истории вычислений')

valid_choices = ['1', '2', '3', '4', '5']
choice = None
while choice not in valid_choices:
    choice = input('Введите номер операции: ')
    if choice not in valid_choices:
        print('Вы ввели не 1, не 2, не 3, не 4 и не 5')

if choice == '5':
    get_result()
else:
    num1 = get_number('Введите первое число: ')
    num2 = get_number('Введите второе число: ')
    if choice == '1':
        r = f'Результат: {num1} + {num2} = {add(num1, num2)}'
        print(r)
        log(r)
    elif choice == '2':
        r = f'Результат: {num1} - {num2} = {subtruct(num1, num2)}'
        print(r)
        log(r)
    elif choice == '3':
        r = f'Результат: {num1} * {num2} = {multiply(num1, num2)}'
        print(r)
        log(r)
    elif choice == '4':
        result = divide(num1, num2)
        if isinstance(result, str):
            print(result)
        else:
            r = f'Результат: {num1} / {num2} = {result:.2f}'
            print(r)
            log(r)
    else:
        print('Неверный выбор операции.')