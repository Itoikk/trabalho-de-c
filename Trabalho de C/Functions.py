def classificar_lados_lados(a, b, c):#A partir dos Lados
    if a <= 0 or b <= 0 or c <= 0:
        return "Os lados devem ser maiores que zero."
    if (a < b + c) and (b < a + c) and (c < a + b):
        if a == b == c:
            return "Triângulo equilátero"
        elif a == b or b == c or a == c:
            return "Triângulo isósceles"
        else:
            return "Triângulo escaleno"
    else:
        return "As medidas não formam um triângulo válido."

def calcular_area_lados(lado1, lado2, lado3):#A partir dos Lados
    if (lado1 < lado2 + lado3) and (lado2 < lado1 + lado3) and (lado3 < lado1 + lado2):

        semiperimetro = (lado1 + lado2 + lado3) / 2
        area = (semiperimetro * (semiperimetro - lado1) * (semiperimetro - lado2) * (semiperimetro - lado3)) ** 0.5
        return area

    else:
        return ""

def calcular_perimetro_lados(lado1, lado2, lado3):#A partir dos Lados
    if (lado1 < lado2 + lado3) and (lado2 < lado1 + lado3) and (lado3 < lado1 + lado2):
        perimetro = lado1 + lado2 + lado3
        return perimetro
    else:
        return ""
    
def classificar_angulos_angulos(a, b, c):#Classifica os angulos partir dos Angulos
    if a + b + c != 180:
        return "A soma dos 3 ângulos deve ser igual a 180°"
    elif 90 in [a, b, c]:
        return "Triângulo retângulo"
    elif  a > 90 or b > 90 or c > 90:
        return "Obtusângulo"
    elif a < 90 and b < 90 and c < 90:
        return "Acutângulo"
    
def classificar_lados_angulos(a, b, c):#Classifica os Lados a partir dos Angulos
    if not(a + b + c != 180 or a <= 0 or b <= 0 or c <= 0):
        if a == b == c:
            return "Triângulo equilátero"
        elif a == b or b == c or a == c:
            return "Triângulo isósceles"
        else:
            return "Triângulo escaleno"
    else:
        return "As medidas não formam um triângulo válido."
    
def achar_lados(A, B, C):#Cria a relação do tamanho dos Lados a partir dos Angulos
    import math
    if A <= 0 or B <= 0 or C <= 0 or A + B + C != 180:
        return "Ângulos inválidos"
    a = 1
    k = a / math.sin(math.radians(A))
    b = k * math.sin(math.radians(B))
    c = k * math.sin(math.radians(C))
    M = max(a, b, c)
    a /= M
    b /= M
    c /= M
    return f"a = {a:.2f} | b = {b:.2f} | c = {c:.2f}"