import array
import math
import re
from re import split

def std_round(value:float):
    return round(value, 8)

def safe_eval(expr: str) -> object:
    allowed = {name: getattr(math, name) for name in dir(math) if not name.startswith("_")}
    allowed["math"] = math
    allowed["__builtins__"] = {}
    return eval(expr, allowed)

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

def derivada_aprox(valor:float | list, func:callable):
    retlist = True
    if(not isinstance(valor, list)):
        valor = [valor]
        retlist = False
    passo_x = 0.00000001
    for i in range(len(valor)):
        valor[i] = std_round(valor[i])
    deriv = []
    for i in range(len(valor)):
        args_backward = valor[:]
        args_forward = valor[:]
        args_forward[i] = valor[i] + passo_x
        args_backward[i] = valor[i] - passo_x
        deriv.append(std_round((std_round(func(*args_forward)) - std_round(func(*args_backward))) / (2 * passo_x)))
    if retlist:
        return deriv
    else:
        return deriv[0]

"""print(derivada_aprox([2,1],lambda x, y: math.pow(x,2) + x*y))"""

def gradiente(ingreme:bool, iteracoes:int, valor_inicial:float, passo:float, func:callable):
    valor = std_round(valor_inicial)
    for i in range (1, iteracoes+1):
        valor = std_round(valor + (1 if ingreme else -1) * std_round(passo*derivada_aprox(valor, func)))
        print_iter(i, valor)
    return valor

"""gradiente(True, 5, 5, 0.1, lambda x: math.pow(x,2) + 4*x +4)
gradiente(False, 5, 5, 0.1, lambda x: math.pow(x,2) + 4*x +4)
gradiente(False, 100, 5, 0.1, lambda x: math.pow(x,2) + 4*x +4)
gradiente(False, 100, -5, 0.1, lambda x: math.pow(x,2) + 4*x +4)"""

while (True):
    try:
        print("Argumentos(x, y, z, ... n)")
        arg = input()
        print("Função")
        func = input()
        inp = f"lambda {arg}: {func}"
        funcao = safe_eval(inp)
        funcao(*range(len(arg)))
        break
    except Exception as ex:
        print("Função invalida!",ex)
print(inp, derivada_aprox(5, funcao), funcao(5))