
import functools
import math
import random
from traceback import print_tb

from matplotlib.pylab import rand


def std_round(value:float):
    return round(value, 8)

R_substituicao = 0.5

crossover_points = [3]

r_eliminacao = 0.34

t_mutacao = 0.25

class position:
    def __init__(self, id, x:float=None, y:float=None, start:bool=False, end:bool=False):
        self.id = id
        self.paths = []
        self.start = start
        self.end = end
        self.x = x
        self.y = y

    def showPaths(self):
        return [f"{p.id}: {p.prev.id}<->{p.next.id}" for p in self.paths ]

class path:
    def __init__(self, prev:position, next:position, distance:float=None):
        self.prev = prev
        self.next = next
        self.id = f"{prev.id}<->{next.id}"
        self.prev.paths.append(self)
        self.next.paths.append(self)
        if prev.x is None or prev.y is None or next.x is None or next.y is None:
            self.distance = 1 if distance is None else distance
        else:
            self.distance = std_round(math.sqrt((next.x - prev.x)**2 + (next.y - prev.y)**2))

def aptidao(ind:list[position], f:callable) -> list[float]:
    apt = [ std_round(f(i)) for i in ind ]
    apt_incorrect = None
    mn = min(apt)
    if mn < 0:
        mn = abs(mn)
        apt_incorrect = list(apt)
        apt = [std_round(i+mn) for i in apt]
    return apt, apt_incorrect

def int_rep(ind:list[list[position]]) -> list[list[int]]:
    return [ [ int(i.id) for i in rota ] for rota in ind ]

def probabilidade_rep(ind:list[position], f:callable, apt:list[float]=list()) -> list[float]:
    if(len(apt) == 0):
        apt,_ = aptidao(ind, f)
    sm = std_round(sum(apt))
    print('Σ: ',sm)
    return [ std_round(i/sm) for i in apt ]

def inversao_probabilidade_rep(ind:list[position], f:callable, apt:list[float]=list()) -> list:
    if(len(apt) == 0):
        apt,_ = aptidao(ind, f)
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

def crossover(casal:list[list[position]], points:list[int]=crossover_points):
    filhos = [[],[]]
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

def mutacao(iteration:int, to_mut:list[list[position]], r_mut:float=t_mutacao):
    ret = []
    for f in to_mut:
        if roleta(r_mut):
            idx = random.randint(0,len(f)-1)
            idx2 = random.randint(0,len(f)-1)
            temp = f[idx]
            f[idx] = f[idx2]
            f[idx2] = temp
        ret.append(f)
    return ret

"""
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
"""

"""filh[0] = mutacao(filh[0])
filh[1] = mutacao(filh[1])

print('Mutado:\n',filh)
print(int_rep(filh),'\n')"""


def makeGraphFromFile(Filename:str=None):
    if Filename is None:
        Filename = input
    graph = []
    try:
        file = open(Filename, "rt")
        coord = False
        for line in file: 
            line = line.strip()
            if not coord:
                if line == "NODE_COORD_SECTION":
                    coord = True
            else:
                info = line.split(' ')
                graph.append(position(info[0],float(info[1]),float(info[2])))
        file.close()
    except Exception as e:
        print(e)
    visited = set()
    for node in graph:
        visited.add(node)
        for node2 in graph:
            if node2 not in visited:
                path(node,node2)
    return graph

def rota_distancia(rota:list[position]):
    distancia_total = 0
    
    # Calcular a distância do percurso entre as cidades
    for i in range(len(rota) - 1):
        distancia_total += next(x for x in rota[i].paths if x.next is rota[i+1] or x.prev is rota[i+1]).distance
    
    # Adicionar a distância de retorno da última cidade para a primeira
    distancia_total += next(x for x in rota[-1].paths if x.next is rota[0] or x.prev is rota[0]).distance
    
    return distancia_total

