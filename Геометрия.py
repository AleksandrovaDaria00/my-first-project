from tkinter import *

window = Tk()
window.title('Главное окно')

w = window.winfo_screenwidth()
h = window.winfo_screenheight()
w2 = w // 2 - 200 # отняли половину окна
h2 = h // 2 - 150 # отняли половину окна
window.geometry(f'400x300+{w2}+{h2}')

window.mainloop()