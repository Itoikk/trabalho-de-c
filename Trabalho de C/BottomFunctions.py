from Functions import *
from tkinter import *

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

def limpar(frame_target, canvas):
    for widget in frame_target.winfo_children():
        if not isinstance(widget, Canvas):
            widget.destroy()
    canvas.delete("all")

def classificar_triangulo(entry1, entry2, entry3, target_frame):
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        c = float(entry3.get()) 
        classificacao = classificar_lados(a, b, c)
        for widget in target_frame.winfo_children():
            if not isinstance(widget, Label):
                widget.destroy()
        lbl = Label(target_frame, text=f"Classificação: {classificacao}", fg="black", bg="white", font=("Arial", 13))
        lbl.place(relx=0.1, rely=0.3, anchor='w')
    except ValueError:
        lbl = Label(target_frame, text="Entrada inválida", fg="red", bg="white", font=("Arial", 10))
        lbl.place(relx=0.5, rely=0.5, anchor='center')

def desenhar_triangulo(entry1, entry2, entry3, canvas, frame_target):
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        c = float(entry3.get())
        canvas.delete("all")
        s=(a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        h = (2 * area) / a
        x_c = (b**2 - c**2 + a**2) / (2 * a)
        y_c = h
        max_dim = max(a, b, c, h)
        escala = 300 / max_dim
        x1, y1 = 50, 300
        x2, y2 = x1 + a * escala, 300
        x3, y3 = x1 + x_c * escala, 300 - y_c * escala
        centro_x = (x1 + x2 + x3) / 3
        centro_y = (y1 + y2 + y3) / 3
        canvas_cx = canvas.winfo_width() / 2
        canvas_cy = canvas.winfo_height() / 2
        dx = canvas_cx - centro_x
        dy = canvas_cy - centro_y
        x1 += dx
        y1 += dy
        x2 += dx
        y2 += dy
        x3 += dx
        y3 += dy

        canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill="lightblue", outline="black", width=2)
        canvas.create_line(x3, y3, x3, y1, fill="black", width=2)
    except ValueError:
        lbl = Label(frame_target, text="Entrada inválida", fg="red", bg="white", font=("Arial", 10))
        lbl.place(relx=0.5, rely=0.5, anchor='center')