def iterate_generations(max_iter:int=5, 
individuos:list[list[position]]=[],
R_substituicao:float=R_substituicao, 
t_mutacao:float=t_mutacao, 
func:callable=lambda x: x**2,
regra_selecao:callable=roll_till_r,
regra_mutacao:callable=mutacao,
regra_eliminacao:callable=roll_till_r,
crossover_points:list[int]|list[list[int]]=crossover_points
):
    for i in range(max_iter):
        print(f"\nGeração {i}: ")
        print('\r\n'.join(str(sublist) for sublist in int_rep(individuos)))


        aptid,incorrect = aptidao(individuos, func)
        if(incorrect):
            print("Maximizada:")
            print(incorrect)
        print(f"Aptidão: ")
        print(aptid)

        probabilidade = probabilidade_rep(individuos, func, aptid)
        print("Probabilidade: ")
        print(probabilidade)
        to_select = math.floor(len(probabilidade)*R_substituicao)

        selected = regra_selecao(i, probabilidade, to_select)
        print("Selecionado para reprodução:")
        print("\r\n".join([f"{i}: {[j.id for j in individuos[i]]}" for i in selected]))
        individuos
        j = 0
        masx = len(selected)
        filhos = []
        while j < masx:
            casal = [individuos[selected[j]], individuos[selected[j+1]]]

            print(f'Pais {j+1}:')
            print(int_rep(casal),'\n')

            if isinstance(crossover_points, list) and isinstance(crossover_points[0], list):
                filh = crossover(casal,crossover_points[i])
            else:
                filh = crossover(casal,crossover_points)
            print(f'Filhos {j+1}:')
            filhos.extend(filh)
            print(int_rep(filhos))
            j += 2

        filhos = regra_mutacao(i, filhos, t_mutacao)
        print('Mutado:')
        print(int_rep(filhos),'\n')

        aptid,_ = aptidao(individuos, func)
        print(f"Aptidão: ")
        print(aptid)
        probabilidade_culling = inversao_probabilidade_rep(individuos, func, aptid)
        print("Probabilidade de eliminação:")
        print(probabilidade_culling)
        selected = regra_eliminacao(i,probabilidade_culling,to_select)
        print("Selecionado para eliminação:")
        print("\r\n".join([f"{i}: {[j.id for j in individuos[i]]}" for i in selected]))
        for j in selected:
            individuos[j] = None
        for j in range(len(selected)):
            individuos.remove(None)
        individuos.extend(filhos)
        print("Pos-Reprodução:")
        print('\r\n'.join(str(sublist) for sublist in int_rep(individuos)))

    print(f"\r\nIndividuos finais: \r\n{'\r\n'.join(str(sublist) for sublist in int_rep(individuos))}")
    print("\r\n".join([str(apt) for apt in list(aptidao(individuos, func))]))

graph = makeGraphFromFile("berlin10.tsp")

random.seed(42)
ind = [
        random.sample(graph,len(graph)),
        random.sample(graph,len(graph)),
        random.sample(graph,len(graph)),
        random.sample(graph,len(graph)),
        random.sample(graph,len(graph)),
        random.sample(graph,len(graph))]

print("Distancia inicial:")
print('\r\n'.join(str(rota_distancia(rota)) for rota in ind))
iterate_generations(max_iter=10, 
                    individuos=ind, 
                    R_substituicao=1/3,
                    t_mutacao=0.25,
                    func=lambda x: 1 / (1 + rota_distancia(x)),
                    regra_selecao=roll_till_r, 
                    regra_mutacao=mutacao,
                    regra_eliminacao=elitist,
                    crossover_points=[3])

print("Distancia Final:")
print('\r\n'.join(str(rota_distancia(rota)) for rota in ind))

#iterate_generations(20, [1, 2, 4, 8, 16, 32], 6, 2/6, 0.25, lambda x: x**3 + x + 3, roll_till_r, mutacao, elitist, [0,1,2,3,4,5])