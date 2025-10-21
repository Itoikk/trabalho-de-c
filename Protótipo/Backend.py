from tkinter import *

def entrada():
    a= Entry()
    a.grid(column=10, row=4)
    b= Entry()
    b.grid(column=10, row=5)
    c= Entry()
    c.grid(column=10, row=6)

def tipo_de_triângulo_lados():
    a= Entry()
    a.grid(column=10, row=4)
    b= Entry()
    b.grid(column=10, row=5)
    c= Entry()
    c.grid(column=10, row=5)
    if a<b+c and b<a+c and c<a+b:
        if a==b and b==c and c==a:
            return "Equilatero"
        elif a!=b and b!=c and c!=a:
            return "Escaleno"
        else:
            return "Isósceles"
    else:
        return "Triangulo com medidas erradas -O triangulo não fecha-"

def tipo_de_triângulo_angulos():
    entrada()
    a=float(a.get()) 
    b=float(b.get())
    c=float(c.get())
    if a+b+c!=180:
        print("Isso não é um triângulo completo")
        print("Explicação: Um triângulo deve sempre, em um plano totalmente plano, ter a soma de seus ângulos igual a 180°")
        return 0
    elif a<90 and b<90 and c<90:
        return "Acutângulo"
    elif a==90 or b==90 or c==90:
        return "Retângulo"
    else:
        return "Obtusângulo"

janela= Tk()
texto_principal= Label(janela, text='Bem vindo ao simulador de triângulos. \nClique no botão para iniciar o programa')
texto_principal.grid(column=10, row=0)
botão_de_ângulo=Button(janela, text='Ângulo', command=tipo_de_triângulo_angulos)
botão_de_ângulo.grid(column=10, row=3)
botão_lados=Button(janela, text='Medidas por lados', command=tipo_de_triângulo_lados)

janela.mainloop()
'''
while True:
    decisao=int(input("Digite 1 para classificar um triangulo com base nos seus lados, 2 para classifica-lo com base em seus ângulos e 3 para encerrar o programa: \n"))
    if decisao==1:
        a=int(input("Digite o 1° lado de seu triangulo em cm: "))
        b=int(input("Digite o 2° lado de seu triangulo em cm: "))
        c=int(input("Digite o 3° lado de seu triangulo em cm: "))
        print(tipo_de_triângulo_lados(a, b, c))
    elif decisao==2:
        a=int(input("Digite o 1° ângulo de seu triangulo: "))
        b=int(input("Digite o 2° ângulo de seu triangulo: "))
        c=int(input("Digite o 3° ângulo de seu triangulo: "))
        print(tipo_de_triângulo_angulos(a, b, c))
    else:
        print("Encerrando o programa!!")
        break
'''