import tkinter as tk

root=tk.Tk()
def out():
    print('Halo')
wb=tk.Button(text='Klik Saya', width=20, height=10, bg='red', fg='black', command=out)
wb.pack()
root.mainloop()