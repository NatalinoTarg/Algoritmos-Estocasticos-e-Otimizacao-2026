import matplotlib.pyplot as plt
import numpy as np
from main import std_round
import math
import random

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

class position:
    def __init__(self, id, x:float=None, y:float=None, start:bool=False, end:bool=False):
        self.id = id
        self.paths = []
        self.start = start
        self.end = end
        self.x = x
        self.y = y

    def showPaths(self):
        return [f"{p.id}:  {p.phero} in {p.prev.id}<->{p.next.id}" for p in self.paths ]

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

num_simulacoes = 10000  # Numero de simulações Monte Carlo

# Definir semente aleatória para que os resultados sejam replicáveis
np.random.seed(42)

# Função para gerar uma rota aleatória e calcular a sua distância total
def gerar_rota_e_distancia(graph:list[position]):
    # Cria uma sequência aleatória de cidades (ex: [3, 0, 5, 2, 1, 4...])
    rota = list(graph)
    random.shuffle(rota)
    distancia_total = 0
    
    # Calcular a distância do percurso entre as cidades
    for i in range(len(rota) - 1):
        distancia_total += next(x for x in rota[i].paths if x.next is rota[i+1] or x.prev is rota[i+1]).distance
    
    # Adicionar a distância de retorno da última cidade para a primeira
    distancia_total += next(x for x in rota[-1].paths if x.next is rota[0] or x.prev is rota[0]).distance
    
    return rota, distancia_total

# Executar a Simulação de Monte Carlo
def simulacao_monte_carlo(num_simulacoes:int, graph:list[position]):
    todas_distancias = []
    melhor_distancia = float('inf')
    melhor_rota = None
    
    for _ in range(num_simulacoes):
        rota, distancia = gerar_rota_e_distancia(graph)
        todas_distancias.append(distancia)
        
        # Guardar a melhor rota encontrada até agora
        if distancia < melhor_distancia:
            melhor_distancia = distancia
            melhor_rota = rota
            
    return todas_distancias, melhor_rota, melhor_distancia

graph = makeGraphFromFile("berlin10.tsp")
# Correr o Monte Carlo
distancias, melhor_rota, melhor_distancia = simulacao_monte_carlo(num_simulacoes, graph)

# Output dos resultados
print(f"Distâncias calculadas (Primeiras 5 amostras): {[round(d, 2) for d in distancias[:5]]}")
print("-" * 50)

# Calcular as medidas estatísticas
media_distancia = np.mean(distancias)
desvio_padrao_distancia = np.std(distancias)
percentis = np.percentile(distancias, [5, 50, 95])

print(f"Distância Média: {media_distancia:.2f}")
print(f"Desvio Padrão da Distância: {desvio_padrao_distancia:.2f}")
print(f"Percentil 5 (Rotas mais curtas): {percentis[0]:.2f}")
print(f"Percentil 50 (Mediana): {percentis[1]:.2f}")
print(f"Percentil 95 (Rotas mais longas): {percentis[2]:.2f}")
print("-" * 50)
print(f"Melhor Distância Encontrada: {melhor_distancia:.2f}")
print(f"Melhor Rota Encontrada: {[pos.id for pos in melhor_rota]}")

# Gráfico da Distribuição das Distâncias
plt.figure(figsize=(10, 5))
plt.hist(distancias, bins=50, color='lightgreen', edgecolor='black')
plt.title('Simulação de Monte Carlo: Distribuição das Distâncias do Caixeiro Viajante')
plt.xlabel('Distância Total da Rota')
plt.ylabel('Frequência')
plt.axvline(melhor_distancia, color='red', linestyle='dashed', linewidth=2, label=f'Melhor Rota ({melhor_distancia:.2f})')
plt.legend()
plt.show(block=True)