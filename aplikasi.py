import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.title('Aplikasi Ridho & Eko')
root.resizable(True, True)

style=('Times New Roman', 20)

judul=ttk.Label(root, text='', font=style)
judul.pack(padx=5, pady=5)

bPrep=tk.Button(root, text='DATA PREPARATION', command='')
bPrep.pack(padx=5, pady=5)
bTrain=tk.Button(root, text='DATA TRAINING', command='')
bTrain.pack(padx=5, pady=5)
bTest=tk.Button(root, text='DATA TESTING',command='')
bTest.pack(padx=5, pady=5)

form=tk.Frame(root, relief='sunken', bd=2)
form.pack(padx=5, pady=5)

fitur1=tk.Label(form, text='FITUR 1: ')
fitur1.pack(padx=5, pady=5)
gFtr1=tk.IntVar()
iFtr1=tk.Entry(form, textvariable=gFtr1, relief='ridge', bd=2)
iFtr1.pack(padx=5, pady=5)

fitur2=tk.Label(form, text='FITUR 2: ')
fitur2.pack(padx=5, pady=5)
gFtr2=tk.IntVar()
iFtr2=tk.Entry(form, textvariable=gFtr2)
iFtr2.pack(padx=5, pady=5)

fitur3=tk.Label(form, text='FITUR 3: ')
fitur3.pack(padx=5, pady=5)
gFtr3=tk.IntVar()
iFtr3=tk.Entry(form, textvariable=gFtr3)
iFtr3.pack()

bKonf=tk.Button(root, text='KONFIRMASI', command='')

root.mainloop()