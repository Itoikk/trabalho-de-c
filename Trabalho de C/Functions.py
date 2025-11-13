def classificar_lados(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Os lados devem ser maiores que zero."
    if (a < b + c) and (b < a + c) and (c < a + b):
        # Classificação
        if a == b == c:
            return "Triângulo equilátero"
        elif a == b or b == c or a == c:
            return "Triângulo isósceles"
        else:
            return "Triângulo escaleno"
    else:
        return "As medidas não formam um triângulo válido."
    
def calcular_area(lado1, lado2, lado3):
    if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
        return "Os lados devem ser maiores que zero."
    if (lado1 < lado2 + lado3) and (lado2 < lado1 + lado3) and (lado3 < lado1 + lado2):

        semiperimetro = (lado1 + lado2 + lado3) / 2
        area = (semiperimetro * (semiperimetro - lado1) * (semiperimetro - lado2) * (semiperimetro - lado3)) ** 0.5
        return area

    else:
        return "As medidas não formam um triângulo válido."

def calcular_perimetro(lado1, lado2, lado3):
    if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
        return "Os lados devem ser maiores que zero."
    if (lado1 < lado2 + lado3) and (lado2 < lado1 + lado3) and (lado3 < lado1 + lado2):

        perimetro = lado1 + lado2 + lado3
        return perimetro

    else:
        return "As medidas não formam um triângulo válido."
