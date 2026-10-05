# def in_file(filename, data):
#     try:
#         with open(filename, 'a') as file:
#             for k, v in t.items():
#                 file.write(f'{k} {v}\n')
#     except IOError:
#         print('Ошибка при записи файла.')
#
# t = {
#     'кошка': 'cat',
#     'собака': 'dog',
#     'книга': 'book',
#     'яблоко': 'apple',
#     'солнце': 'sun',
#     'вода': 'water',
#     'дерево': 'tree',
#     'цветок': 'flower',
#     'машина': 'car',
#     'дом': 'house',
#     'cat': 'кошка',
#     'dog': 'собака',
#     'book': 'книга',
#     'apple': 'яблоко',
#     'sun': 'солнце',
#     'water': 'вода',
#     'tree': 'дерево',
#     'flower': 'цветок',
#     'car': 'машина',
#     'house': 'дом'
# }
#
# in_file('translator.txt', t)

def translate(file_name):
    dictionary = {}
    try:
        with open(file_name, 'r', encoding='windows-1251') as file:
            for line in file:
                key, value = line.split()
                dictionary[key] = value
            print(dictionary)
    except FileNotFoundError:
        print('Файл словаря не найден.')
    except ValueError:
        print('Ошибка в формате словаря.')
    return dictionary

dict = translate('translator.txt')

word = input('Введите слово: ')
if word in dict:
    print(f'Перевод слова {word}: {dict[word]}')
else:
    print('Слово не найдено в словаре.')
