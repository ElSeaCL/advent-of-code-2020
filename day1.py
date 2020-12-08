'''
Como ya me spoile la soluciòn sencilla que utiliza combinatios de la
libreria itertools, voy a implementar mi solución màs artesanal
pero igual de efectiva.

Parte la funcion limpiando los valores que sabemos que no pueden
sumar 2020.

Luego se forma una matriz de n*n con n igual al largo de la lista,
los valores de este son una repeticion de los vavlores de la lista.

A partir de la matriz se forma la transpuesta, luego se suman ambas
y se busca el resultado deseado.
'''

# Para poder trabajar con matrices
import numpy as np

def suma2020(lista):
    # Primero vamos a ordenar la lista de menor a mayor
    lista.sort()

    # Luego tomamos el elemento menor de la lista y vemos si la suma es menor
    # que el valor objetivo (2020) entonces eliminamos este elemento y seguimos
    for x in lista:
        if x + lista[-1] < 2020:
            lista.pop(0)
        else:
    # Una vez reducida la lista contamos la cantidada de elementos para formar
    # una matriz de n * n
            n = len(lista)
            listaRep = [lista for x in range(n)] 

    # Una vez formada la lista de listas se puede transformar en una matriz
            listaMat = np.array(listaRep)

    # Y a partir de esta formamos la transpuesta
            listaTrans = np.matrix.transpose(listaMat)

    # Finalmente con esto generamos la matriz con todas las posibles sumas
            resultados = listaMat + listaTrans

    # Ya con esta matriz podemos encontrar los puntos que dan el objetivo
            indices = np.where(resultados == 2020)

    # Y como solo nos interesaa una opciòn tomamos el primer resultado
            indices = indices[0]

    # Y ahora podemos devolver el resultado
            return lista[indices[0]] * lista[indices[1]]

import itertools as it
def suma2020iter(lista):
    for a, b in it.combinations(lista, 2):
        if a + b == 2020:
            return a * b


