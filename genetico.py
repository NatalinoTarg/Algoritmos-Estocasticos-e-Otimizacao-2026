
import functools
import math
import random


def std_round(value:float):
    return round(value, 8)

f = lambda x: x**2

individuos = [0, 11, 46, 63]

bit_size = 6

R_substituicao = 0.5

crossover_points = [3]

r_eliminacao = 0.34

t_mutacao = 0.25

def aptidao(ind:list[int], f:callable) -> list[float]:
    apt = [ std_round(f(i)) for i in ind ]
    mn = min(apt)
    if mn < 0:
        print(apt)
        mn = abs(mn)
        apt = [std_round(i+mn) for i in apt]
    return apt

def bit(valor:int, bit_size:int=bit_size) -> str:
    return f'{valor:0{bit_size}b}'

#print(bit(11))

def bit_rep(ind:list[int], bit_size:int=bit_size) -> list[str]:
    return [ bit(i,bit_size) for i in ind ]

def int_rep(ind:list[str]) -> list[int]:
    return [ int(i,2) for i in ind ]

def probabilidade_rep(ind:list[int], f:callable, apt:list[float]=list()) -> list[float]:
    if(len(apt) == 0):
        apt = aptidao(ind, f)
    sm = std_round(sum(apt))
    print('Σ: ',sm)
    return [ std_round(i/sm) for i in apt ]

def inversao_probabilidade_rep(ind:list[int], f:callable, apt:list[float]=list()) -> list:
    if(len(apt) == 0):
        apt = aptidao(ind, f)
    apt = [std_round(1/(i if i != 0 else 1)) for i in apt]
    sm = std_round(sum(apt))
    return [ std_round(i/sm) for i in apt ]

#print(probabilidade_rep(individuos, f))

def roleta(prob:float) -> bool:
    return prob >= random.random()

"""
cnt = 0
for i in range(100):
    if roleta(0.7):
        cnt += 1
print(cnt/100)
"""

def roll_till_r(iteration:int, probabilidades:list[float], to_select:int=2) -> list[int]:
    selected = list()
    i = 0
    while(len(selected) < to_select):
        if(i not in selected and roleta(probabilidades[i])):
            selected.append(i)
        if i+1 < len(probabilidades):
            i += 1
        else:
            i = 0
    return selected

#probabilidade = probabilidade_rep(individuos, f)
#print(roll_till_r(probabilidade))
#print(probabilidade)

def perc_by_iteration(rolls:list[list[int]],iteration:int, original:list[float], to_select:int=2):
    probabilidades = list(original)
    probabilidades.sort(reverse=True)
    selected = []
    for i in range(to_select):
        roll = rolls[iteration][i]
        if roll >= 0:
            roll -= 1
        selected.append(original.index(probabilidades[roll]))
    return selected

"""prob = [0.5, 0.3, 0.2]
random.shuffle(prob)
rolls = [[-1, -2]]
print(prob)
print (rolls)
print (perc_by_iteration(rolls, 1, prob))"""

def elitist(iteration:int, original:list[float], to_select:int=2):
    probabilidades = []
    for i in range(len(original)):
        probabilidades.append((i,original[i]))
    probabilidades.sort(key=lambda x: x[1],reverse=True)
    selected = []
    for i in range(to_select):
        selected.append(probabilidades[i][0])
    return selected

def crossover(casal:list[str], points:list[int]=crossover_points):
    filhos = ["",""]
    points.sort()
    lenPoint = len(points)
    pieces = []
    for p in casal:
        rest = p
        prog = 0
        parent = []
        for c in range(lenPoint):
            parent.append(rest[:points[c]-prog])
            rest = rest[points[c]-prog:]
            prog = points[c]
        parent.append(rest)
        pieces.append(parent)
    for i in range(len(pieces[0])):
        filhos[0] += pieces[i%2][i]
        filhos[1] += pieces[(i+1)%2][i]
    return filhos

"""casal = [46, 63]
casal_bit = bit_rep(casal)

print('Pais:\n',casal)
print(casal_bit,'\n')

filh = crossover(casal_bit)
print('Filhos:\n',filh)
print(int_rep(filh),'\n')"""

def mutacao(iteration:int, to_mut:list[int], bit_size:int=bit_size, r_mut:float=t_mutacao):
    ret = []
    for f in to_mut:
        f = bit(f,bit_size)
        if roleta(r_mut):
            flist = list(f)
            idx = random.randint(0,5)
            flist[idx] = str(int(not bool(int(flist[idx]))))
            f = "".join(flist)
        ret.append(int(f,2))
    return ret

