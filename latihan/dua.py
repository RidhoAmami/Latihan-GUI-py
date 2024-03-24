import tkinter as tk



window = tk.Tk()
window.title("Muh Ridho")
WLabel = tk.Label(text="Halo", fg="white", bg="black")
WLabel.pack()


#image
logo = tk.PhotoImage(file="images/abstrak.png")
WLabelImage = tk.Label(image=logo)
WLabelImage.pack()

#tombol
WButton = tk.Button(
    text="klik saya",
    width=20,
    height=10,
    bg="blue",
    fg="purple"
)



#tombol12
def out():
    print("Tombol diklik")
    window.destroy()

WButton1 = tk.Button(
    text="klik!",
    #width=20,
    height=3,
    bg="black",
    fg="blue",
    command= out
)
WButton1.pack(fill=tk.X)
window.mainloop()