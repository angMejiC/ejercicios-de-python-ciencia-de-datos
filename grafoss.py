import matplotlib.pyplot as plt
import networkx as nx

# Función de búsqueda voraz
def busqueda_voraz(grafo, heuristica, inicio, objetivo):
    from heapq import heappop, heappush
    
    # Cola de prioridad para nodos a visitar
    cola_prioridad = []
    # Añadimos el nodo inicial con su heurística
    heappush(cola_prioridad, (heuristica[inicio], inicio))
    
    # Diccionario para almacenar el camino más corto encontrado hasta cada nodo
    came_from = {}
    came_from[inicio] = None
    
    while cola_prioridad:
        # Sacamos el nodo con la menor heurística
        _, actual = heappop(cola_prioridad)
        
        # Si hemos llegado al objetivo, reconstruimos el camino
        if actual == objetivo:
            camino = []
            while actual:
                camino.append(actual)
                actual = came_from[actual]
            camino.reverse()
            return camino
        
        # Explorar los vecinos
        for vecino in grafo[actual]:
            if vecino not in came_from:
                # Registrar de dónde venimos y añadir a la cola de prioridad
                came_from[vecino] = actual
                heappush(cola_prioridad, (heuristica[vecino], vecino))
    
    return None  # Si no hay camino

# Definición del grafo
grafo = {
    'Logroño': {'Bilbao': 136, 'Burgos': 132, 'Soria': 100, 'Huesca': 239, 'Zaragoza': 170},
    'Bilbao': {'Huesca': 371, 'Burgos': 158, 'Logroño': 136},
    'Burgos': {'Logroño': 132, 'Madrid': 249, 'Bilbao': 158},
    'Soria': {'Logroño': 100, 'Guadalajara': 170, 'Madrid': 231},
    'Huesca': {'Logroño': 239, 'Zaragoza': 74, 'Bilbao': 371, 'Tarragona': 212},
    'Zaragoza': {'Logroño': 170, 'Huesca': 74, 'Tarragona': 236, 'Teruel': 170, 'Guadalajara': 256},
    'Teruel': {'Castellon': 144, 'Zaragoza': 170, 'Guadalajara': 244},
    'Guadalajara': {'Soria': 170, 'Madrid': 68, 'Cuenca': 136, 'Zaragoza': 256},
    'Madrid': {'Cuenca': 165, 'Guadalajara': 62, 'Soria': 231},
    'Tarragona': {'Huesca': 212, 'Castellon': 187, 'Zaragoza': 236},
    'Cuenca': {'Madrid': 165, 'Guadalajara': 136, 'Valencia': 199},
    'Castellon': {'Tarragona': 187, 'Teruel': 144, 'Valencia': 73}
}

# Definición de las heurísticas
heuristica = {
    'Logroño': 375,
    'Bilbao': 473,
    'Burgos': 424,
    'Soria': 311,
    'Huesca': 296,
    'Zaragoza': 246,
    'Teruel': 115,
    'Guadalajara': 270,
    'Madrid': 302,
    'Tarragona': 229,
    'Cuenca': 100,
    'Castellon': 60,
    'Valencia': 0
}

# Ejecución del algoritmo
inicio = 'Logroño'
objetivo = 'Valencia'
camino = busqueda_voraz(grafo, heuristica, inicio, objetivo)

# Imprimir el resultado
if camino:
    print("El camino más corto encontrado es:", " -> ".join(camino))
else:
    print("No se encontró un camino desde", inicio, "hasta", objetivo)

# Graficar el grafo y el camino más corto
G = nx.Graph()

# Añadir nodos y aristas al grafo
for nodo in grafo:
    for vecino, peso in grafo[nodo].items():
        G.add_edge(nodo, vecino, weight=peso)

# Posiciones de los nodos para el gráfico
pos = nx.spring_layout(G)

# Dibujar nodos y aristas
nx.draw_networkx_nodes(G, pos, node_size=500)
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)

# Dibujar etiquetas de los nodos
nx.draw_networkx_labels(G, pos, font_size=12, font_family="sans-serif")

# Dibujar el camino más corto en rojo
if camino:
    path_edges = list(zip(camino, camino[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=2, alpha=0.8, edge_color='r')

# Mostrar el gráfico
plt.title("Camino más corto desde Logroño hasta Valencia")
plt.show()
