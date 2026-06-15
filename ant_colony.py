"""
τ: tau quantidade de feromonas
τ₀: quantidade inicial de feromonas de feromonas de todas as arestas

pᵏᵢⱼ

Δτᵏᵢⱼ quantidade de feromonas na aresta (i,j) pela formiga

τᵢⱼ

Lᵏ quantidade de arestas no caminho percorrido pela formiga k


ρ: taxa de evaporação

vertex 1:
2
4
3

vertex 2:
1
3
4

vertex 3:
2
4
1

vertex 4:
1
3
2

feromonas ao sair = 1

τ12 = 1
τ14 = 1
τ13 = 1
τ23 = 1
τ24 = 1
τ34 = 1


1
P¹12 = t12/τ12+t13+t14
P¹12 = 1/3 True

P¹14 = 1/3

P¹13 = 1/3

P¹23 = 1/2
P¹24 = 1/2 True

Δ¹12 = 0.5
Δ¹24 = 0.5

2
P²12 = 1/3

P²14 = 1/3 True

P²13 = 1/3

Δ²14 = 1

3
P³12 = 1/3 

P³14 = 1/3 True

P³13 = 1/3

Δ³14 = 1

4
P⁴12 = 1/3 True

P⁴14 = 1/3

P⁴13 = 1/3

P⁴23 = 1/2
P⁴24 = 1/2 True

Δ⁴12 = 0.5
Δ⁴24 = 0.5

ρ = 0.5
τ12 = 1
τ12 = τ12*ρ
τ12 = 0.5

τ12 = 0.5
τ14 = 0.5
τ13 = 0.5
τ23 = 0.5
τ24 = 0.5
τ34 = 0.5

Δ12 = 1
Δ14 = 2
Δ24 = 1

τ12 = 1.5
τ14 = 2.5
τ13 = 0.5
τ23 = 0.5
τ24 = 1.5
τ34 = 0.5

iter 2

1
P¹12 = 1.5/1.5+2.5+05
P¹12 = 1.5/4.5
P¹12 = 0.33

P¹13 = 0.5/1.5+2.5+05
P¹13 = 0.5/4.5
P¹13 = 0.11

P¹14 = 2.5/4.5
P¹14 = 0.56 True

Δ¹14 = 1

2
P²12 = 1.5/1.5+2.5+05
P²12 = 1.5/4.5
P²12 = 0.33

P²13 = 0.5/1.5+2.5+05
P²13 = 0.5/4.5
P²13 = 0.11

P²14 = 2.5/4.5
P²14 = 0.56 True

Δ²14 = 1

3
P³12 = 1.5/1.5+2.5+05
P³12 = 1.5/4.5
P³12 = 0.33

P³13 = 0.5/1.5+2.5+05
P³13 = 0.5/4.5
P³13 = 0.11

P³14 = 2.5/4.5
P³14 = 0.56 True

Δ³14 = 1

4
P⁴12 = 1.5/1.5+2.5+05
P⁴12 = 1.5/4.5
P⁴12 = 0.33 True

P⁴13 = 0.5/1.5+2.5+05
P⁴13 = 0.5/4.5
P⁴13 = 0.11

P⁴14 = 2.5/4.5
P⁴14 = 0.56

P⁴24 = 1.5/1.5+0.5
P⁴24 = 1.5/2
P⁴24 = 0.75 True

P⁴23 = 0.5/1.5+0.5
P⁴23 = 0.5/2
P⁴23 = 0.25

Δ⁴12 = 0.5
Δ⁴24 = 0.5

ρ

τ12 = 1.5 = 0.75
τ14 = 2.5 = 1.25
τ13 = 0.5 = 0.25
τ23 = 0.5 = 0.25
τ24 = 1.5 = 0.75
τ34 = 0.5 = 0.25

Δ14 = 3
Δ12 = 0.5
Δ24 = 0.5

τ12 = 0.75 = 1.25
τ14 = 1.25 = 3.25
τ13 = 0.25 = 0.25
τ23 = 0.25 = 0.25
τ24 = 0.75 = 1.25
τ34 = 0.25 = 0.25

f1 v1 v2 v4
f2 v1 v2 v4


Exemplo 2:

ρ: 0.6

vertex 1:
2
4
3

vertex 2:
1
3
4

vertex 3:
2
4
1

vertex 4:
1
3
2

feromonas ao sair = 1

τ12 = 1
τ14 = 1
τ13 = 1
τ23 = 1
τ24 = 1
τ34 = 1

formiga 1
P¹12 = 1/3 True
P¹13 = 1/3
P¹14 = 1/3

P¹23 = 1/2
P¹24 = 1/2 True

Δ¹12 = 0.5
Δ¹24 = 0.5

formiga 2
P²12 = 1/3 True
P²13 = 1/3
P²14 = 1/3

P²23 = 1/2
P²24 = 1/2 True

Δ²12 = 0.5
Δ²24 = 0.5

formiga 3
P³12 = 1/3
P³13 = 1/3 True
P³14 = 1/3

P³23 = 1/2 True
P³34 = 1/2

P³24 = 1/1 True

Δ³13 = 0.33
Δ³23 = 0.33
Δ³24 = 0.33

formiga 4
P⁴12 = 1/3 True
P⁴13 = 1/3
P⁴14 = 1/3

P⁴23 = 1/2
P⁴24 = 1/2 True

Δ⁴12 = 0.5
Δ⁴24 = 0.5

ρ = 0.6
remanece = 0.4

τ12 = 1 * (1 - ρ) = 0.4
τ14 = 1 * (1 - ρ) = 0.4
τ13 = 1 * (1 - ρ) = 0.4
τ23 = 1 * (1 - ρ) = 0.4
τ24 = 1 * (1 - ρ) = 0.4
τ34 = 1 * (1 - ρ) = 0.4


Δ¹12 = 0.5
Δ²12 = 0.5
Δ⁴12 = 0.5
Δ12 = 1.5

Δ¹24 = 0.5
Δ²24 = 0.5
Δ⁴24 = 0.5
Δ³24 = 0.33
Δ24 = 1.83

Δ³13 = 0.33
Δ13 = 0.33

Δ³23 = 0.33
Δ23 = 0.33

τ12 = 0.4 + 1.5 = 1.9
τ14 = 0.4 
τ13 = 0.4 + 0.33 = 0.73
τ23 = 0.4 + 0.33 = 0.73
τ24 = 0.4 + 1.83 = 2.23
τ34 = 0.4 

τ12 = 1.9
τ14 = 0.4 
τ13 = 0.73
τ23 = 0.73
τ24 = 2.23
τ34 = 0.4   

Iteração 2

formiga 1

P¹12 = 1.9/1.9+0.4+0.73
P¹12 = 1.9/3.03
P¹12 = 0.63 True

P¹13 = 0.73/3.03
P¹13 = 0.24

P¹14 = 0.4/3.03
P¹14 = 0.13

P¹23 = 0.73/0.73 + 2.23
P¹23 = 0.73/2.96
P¹23 = 0.25

P¹24 = 2.23/2.96
P¹24 = 0.75 True

Δ¹12 = 0.5
Δ¹24 = 0.5

formiga 2

P²12 = 0.63 True

P²13 = 0.24

P²14 = 0.13

P²23 = 0.25

P²24 = 0.75 True

Δ²12 = 0.5
Δ²24 = 0.5

formiga 3

P³12 = 0.63

P³13 = 0.24

P³14 = 0.13 True

Δ³14 = 1

formiga 4

P⁴12 = 0.63 True

P⁴13 = 0.24

P⁴14 = 0.13

P⁴23 = 0.25

P⁴24 = 0.75 True

Δ⁴12 = 0.5
Δ⁴24 = 0.5

ρ = 0.6
remanescente = 1-ρ

τ12 = 1.9 * (1-ρ) = 0.76
τ14 = 0.4 * (1-ρ) = 0.16
τ13 = 0.73 * (1-ρ) = 0.29
τ23 = 0.73 * (1-ρ) = 0.29
τ24 = 2.23 * (1-ρ) = 0.89
τ34 = 0.4 * (1-ρ) = 0.16


Δ¹12 = 0.5
Δ²12 = 0.5
Δ⁴12 = 0.5
Δ12 = 1.5

Δ¹24 = 0.5
Δ²24 = 0.5
Δ⁴24 = 0.5
Δ24 = 1.5

Δ³14 = 1


τ12 = 0.76 + 1.5 = 2.26
τ14 = 0.16 + 1 = 1.16
τ13 = 0.29
τ23 = 0.29
τ24 = 0.89 + 1.5 = 2.39
τ34 = 0.16

τ12 = 2.26
τ14 = 1.16
τ13 = 0.29
τ23 = 0.29
τ24 = 2.39
τ34 = 0.16

Iteração 3

Formiga 1
P¹12 = 2.26/2.26+0.29+1.16
P¹12 = 2.26/3.71
P¹12 = 0.61 True

P¹13 = 0.29/3.71
P¹13 = 0.08

P¹14 = 1.16/3.71
P¹14 = 0.31

P¹23 = 0.29/0.29+2.39
P¹23 = 0.29/2.68
P¹23 = 0.11

P¹24 = 2.39/2.68
P¹24 = 0.89 True

Δ¹12 = 0.5
Δ¹24 = 0.5

Formiga 2
P²12 = 0.61

P²13 = 0.08

P²14 = 0.31 True

Δ²14 = 1

Formiga 3
P³12 = 0.61

P³13 = 0.08

P³14 = 0.31 True

Δ³14 = 1

Formiga 4
P⁴12 = 0.61 True

P⁴13 = 0.08

P⁴14 = 0.31

P⁴23 = 0.11

P⁴24 = 0.89 True

Δ⁴12 = 0.5
Δ⁴24 = 0.5

ρ = 0.6

τ12 = 2.26 * (1 - ρ) = 0.90
τ14 = 1.16 * (1 - ρ) = 0.46
τ13 = 0.29 * (1 - ρ) = 0.12
τ23 = 0.29 * (1 - ρ) = 0.12
τ24 = 2.39 * (1 - ρ) = 0.96
τ34 = 0.16 * (1 - ρ) = 0.06

Δ¹12 = 0.5
Δ⁴12 = 0.5
Δ12 = 1

Δ¹24 = 0.5
Δ⁴24 = 0.5
Δ24 = 1

Δ²14 = 1
Δ³14 = 1
Δ14 = 2

τ12 = 0.90 + 1 = 1.90
τ14 = 0.46 + 2 = 2.46
τ13 = 0.12
τ23 = 0.12
τ24 = 0.96 + 1 = 1.96
τ34 = 0.06

τ12 = 1.90
τ13 = 0.12
τ14 = 2.46
τ23 = 0.12
τ24 = 1.96
τ34 = 0.06

Iteração 4

Formiga 1
P¹12 = 1.90/1.90+0.12+2.46
P¹12 = 1.90/4.48
P¹12 = 0.42

P¹13 = 0.12/4.48
P¹13 = 0.03

P¹14 = 2.46/4.48
P¹14 = 0.55 True

Δ14¹ = 1

Formiga 2
P²12 = 0.42 True

P²13 = 0.03

P²14 = 0.55

P²23 = 0.12/0.12+1.96
P²23 = 0.12/2.08
P²23 = 0.06 True

P²24 = 1.96/2.08
P²24 = 0.94

P²34 = 0.06/0.06
P²34 = 1 True

Δ²12 = 0.33
Δ²23 = 0.33
Δ²34 = 0.33

Formiga 3
P³12 = 0.42

P³13 = 0.03

P³14 = 0.55 True

Δ³14 = 1

Formiga 4
P⁴12 = 0.42

P⁴13 = 0.03

P⁴14 = 0.55

Δ⁴14 = 1

ρ = 0.6

τ12 = 1.90 * (1-ρ) = 0.76
τ13 = 0.12 * (1-ρ) = 0.05
τ14 = 2.46 * (1-ρ) = 0.98
τ23 = 0.12 * (1-ρ) = 0.05
τ24 = 1.96 * (1-ρ) = 0.78
τ34 = 0.06 * (1-ρ) = 0.02


Δ14¹ = 1
Δ³14 = 1
Δ⁴14 = 1
Δ14 = 3

Δ²12 = 0.33
Δ12 = 0.33

Δ²23 = 0.33
Δ23 = 0.33

Δ²34 = 0.33
Δ34 = 0.33

τ12 = 0.76 + 0.33 = 1.09
τ13 = 0.05
τ14 = 0.98 + 3 = 3.98
τ23 = 0.05 + 0.33 = 0.38
τ24 = 0.78
τ34 = 0.02 + 0.33 = 0.35

τ12 = 1.09
τ13 = 0.05
τ14 = 3.98
τ23 = 0.38
τ24 = 0.78
τ34 = 0.35

iteração 5

"""
import sys, io

