from collections import deque
import heapq

# Configuración final
CONFIG_FINAL = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def comprobar(lista):
    m = 0
    for i in range(16):
        for j in range(i + 1, 16):
            if lista[j] < lista[i] and lista[j] != 16:
                m += 1

    casillas_verdes = [1, 3, 4, 6, 9, 11, 12, 14]
    pos_hueco = lista.index(16)

    if pos_hueco in casillas_verdes:
        m += 1

    return m % 2 == 0

def mostrar_tablero(lista, n):
    print("")
    for i in range(n):
        print("+----" * n + "+")
        for j in range(n):
            if lista[i * n + j] == 16:
                print("|    ", end="")
            else:
                print("| {:2d} ".format(lista[i * n + j]), end="")
        print("|")
    print("+----" * n + "+")

def encontrar_vecinos(configuracion):
    vecinos = []
    pos_vacia = configuracion.index(16)
    fila_vacia, col_vacia = pos_vacia // 4, pos_vacia % 4

    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Arriba, abajo, izquierda, derecha

    for mov in movimientos:
        nueva_fila, nueva_col = fila_vacia + mov[0], col_vacia + mov[1]
        if 0 <= nueva_fila < 4 and 0 <= nueva_col < 4:
            nueva_pos = nueva_fila * 4 + nueva_col
            nueva_config = configuracion[:]
            # Intercambiar la posición vacía con la nueva posición
            nueva_config[pos_vacia], nueva_config[nueva_pos] = nueva_config[nueva_pos], nueva_config[pos_vacia]
            vecinos.append(nueva_config)

    return vecinos

#Con el siguiente metodo lo que vamos hacer es caclular la diastancia entre el camino mas corto del estado actual =(x1,y1) y (x2,y2)
#es la suma de las diferencias absolutas de sus coordenadas. Distancia = |x1-x2| + |y1-y2|///
def heuristica_manhattan(config):
    distancia = 0
    for i in range(16):
        if config[i] != 16:
            fila_actual, col_actual = divmod(i, 4)
            fila_objetivo, col_objetivo = divmod(config[i] - 1, 4)
            distancia += abs(fila_actual - fila_objetivo) + abs(col_actual - col_objetivo)
    return distancia

def resolver_15_puzzle(config_inicial, config_final):
    if not comprobar(config_inicial):
        print("La configuración inicial no es alcanzable desde la configuración objetivo.")
        return

    cola = [(heuristica_manhattan(config_inicial), 0, config_inicial, [])]
    visitados = set()
    heapq.heapify(cola)

    while cola:
        costo_estimado, costo_acumulado, config_actual, camino = heapq.heappop(cola)

        if config_actual == config_final:
            print("Configuración alcanzada!")
            for paso, config in enumerate(camino + [config_actual]):
                print(f"Paso {paso}:")
                mostrar_tablero(config, 4)
            return

        if tuple(config_actual) in visitados:
            continue

        visitados.add(tuple(config_actual))
        vecinos = encontrar_vecinos(config_actual)

        for vecino in vecinos:
            if tuple(vecino) not in visitados:
                nuevo_camino = camino + [config_actual]
                nuevo_costo_acumulado = costo_acumulado + 1
                heapq.heappush(cola, (nuevo_costo_acumulado + heuristica_manhattan(vecino), nuevo_costo_acumulado, vecino, nuevo_camino))

    print("No se encontró solución.")

def leer_configuracion(mensaje):
    while True:
        entrada = input(mensaje)
        try:
            configuracion = [int(x) for x in entrada.split()]
            if len(configuracion) == 16 and set(configuracion) == set(range(1, 17)):
                return configuracion
            else:
                print("Por favor, ingrese exactamente 16 números del 1 al 16.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese 16 números separados por espacios.")

# Leer configuración inicial del usuario
print("Ingrese la configuración inicial del 15 Puzzle (16 números del 1 al 16 separados unicamente por espaciadora, con el espacio vacío representado por 16):")
CONFIG_INICIAL = leer_configuracion("Configuración inicial: ")

# Configuración final predeterminada
CONFIG_FINAL = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# Mostrar configuración inicial
print("Configuración inicial:")
mostrar_tablero(CONFIG_INICIAL, 4)

# Resolver el puzzle
resolver_15_puzzle(CONFIG_INICIAL, CONFIG_FINAL)
