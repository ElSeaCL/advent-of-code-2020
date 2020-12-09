'''
fecha: 09-12-2020
title: advent of code 2020
subtitle: day 3
author: Sebastián gonzález
github: ElSeaCL

Determinar con cuantos arboles de choca siguiendo un recorrido determinado bajando una montaña representada como un mapa.
'''
def tree_crash(movement):
    # Partimos definiendo las constantes para este problema, la posición inicial y 
    # el movimiento a efectuar. Ambos se definen como una tupla donde el primer
    # elemento es el eje X y el segundo el eje Y.

    INI_POS = 0, 0
    MOV = movement

    # Definimos el caracter del arbol
    TREE = '#'
    
    # Cargamos el mapa
    mapa = open('additional/input_d3.txt', 'r')
    
    # Y lo transformamos a una lista de strings
    mapa = list(mapa)
    mapa = [x.rstrip("\n") for x in mapa]
    
    # Conseguimos las dimensiones...
    Y_LEN = len(mapa)
    X_LEN = len(mapa[0])

    # ...e iniciamos el contador de arboles
    tree_counter = 0

    # Tomamos la posicion
    position = list(INI_POS)

    # Con todos estos datos podemos iniciar el bucle 
    while position[1] < Y_LEN:
        # Verificamos si es un arbol y contamos
        altura = mapa[position[1]]
        if altura[position[0]] is TREE:
                tree_counter += 1

        # Avanzamos
        position = [position[0] + MOV[0], position[1] + MOV[1]]

        # Verificamos si supera la longitud del map, si es así corregimos
        if position[0] >= X_LEN:
            position[0] = position[0] - X_LEN

    return tree_counter    

def main():
    resultado = 1
    
    # Listado de los movimientos a evaluar
    listado = [(1,1), (3,1), (5,1), (7,1), (1, 2)]
    for mov in listado:
        trees = tree_crash(mov)
        print("Para un movimiento de {} a la derecha y {} hacia abajo chocamos con {} arboles".format(mov[0], mov[1], trees))
        resultado = resultado * trees

    print("El resultado final es {}".format(resultado))


if __name__ == "__main__":
    main()
