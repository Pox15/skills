import heapq

class Grafo:
    def __init__(self):
        self.grafo = {}

    def adicionar_vertice(self, vertice, coordenadas):
        if vertice not in self.grafo:
            self.grafo[vertice] = {'coordenadas': coordenadas, 'vizinhos': {}}

    def adicionar_aresta(self, vertice1, vertice2, peso):
        if vertice1 in self.grafo and vertice2 in self.grafo:
            self.grafo[vertice1]['vizinhos'][vertice2] = peso
            self.grafo[vertice2]['vizinhos'][vertice1] = peso

    def busca_gulosa(self, inicio, destino):
        fila_prioridade = [(0, inicio)]  # (heurística, vértice)
        visitados = {}
        
        while fila_prioridade:
            _, vertice = heapq.heappop(fila_prioridade)

            if vertice == destino:
                print("Caminho encontrado:")
                caminho = [destino]
                while caminho[-1] != inicio:
                    caminho.append(visitados[caminho[-1]])
                caminho.reverse()
                print(" -> ".join(caminho))
                return

            if vertice not in visitados:
                visitados[vertice] = None

                for vizinho, _ in sorted(self.grafo[vertice]['vizinhos'].items(), key=lambda x: x[1]):
                    if vizinho not in visitados:
                        visitados[vizinho] = vertice
                        heapq.heappush(fila_prioridade, (self.distancia_euclidiana(vizinho, destino), vizinho))

    def distancia_euclidiana(self, vertice1, vertice2):
        # Esta função calcula a distância euclidiana entre dois vértices (para simular uma heurística de distância em linha reta)
        coordenadas1 = self.grafo[vertice1]['coordenadas']
        coordenadas2 = self.grafo[vertice2]['coordenadas']
        return ((coordenadas1[0] - coordenadas2[0]) ** 2 + (coordenadas1[1] - coordenadas2[1]) ** 2) ** 0.5

# Exemplo de uso
grafo = Grafo()

# Adicione vértices, coordenadas e arestas manualmente
grafo.adicionar_vertice('A', [0, 0])
grafo.adicionar_vertice('B', [1, 1])
grafo.adicionar_vertice('C', [2, 2])
grafo.adicionar_vertice('D', [3, 3])
grafo.adicionar_vertice('E', [4, 4])

grafo.adicionar_aresta('A', 'B', 2)
grafo.adicionar_aresta('A', 'C', 4)
grafo.adicionar_aresta('B', 'C', 1)
grafo.adicionar_aresta('B', 'D', 7)
grafo.adicionar_aresta('C', 'E', 3)
grafo.adicionar_aresta('D', 'E', 2)

print("Busca Gulosa de A para E:")
grafo.busca_gulosa('A', 'E')
