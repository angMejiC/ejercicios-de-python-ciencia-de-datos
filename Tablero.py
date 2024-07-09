CONFIG_INICIAL = [1,2,3,4,5,6,16,8,9,10,7,11,13,14,15,12]
CONFIG_FINAL = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]


def comprobar(lista):
  m=0
  for i in range(16):
    for j in range(i+1,16):
      if lista[j] < lista [i]:
        m += 1

  casillas_verdes = [1,3,4,6,9,11,12,14]
  pos_hueco = lista.index(16) 

  if pos_hueco in casillas_verdes:
   m += 1
  print(m)
    





def mostrar_tablero(lista, n):
    print("")
    for i in range(n+1):
      for j in range(n):
         print("+----+", end="")
      print("")
      if i < n:
       for j in range(n):
         print("| {:2d} |".format(lista[i*n+j]), end="")
      print("")

mostrar_tablero(CONFIG_INICIAL, 4)
