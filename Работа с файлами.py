# try:
#     with open('proba2.txt', encoding='utf-8') as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print('Файл не найден.')

# try:
#     with open('proba.txt', 'w', encoding='utf-8') as file:
#         file.write('Новый пробный текст.')
# except IOError:
#     print('Ошибка ввода-вывода.')
# except OSError:
#     print('Ошибка операционной системы.')
# except UnicodeEncodeError:
#     print('Ошибка кодирования текста.')
# except Exception as e:
#     print(f'Неизвестная ошибка: {e}')


# def count(file_name):
#     try:
#         with open(file_name, encoding='utf-8') as file:
#             content = file.read()
#             words = content.split()
#             return len(words)
#     except FileNotFoundError:
#        print('Файл не найден.')
#     except Exception as e:
#         print(f'Неизвестная ошибка: {e}')
#
# words = count('proba.txt')
# print(f'Количество слов в файле: {words}')

# построчная работа с файлом, НО если в одной строке 2 раза встречается слово, он посчитает 1 раз.

# def analyze_log(file_name):
#     counter = {'INFO':0, 'ERROR':0, 'WARNING':0}
#
#     try:
#         with open(file_name) as file:
#             for line in file:
#                 if '[INFO]' in line:
#                     counter['INFO'] += 1
#                 elif '[ERROR]' in line:
#                     counter['ERROR'] += 1
#                 elif '[WARNING]' in line:
#                     counter['WARNING'] += 1
#         for k, v in counter.items():
#             print(f'{k}: {v}')
#     except FileNotFoundError:
#         print(f'Файл {file_name} не найден.')
#     except Exception as e:
#         print(f'Произошла следующая ошибка: {e}')
#
# analyze_log('log.txt')

# генератор поздравлений из файла с рандомными поздравления

import random

def congratulation(file_name):
    try:
        with open(file_name, encoding='utf-8') as file:
            con = file.readlines()
        if not con:
            print('Файл пустой.')
        else:
            print(random.choice(con))
    except FileNotFoundError:
        print(f'Файл {file_name} не найден')
    except Exception as e:
        print(f'Произошла следующая ошибка: {e}')


congratulation('congrats.txt')