def mutacao_fixed_rolls(rolls:list[list[int]], func:callable, gene:int, iteration:int,original:list[int], bit_size:int=bit_size, r_mut:float=t_mutacao):
    to_mut = list(original)
    to_mut.sort(key=func)
    ret = []
    for i in range(len(to_mut)):
        f = bit(to_mut[i],bit_size)
        if r_mut >= rolls[iteration][i]:
            flist = list(f)
            idx = gene-1
            flist[idx] = str(int(not bool(int(flist[idx]))))
            f = "".join(flist)
        ret.append(int(f,2))
    return ret

"""filh[0] = mutacao(filh[0])
filh[1] = mutacao(filh[1])

print('Mutado:\n',filh)
print(int_rep(filh),'\n')"""

def iterate_generations(max_iter:int=5, 
individuos:list[int]=individuos, 
bit_size:int=bit_size, 
R_substituicao:float=R_substituicao, 
t_mutacao:float=t_mutacao, 
func:callable=f,
regra_selecao:callable=roll_till_r,
regra_mutacao:callable=mutacao,
regra_eliminacao:callable=roll_till_r,
crossover_points:list[int]|list[list[int]]=crossover_points
):
    for i in range(max_iter):
        print(f"\nGeração {i}: ")
        print(individuos)

        print(bit_rep(individuos, bit_size))

        aptid = aptidao(individuos, func)
        print(f"Aptidão: ")
        print(aptid)

        probabilidade = probabilidade_rep(individuos, func, aptid)
        print("Probabilidade: ")
        print(probabilidade)
        to_select = math.floor(len(probabilidade)*R_substituicao)

        selected = regra_selecao(i, probabilidade, to_select)
        print("Selecionado para reprodução:")
        print([f"{i}: {individuos[i]}" for i in selected])
        individuos
        j = 0
        masx = len(selected)
        filhos = []
        while j < masx:
            casal = [individuos[selected[j]], individuos[selected[j+1]]]
            casal_bit = bit_rep(casal, bit_size)

            print(f'Pais {j+1}:\n',casal)
            print(casal_bit,'\n')

            if isinstance(crossover_points, list) and isinstance(crossover_points[0], list):
                filh = crossover(casal_bit,crossover_points[i])
            else:
                filh = crossover(casal_bit,crossover_points)
            print(f'Filhos {j+1}:\n',filh)
            filhos.extend(int_rep(filh))
            print(filhos,'\n')
            j += 2

        filhos = regra_mutacao(i, filhos, bit_size ,t_mutacao)
        print('Mutado:\n',filhos)
        print(bit_rep(filhos,bit_size),'\n')

        aptid = aptidao(individuos, func)
        print(f"Aptidão: ")
        print(aptid)
        probabilidade_culling = inversao_probabilidade_rep(individuos, func, aptid)
        print("Probabilidade de eliminação:")
        print(probabilidade_culling)
        selected = regra_eliminacao(i,probabilidade_culling,to_select)
        print("Selecionado para eliminação:")
        print([f"{i}: {individuos[i]}" for i in selected])
        for j in selected:
            individuos[j] = None
        for j in range(len(selected)):
            individuos.remove(None)
        individuos.extend(filhos)
        print("Pos-Reprodução:")
        print(individuos)

    print(f"\r\nIndividuos finais: {individuos}")
    print(aptidao(individuos, func))

#iterate_generations()
#iterate_generations(max_iter=100)

#random.shuffle(individuos)
#iterate_generations(max_iter=10, func=lambda x: x**2 - 63*x + 993)


#fi1indi = [ 1, 12, 20, 24, 50, 54 ]
"""fi1indi = [ 60, 48, 6, 26, 20, 24 ]

iterate_generations(2, fi1indi, R_substituicao=std_round(2/3),t_mutacao=0, func=lambda x: -x**3+50*x**2-40*x)"""

rolls = [
    [1, 3],
    [1, -1],
    [1, 2],
    ]
selection = functools.partial(perc_by_iteration, rolls)

rolls_mut = [
    [0.1, 0.15],
    [0.18, 0.8],
    [0.6, 0.75],
]


fn = lambda x: abs(x*math.sin(math.sqrt(x)))
mut = functools.partial(mutacao_fixed_rolls, rolls_mut, fn,2)

cross = [
    [2],
    [1, 4],
    [3],
]


iterate_generations(max_iter=3, 
                    individuos=[2, 8, 14,16, 22, 31], 
                    bit_size=5,
                    R_substituicao=1/3,
                    t_mutacao=0.25,
                    func=fn,
                    regra_selecao=selection, 
                    regra_mutacao=mut,
                    regra_eliminacao=elitist,
                    crossover_points=cross)


#iterate_generations(20, [1, 2, 4, 8, 16, 32], 6, 2/6, 0.25, lambda x: x**3 + x + 3, roll_till_r, mutacao, elitist, [0,1,2,3,4,5])