from Functions import *
from tkinter import *

#Classificar lados do triângulo
def per(entry1, entry2, entry3, target_frame):
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        c = float(entry3.get())
        perim = calcular_perimetro(a, b, c)
        lbl = Label(target_frame, text=f"Perímetro: {perim}", fg="black", bg="white", font=("Verdana", 13),
                    wraplength=400, justify=LEFT)
        lbl.place(relx=0.05, rely=0.45, anchor='w')
    except ValueError:
        for widget in target_frame.winfo_children():
            widget.destroy()

        lbl = Label(target_frame, text="Entrada inválida", fg="red", bg="white", font=("Verdana", 10))
        lbl.place(relx=0.5, rely=0.5, anchor='center')

def area(entry1, entry2, entry3, target_frame):
    try:
        a=float(entry1.get())
        b=float(entry2.get())
        c=float(entry3.get())
        area=calcular_area(a, b, c)
        lbl = Label(target_frame, text=f"Área: {area}", fg="black",
                    bg="white", font=("Verdana", 13), wraplength=400, justify=LEFT)
        lbl.place(relx=0.05, rely=0.75, anchor='w')
    except ValueError:
        for widget in target_frame.winfo_children():
            widget.destroy()

        lbl = Label(target_frame, text="Entrada inválida", fg="red", bg="white", font=("Verdana", 10))
        lbl.place(relx=0.5, rely=0.5, anchor='center')

def limpar(frames_target, canvas):
    for frame_target in frames_target:
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
        lbl = Label(target_frame, text=f"Classificação com base nos lados: {classificacao}", fg="black", bg="white", font=("Verdana", 13),
                    wraplength=400, justify=LEFT)
        lbl.place(relx=0.05, rely=0.15, anchor='w')
    except ValueError:
        lbl = Label(target_frame, text="Entrada inválida", fg="red", bg="white", font=("Verdana", 10))
        lbl.place(relx=0.5, rely=0.5, anchor='center')

def classificar_botão(entry1, entry2, entry3, target_frame):
    for widget in target_frame.winfo_children():
        widget.destroy()
    classificar_triangulo(entry1, entry2, entry3, target_frame)
    area(entry1, entry2, entry3, target_frame)
    per(entry1, entry2, entry3, target_frame)


#Classificar ângulos do triângulo
def classificar_ângulos(entry1, entry2, entry3, target_frame):
    try:
        a=float(entry1.get())
        b=float(entry2.get())
        c=float(entry3.get())
        for widget in target_frame.winfo_children():
            widget.destroy()
        classificacao=classificar_angulos(a, b, c)
        lbl = Label(target_frame, text=f"Classificação com base nos ângulos: {classificacao}", fg="black",
                    bg="white", font=("Verdana", 13), wraplength=400, justify=LEFT)
        lbl.place(relx=0.05, rely=0.5, anchor='w')
    except ValueError:
        for widget in target_frame.winfo_children():
            widget.destroy()
        lbl = Label(target_frame, text="Entrada inválida", fg="red", bg="white", font=("Verdana", 10))
        lbl.place(relx=0.5, rely=0.5, anchor='center')



def desenhar_triangulo(entry_l1, entry_l2, entry_l3,
                       entry_a1, entry_a2, entry_a3,
                       canvas, frame_target):
    try:
        def get_val(e):
            t = e.get().strip()
            return None if t == "" else float(t)
        l1 = get_val(entry_l1)
        l2 = get_val(entry_l2)
        l3 = get_val(entry_l3)
        a1 = get_val(entry_a1)
        a2 = get_val(entry_a2)
        a3 = get_val(entry_a3)
        import math
        if l1 and l2 and l3:
            a, b, c = l1, l2, l3
            if not (a + b > c and a + c > b and b + c > a):
                raise ValueError
        elif a1 and a2 and a3:
            if round(a1 + a2 + a3, 5) != 180:
                raise ValueError
            a = 1
            b = math.sin(math.radians(a2)) / math.sin(math.radians(a1))
            c = math.sin(math.radians(a3)) / math.sin(math.radians(a1))
        else:
            lados = [l1, l2, l3]
            angs = [a1, a2, a3]
            qtd_ang = sum(1 for x in angs if x is not None)
            qtd_lado = sum(1 for x in lados if x is not None)
            if qtd_ang == 2 and qtd_lado == 1:
                i_ang_faltando = angs.index(None)
                angs[i_ang_faltando] = 180 - sum(x for x in angs if x is not None)
                a1, a2, a3 = angs
                idx_lado = lados.index([x for x in lados if x is not None][0])
                lado_base = lados[idx_lado]
                base_ang = [a1, a2, a3][idx_lado]
                a = (math.sin(math.radians(a1)) / math.sin(math.radians(base_ang))) * lado_base
                b = (math.sin(math.radians(a2)) / math.sin(math.radians(base_ang))) * lado_base
                c = (math.sin(math.radians(a3)) / math.sin(math.radians(base_ang))) * lado_base
            else:
                raise ValueError
        canvas.delete("all")
        s = (a + b + c) / 2
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
        x1 += dx; y1 += dy
        x2 += dx; y2 += dy
        x3 += dx; y3 += dy
        canvas.create_polygon(x1, y1, x2, y2, x3, y3,
                              fill="lightblue", outline="black", width=2)
        canvas.create_line(x3, y3, x3, y1, fill="black", width=2)
    except ValueError:
        lbl = Label(frame_target, text="Entrada inválida",
                    fg="red", bg="white", font=("Arial", 10))
        lbl.place(relx=0.5, rely=0.5, anchor='center')
