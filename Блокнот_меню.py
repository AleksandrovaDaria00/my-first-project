from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd
from transliterate import translit, get_available_language_codes
from deep_translator import GoogleTranslator  # ограничения моего IP


def transliter():
    try:
        source_text = text.get(1.0, END)
        t_text = translit(source_text, 'ru', reversed=True)
        text.delete(1.0, END)
        text.insert(1.0, t_text)
    except Exception as e:
        mb.showerror('Ошибка!', f'Произошла ошибка {e}')
    update_status()


def insert():
    try:
        file = fd.askopenfilename()
        if file:
            with open(file, 'r') as f:
                s = f.read()
            text.insert(1.0, s)
    except FileNotFoundError:
        mb.showerror('Ошибка!', 'Файл не найден')
    except Exception as e:
        mb.showerror('Ошибка!', f'Произошла ошибка {e}')
    update_status()


def delete():
    text.delete(1.0, END)
    update_status()

def save():
    try:
        file = fd.asksaveasfilename(filetypes=(('TXT files', '*.txt'), ('All files:', '*.*')))
        if file:
            with open(file, 'w') as f:
                s = text.get(1.0, END)
                f.write(s)
    except FileNotFoundError:
        mb.showerror('Ошибка!', 'Файл не найден')
    except Exception as e:
        mb.showerror('Ошибка!', f'Произошла ошибка {e}')


def quit():
    window.destroy()


def update_status():
    content = text.get(1.0, END)
    char_count = len(content)
    word_count = len(content.split())
    status_label.config(text=f'Символов: {char_count} Слов: {word_count}')


def translate():
    try:
        source_text = text.get(1.0, END)
        t_text = GoogleTranslator(source='ru', target='en').translate(source_text)
        text.delete(1.0, END)
        text.insert(1.0, t_text)
    except Exception as e:
        mb.showerror('Ошибка!', f'Произошла ошибка {e}')
    update_status()

window = Tk()

frame = Frame()
frame.pack()

text = Text(frame, width=60, height=20, bg='lightgray', fg='black', wrap=WORD)
text.pack(side=LEFT)
text.bind('<Key>', lambda event: update_status())
scroll = Scrollbar(frame, command=text.yview)
scroll.pack(side=LEFT, fill=Y)
text.config(yscrollcommand=scroll.set)
# b2 = Button(text='Открыть файл', command=insert)
# b2.pack(side=LEFT)
# b3 = Button(text='Удаление текста', command=delete)
# b3.pack(side=LEFT)
# b4 = Button(text='Сохранить', command=save)
# b4.pack(side=LEFT)

status_label = Label(text='proba', anchor=W)
status_label.pack(fill=X)




menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Файл', menu=file_menu)
file_menu.add_command(label='Открыть', command=insert)
file_menu.add_command(label='Сохранить', command=save)
file_menu.add_command(label='Удалить', command=delete)
file_menu.add_separator()
file_menu.add_command(label='Выход', command=quit)

process_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Обработка', menu=process_menu)
process_menu.add_command(label='Транслитерация', command=transliter)
process_menu.add_command(label='Перевод на английский', command=translate)

update_status()
window.mainloop()