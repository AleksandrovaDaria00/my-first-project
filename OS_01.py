from tkinter import *
from tkinter import filedialog as fd
import os
from datetime import datetime

window = Tk()
window.withdraw()

direct = fd.askdirectory()

if direct:
    for file in os.listdir(direct):
        if file.lower().endswith(('.jpg', '.jpeg', '.png', '.bnp', '.tiff')):
            filepath = os.path.join(direct, file)
            lt = os.path.getmtime(filepath)
            t = datetime.fromtimestamp(lt).strftime('%d.%m.%Y')
            print(t)
