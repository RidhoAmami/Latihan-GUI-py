import tkinter as tk

master = tk.Tk()

tk.Label(master, text="Nama Depan").grid(row=0)
tk.Label(master, text=" Nama Belakang").grid(row=1)

en1 = tk.Entry(master)
en2 = tk.Entry(master)
en1.grid(row=0, column=1)
en2.grid(row=1, column=1)

def show():
    tk.Label(text=en1.get()).grid(row=3, column=0)
    tk.Label(text=en2.get()).grid(row=3, column=1)
tk.Label(master, text="Nama Depan").grid(row=0)
tk.Label(master, text="Nama Belakang").grid(row=1)

en1 = tk.Entry(master)
en2 = tk.Entry(master)
b1 = tk.Button(text="show", command=show)
en1.grid(row=0, column=1)
en2.grid(row=1, column=1)
b1.grid(row=2, column=1)

master.mainloop()