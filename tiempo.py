import time
import sys
from f_cola import f_cola
from f_recursiva import f_recursiva
from f_iter import f_iter
sys.setrecursionlimit(2000)
# codigo para obtener el tiempo que toma cada implementacion de F con distintos valores de n
# por la naturaleza de cada implementacion, se usaran distintos valores para realizar las pruebas
valoresIter = [50000,100000,150000,200000,250000,300000]
valoresCola = [500,700,900,1100,1300,1500]
valoresRec = [100,120,140, 160, 180, 200]
tiemposRecursiva = []
tiemposCola = []
tiemposIter = []

for valor in valoresRec:
    tiempoInicio = time.time()
    f_recursiva(valor)
    tiemposRecursiva.append(time.time() - tiempoInicio)

for valor in valoresCola:
    tiempoInicioCola = time.time()
    f_cola(valor)
    tiemposCola.append(time.time() - tiempoInicioCola)

for valor in valoresIter:
    tiempoInicioIter = time.time()
    f_iter(valor)
    tiemposIter.append(time.time() - tiempoInicioIter)

print("Tiempo de la implementacion recursiva :")
print(tiemposRecursiva)
print("Tiempo de la implementacion recursiva de cola:")
print(tiemposCola)
print("Tiempo de la implementacion iterativa:")
print(tiemposIter)


