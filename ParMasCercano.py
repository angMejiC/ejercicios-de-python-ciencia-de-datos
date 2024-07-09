import math
import matplotlib.pyplot as plt
import time
import random

# Calcula la distancia entre dos puntos en el plano
def distancia(p, q):
    d = math.sqrt((q[0] - p[0]) ** 2 + (q[1] - p[1]) ** 2)
    return d

# Encuentra los dos pares más cercanos y la distancia entre ellos
def fuerza_bruta(listaPares):
    numPares = len(listaPares)
    disMinima = math.inf
    paresCercanos = []
    for i in range(numPares):
        for j in range(i + 1, numPares):
            disTemporal = distancia(listaPares[i], listaPares[j])
            if disTemporal < disMinima:
                disMinima = disTemporal
                paresCercanos = [listaPares[i], listaPares[j]]
    return paresCercanos, disMinima

# Organiza una lista de tuplas (x, y). Si coordenada = 0, el ordenamiento se realiza según x; si coordenada = 1, se realiza según y.
def ordenar_lista(listaPares, coordenada):
    return sorted(listaPares, key=lambda x: x[coordenada])

# Función principal que encuentra el par más cercano utilizando el método de divide y vencerás
def encontrar_pares_cercanos(listaPares):
    def _closest_pair_rec(Px, Py):
        if len(Px) <= 3:
            return fuerza_bruta(Px)

        mid = len(Px) // 2
        Qx = Px[:mid]
        Rx = Px[mid:]
        midpoint = Px[mid][0]

        Qy = list(filter(lambda x: x[0] <= midpoint, Py))
        Ry = list(filter(lambda x: x[0] > midpoint, Py))

        (p1, q1), dis1 = _closest_pair_rec(Qx, Qy)
        (p2, q2), dis2 = _closest_pair_rec(Rx, Ry)

        if dis1 <= dis2:
            dmin = dis1
            min_pair = (p1, q1)
        else:
            dmin = dis2
            min_pair = (p2, q2)

        (p3, q3), dis3 = closest_split_pair(Px, Py, dmin, min_pair)

        if dmin <= dis3:
            return min_pair, dmin
        else:
            return (p3, q3), dis3

    def closest_split_pair(Px, Py, delta, best_pair):
        len_x = len(Px)
        mx = Px[len_x // 2][0]
        Sy = [x for x in Py if mx - delta <= x[0] <= mx + delta]

        best = delta
        len_Sy = len(Sy)
        for i in range(len_Sy - 1):
            for j in range(i + 1, min(i + 7, len_Sy)):
                p, q = Sy[i], Sy[j]
                dist = distancia(p, q)
                if dist < best:
                    best_pair = (p, q)
                    best = dist
        return best_pair, best

    Px = ordenar_lista(listaPares, 0)
    Py = ordenar_lista(listaPares, 1)
    return _closest_pair_rec(Px, Py)

# Genera una lista de puntos aleatorios
def generar_puntos(n):
    return [(random.uniform(0, 1000), random.uniform(0, 1000)) for _ in range(n)]

# Ejemplo de uso
listaPares = generar_puntos(30)
inicio = time.time()
paresCercanos, distanciaMinima = encontrar_pares_cercanos(listaPares)
fin = time.time()

print("Pares más cercanos:", paresCercanos)
print("Distancia mínima:", distanciaMinima)
print("Tiempo de ejecución:", fin - inicio, "segundos")

# Graficar los puntos y el par más cercano
x, y = zip(*listaPares)
plt.scatter(x, y)
px, py = zip(*paresCercanos)
plt.plot(px, py, 'r-')
plt.show()