from main import std_round
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import math
import random

from click import File

class position:
    def __init__(self, id, x:float=None, y:float=None, start:bool=False, end:bool=False):
        self.id = id
        self.paths = []
        self.start = start
        self.end = end
        self.x = x
        self.y = y

    def showPaths(self):
        return [f"{p.id}:  {p.phero} in {p.prev.id}←→{p.next.id}" for p in self.paths ]

class path:
    def __init__(self, prev:position, next:position, initial_phero:int=1, distance:float=None):
        self.phero = initial_phero
        self.prev = prev
        self.next = next
        self.id = f"τ{prev.id}{next.id}"
        self.prev.paths.append(self)
        self.next.paths.append(self)
        if prev.x is None or prev.y is None or next.x is None or next.y is None:
            self.distance = 1 if distance is None else distance
        else:
            self.distance = std_round(math.sqrt((next.x - prev.x)**2 + (next.y - prev.y)**2))

class ant:
    def __init__(self, phero:float):
        self.phero = phero
        self.visited = set()
        self.path = set()

def makeGrid(x:int, y:int):
    grid = [ [ position((i,j)) for i in range(x)] for j in range(y) ]

    return grid

def stringifyGrid(grid:list[list[position]], showPos:bool=False):
    string = ""
    for i in grid:
        for j in i:
            if showPos:
                string += f"({j.x}, {j.y})\t"
            else:
                string += f"{j.value}\t"
        string += "\r\n"
    return string

