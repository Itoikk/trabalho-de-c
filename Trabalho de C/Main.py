from Functions import *
import BottomFunctions
from tkinter import *

class Aplications():
    def __init__(self):
        self.janela = Tk()
        self.tela()
        self.frames()
        self.botões()
        self.labels()
        self.canva()
        self.janela.mainloop()

    def tela(self):
        self.janela.title("Triângulos")
        self.janela.configure(background="lightblue")
        self.janela.geometry("700x500")
    def frames(self):
        self.frame_1=Frame(
            self.janela, bd=4, bg="white",
            highlightbackground="gray", highlightthickness=3)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)
        self.frame_2=Frame(
            self.janela, bd=4, bg="lightgray",
            highlightbackground="gray", highlightthickness=3)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)
    def botões(self):
        #Criação botão classificar triângulo
        self.bt_class=Button(self.frame_2, text="Classificar Triângulo", command = lambda: BottomFunctions.classificar_triangulo(self.dad1, self.dad2, self.dad3, self.frame_1))
        self.bt_class.place(relx=0.20, rely=0.8, relwidth=0.2, relheight=0.15)


        #Criação botão calcular área
        self.bt_area=Button(self.frame_2, text="Calcular Área", command=lambda: BottomFunctions.area(self.dad1, self.dad2, self.dad3, self.frame_1))
        self.bt_area.place(relx=0.60, rely=0.8, relwidth=0.2, relheight=0.15)
        #Criação botão perímetro
        self.bt_peri=Button(self.frame_2, text="Calcular Perímetro", command=lambda: BottomFunctions.per(self.dad1, self.dad2, self.dad3, self.frame_1))
        self.bt_peri.place(relx=0.40, rely=0.8, relwidth=0.2, relheight=0.15)
        #Criação botão limpar
        self.bt_clear=Button(self.frame_2, text="Limpar", command=lambda: BottomFunctions.limpar(self.frame_1, self.canvas))
        self.bt_clear.place(relx=0.00, rely=0.8, relwidth=0.2, relheight=0.15)
        #Criação botão criar triângulo
        self.bt_create=Button(self.frame_2, text="Criar Triângulo", command=lambda: BottomFunctions.desenhar_triangulo(self.dad1, self.dad2, self.dad3, self.canvas, self.frame_1))
        self.bt_create.place(relx=0.80, rely=0.8, relwidth=0.2, relheight=0.15)
    
    def labels(self):
        self.lbl_insdados=Label(self.frame_2, text="Insira as medidas do triângulo",
                                fg="black", bg="lightgray", font=("Arial", 11))
        self.lbl_insdados.place(relx=0.35, rely=0.02, relwidth=0.3, relheight=0.1)

        self.dad1=Entry(self.frame_2)
        self.dad1.place(relx=0.4, rely=0.15, relwidth=0.2, relheight=0.1)
        self.dad2=Entry(self.frame_2)
        self.dad2.place(relx=0.4, rely=0.3, relwidth=0.2, relheight=0.1)
        self.dad3=Entry(self.frame_2)
        self.dad3.place(relx=0.4, rely=0.45, relwidth=0.2, relheight=0.1)
    
    def canva(self):
        self.canvas=Canvas(self.frame_1, bg="white", highlightbackground="gray", highlightthickness=3,)
        self.canvas.place(relx=0.3, rely=0.0, relwidth=0.7, relheight=1)


if __name__ == "__main__":
    Aplications()

