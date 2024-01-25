class Grafo:
    def __init__(self):
        self.grafo = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = []

    def adicionar_aresta(self, vertice1, vertice2):
        if vertice1 in self.grafo:
            self.grafo[vertice1].append(vertice2)
        else:
            self.grafo[vertice1] = [vertice2]

    def busca_em_profundidade(self, vertice_inicial):
        visitados = set()

        def dfs(vertice):
            visitados.add(vertice)
            print(vertice, end=' ')

            for vizinho in self.grafo[vertice]:
                if vizinho not in visitados:
                    dfs(vizinho)

        if vertice_inicial in self.grafo:
            dfs(vertice_inicial)

# Função para criar um grafo com base no número de vértices e arestas fornecidos
def criar_grafo(num_vertices):
    grafo = Grafo()
    for i in range(num_vertices):
        vertice = input(f"Digite o nome do vértice {i+1}: ")
        grafo.adicionar_vertice(vertice)

    while True:
        aresta = input("Digite uma aresta no formato 'vertice1 vertice2' (ou 'sair' para encerrar): ")
        if aresta.lower() == 'sair':
            break
        else:
            vertices = aresta.split()
            if len(vertices) == 2:
                grafo.adicionar_aresta(vertices[0], vertices[1])
            else:
                print("Formato inválido. Use 'vertice1 vertice2'.")

    return grafo

# Exemplo de uso
num_vertices = int(input("Digite o número de vértices: "))
grafo = criar_grafo(num_vertices)

vertice_inicial = input("Digite o vértice inicial para a busca em profundidade: ")
print("Busca em Profundidade:")
grafo.busca_em_profundidade(vertice_inicial)