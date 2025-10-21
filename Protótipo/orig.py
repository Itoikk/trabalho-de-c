from tkinter import *

def tipo_de_triângulo_lados(a, b, c):
    if a<b+c and b<a+c and c<a+b:
        if a==b and b==c and c==a:
            return "Equilatero"
        elif a!=b and b!=c and c!=a:
            return "Escaleno"
        else:
            return "Isósceles"
    else:
        return "Triangulo com medidas erradas -O triangulo não fecha-"
    

triangulos=Tk()
triangulos.title("Triângulos")
entry1= Entry(triangulos)
entry2= Entry(triangulos)
entry3= Entry(triangulos)


def botão_lados():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        c = float(entry3.get())
        resultado=tipo_de_triângulo_lados(a, b, c)
        resultado_label.config(text= f'Classificação: {resultado}')
    except ValueError:
        resultado_label.config(text="Erro: Insira números válidos")


botão_lados1=Button(triangulos, text='Classificar Triângulo', command=botão_lados)
resultado_label=Label(triangulos, text='Classificação: ')

entry1.pack(pady=6)
entry2.pack(pady=6)
entry3.pack(pady=6)
botão_lados1.pack(pady=11)
resultado_label.pack(pady=6)

triangulos.mainloop()