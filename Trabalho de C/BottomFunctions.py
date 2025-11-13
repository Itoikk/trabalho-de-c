from Functions import *
from tkinter import Label

def per(entry1, entry2, entry3, target_frame):
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        c = float(entry3.get())
        perim = calcular_perimetro(a, b, c)
        lbl = Label(target_frame, text=f"Perímetro: {perim}", fg="black", bg="white", font=("Arial", 13))
        lbl.place(relx=0.1, rely=0.2, anchor='w')
    except ValueError:
        for widget in target_frame.winfo_children():
            widget.destroy()

        lbl = Label(target_frame, text="Entrada inválida", fg="red", bg="white", font=("Arial", 10))
        lbl.place(relx=0.5, rely=0.5, anchor='center')

def area(entry1, entry2, entry3, target_frame):
    try:
        a=float(entry1.get())
        b=float(entry2.get())
        c=float(entry3.get())
        area=calcular_area(a, b, c)
        lbl = Label(target_frame, text=f"Área: {area}", fg="black",
                    bg="white", font=("Arial", 13))
        lbl.place(relx=0.1, rely=0.1, anchor='w')
    except ValueError:
        for widget in target_frame.winfo_children():
            widget.destroy()

        lbl = Label(target_frame, text="Entrada inválida", fg="red", bg="white", font=("Arial", 10))
        lbl.place(relx=0.5, rely=0.5, anchor='center')

def limpar(frame_target):
    for widget in frame_target.winfo_children():
        widget.destroy()

