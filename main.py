import math

def std_round(value:float):
    return round(value, 8)

def print_iter(x:int, fx:float):
    print(f"Xᵢ: i = {x}\tXᵢ = {fx}")

def ErroAbsoluto(aproximação:float, exato:float):
    return std_round(abs(std_round(exato)-std_round(aproximação)))

def ErroRelativo(aproximação:float, exato:float, absoluto:float=None):
    aproximação = std_round(aproximação)
    exato = std_round(exato)
    if (absoluto is None):
        absoluto = ErroAbsoluto(aproximação, exato)
    if (exato == 0):
        exato = math.pow(10,-8)
    return absoluto/exato

def derivada_aprox(valor:float, func:callable):
    valor = std_round(valor)
    passo_x = 0.00000001
    return (std_round(func(valor+passo_x)) - std_round(func(valor-passo_x)))/(2*passo_x)

def gradiente(ingreme:bool, iteracoes:int, valor_inicial:float, passo:float, func:callable):
    valor = std_round(valor_inicial)
    for i in range (1, iteracoes+1):
        valor = valor + (1 if ingreme else -1) * std_round(passo*derivada_aprox(valor, func))
        print_iter(i, valor)
    return valor

"""gradiente(True, 5, 5, 0.1, lambda x: math.pow(x,2) + 4*x +4)
gradiente(False, 5, 5, 0.1, lambda x: math.pow(x,2) + 4*x +4)
gradiente(False, 100, 5, 0.1, lambda x: math.pow(x,2) + 4*x +4)
gradiente(False, 100, -5, 0.1, lambda x: math.pow(x,2) + 4*x +4)"""