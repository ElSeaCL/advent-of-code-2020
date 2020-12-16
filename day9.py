'''
fecha: 15-12-2020
title: advent of code 2020
subtitle: day 9
author: Sebastián gonzález
github: ElSeaCL

Realizar el conteo de respuestas positivas por grupos. el primer problema 
cuenta la cantidad total de respuestas únicas, mientras que el segundo
cuanta la cantidad total de respuestas repetidas.
'''
import itertools as it

def encode_list(file):
    encode_list = []
    for line in file:
        line.rstrip('\n')
        encode_list.append(int(line))

    return encode_list

def check_value(value_list):
    '''
    Mediante itertools.combinations revisa si existen combinaciones
    que sumen el valor verificado a partir del rango de la lista (25 números
    antes del verificado. Si se encuentra una opción entonces el indicador cambia a True
    Si no se encuentra una opción se mantiene en False. Al salir del loop si este sigue
    en False Se retorna el valor.
    '''
    
    for x in range(25,1000):
        # Valor a verificar
        check_value = value_list[x]
        # Lista donde se deben encontrar los valores a sumar
        check_list = value_list[x - 25 : x]
        # Indicador que cambia al encontrar una suma viable    
        indicator = False

        for a, b in it.combinations(check_list, 2):
            if a + b == check_value:
                #print("{} y {} suman el valor {} del indice {}".format(a, b, check_value, x))
                indicator = True
                break
        # Si no se encuentra una suma viable se devuelve el valor verificado
        if indicator is False:
            return check_value
    return 0
            
def main():
    
    file = open('additional/input_d9', 'r')
    lista = encode_list(file)

    valor = check_value(lista)

    print('El valor que no cuadra con el encoding es {}'.format(valor))

    index_value = lista.index(valor)
    option_list = lista[index_value - 25 : index_value]

    for i in range(0,24):
        for j in range(1,25):
            suma = sum(option_list[i:j]
            if suma == valor:
                    return i, j
            elif suma < 
    
if __name__ == "__main__":
    main()