def roleta(prob:float) -> bool:
    return prob >= random.random()

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

"""test_grid = makeGrid(10,10)
print( stringifyGrid(test_grid, True))
print( stringifyGrid(test_grid))"""


"""
r_evaporation = 0.5

edge1 = position(1,start=True)
edge2 = position(2)
edge3 = position(3)
edge4 = position(4)

path(edge1,edge2, 1)
path(edge1,edge3, 1)
path(edge1,edge4, 1)

path(edge2,edge3, 1)
path(edge2,edge4, 1)

path(edge3,edge4, 1)

print(f"Point{edge1.id}",edge1.showPaths())
print(f"Point{edge2.id}",edge2.showPaths())
print(f"Point{edge3.id}",edge3.showPaths())
print(f"Point{edge4.id}",edge4.showPaths())"""

def displayGraph(paths:set[path]):
    lpath = list(paths)
    lpath.sort(key=lambda x: x.id)
    for p in lpath:
        print(f"{p.id}:  {p.phero} in {p.prev.id}←→{p.next.id}")

def iterate_ant( graph:list[position], max_iter:int=5, ants:int=4, pheromone:int=1, r_evaporation:float=0.5):
    init = None
    for edge in graph:
        if(edge.start):
            init = edge
            break
    if init is None:
        init = graph[random.randint(0,len(graph)-1)]
    paths = set([ p for pos in graph for p in pos.paths])
    for i in range( max_iter):
        print(f"\r\n\r\niteração {i+1}:")
        print("\r\nInicial:")
        displayGraph(paths)
        hive = []
        for j in range(ants):
            edge = init
            at = ant(pheromone)
            hive.append(at)
            not_end = True
            print(f"\r\nFormiga {j+1}:")
            while not_end:
                at.visited.add(edge)
                sm = 0
                valid = []
                for p in edge.paths:
                    if p.prev not in at.visited:
                        sm += p.phero
                        valid.append(p)
                    if p.next not in at.visited:
                        sm += p.phero
                        valid.append(p)
                prob = []
                print("Chance")
                for p in range(len(valid)):
                    rs = valid[p].phero/sm
                    print(f"{valid[p].id}: {math.floor(rs*100)}%")
                    prob.append(rs)
                if len(prob) == 0:
                    print(f"Final: {edge.id}")
                    not_end = False
                    break
                selected = roll_till_r(i, prob, 1)
                pth = valid[selected[0]]
                print(f"Escolhido: {pth.id}")
                at.path.add(pth)
                edge = pth.prev if pth.prev not in at.visited else pth.next
                if edge.end:
                    print(f"Final: {edge.id}")
                    not_end = False
        for p in paths:
            p.phero *= (1-r_evaporation)
        print("\r\nEvaporation:")
        displayGraph(paths)

        for at in hive:
            phero = at.phero/sum([ p.distance for p in at.path])
            for p in at.path:
                p.phero += phero
        print("\r\nFeromonios adicionados:")
        displayGraph(paths)

r_evaporation = 0.5
"""
edge1 = position(1,start=True)
edge2 = position(2)
edge3 = position(3)
edge4 = position(4)
edge5 = position(5, end=True)

path(edge1,edge2, 1)
path(edge1,edge5, 1)

path(edge2,edge3, 1)
path(edge2,edge4, 1)
path(edge2,edge5, 1)

path(edge3,edge4, 1)

path(edge4,edge5, 1)

iterate_ant(graph=[edge1, edge2, edge3, edge4, edge5], max_iter=5, ants=4, pheromone=1,r_evaporation=r_evaporation)
"""

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

graph = makeGraphFromFile("berlin10.tsp")
iterate_ant(graph=graph, max_iter=5, ants=4, pheromone=1000,r_evaporation=r_evaporation)