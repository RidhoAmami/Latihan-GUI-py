import tkinter as tk
from tkinter import ttk

def update():
    cvrtX = int(intX.get())
    cvrtY = int(intY.get())
    rumus = 0.5 * cvrtX * cvrtY
    tHsl = f'= {rumus}'
    lHsl.config(text=tHsl)

root = tk.Tk()
root.title('Muh Ridho Amami')
root.resizable(True, True)

style = ('Times New Roman', 16)

hasil = tk.Frame(master=root, relief='sunken', bd=2)
hasil.pack(fill=tk.X, padx=5, pady=5)
lHsl = tk.Label(master=hasil, text='=', font=style)
lHsl.pack(anchor=tk.E, padx=5, pady=5)

inputan = tk.Frame(master=root, relief='ridge', bd=2)
inputan.pack(fill='x', padx=5, pady=5)

lX = ttk.Label(master=inputan, text='Tinggi:')
lX.pack()
intX = tk.StringVar()
iX = ttk.Entry(master=inputan, textvariable=intX)
iX.pack()

lY = ttk.Label(master=inputan, text='Alas:')
lY.pack()
intY = tk.StringVar()
iY = ttk.Entry(master=inputan, textvariable=intY)
iY.pack()

btn = ttk.Button(master=root, text='INPUT', command=update)
btn.pack()

root.mainloop()
