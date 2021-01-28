'''
fecha: 01-01-2021
title: advent of code 2020
subtitle: day 13
author: Sebastián gonzález
github: ElSeaCL

Siguiendo las reglas de uso/desuso de asientos en el área de espera de un terminal
de un ferry, determinar la cantidad de asientos acupados al momento en que no 
hayan más cambios.
'''

from itertools import permutations

def readfile(file):
    # Devuelve una lista con las direcciones de cada uno de los
    # numeros y un zip de los pares mask, number
    address_list = []
    mask_list = []
    num_list = []

    with open('additional/input_d14', 'r') as instructions:    
        for line in instructions:
            line = line.rstrip('\n')
            if line[:4] == 'mask':
                mask = line[7:]
            else:
                pair = line.split(' = ')
                add = pair[0][4:-1]
                num = pair[1]

                address_list.append(add)
                mask_list.append(mask)
                num_list.append(int(num))

    mask_zip = zip(mask_list, num_list)
    return address_list, mask_zip


def mask_to_num(mask, number, tipo='numero'):
    # Toma la mascara, se la aplica al numero y devuelve el numero nuevo
    
    # Primero se transforma en binario string y se retira los dos primeros char
    number = bin(number)[2:]

    # Se ve la diferencia de caracteres con la mascara y se rellenan al 
    # principio del numero con 0s
    relleno = '0' * (36 - len(number))
    number = relleno + number

    n_num = ''
    if tipe == 'number':
        for x in zip(mask, number):
            if x[0] == 'X':
                char = x[1]
            else:
                char = x[0]
            n_num = n_num + char
    else:
        for x in zip(mask, number):
            if x[0] == 'X':
                char = 'X'
            elif x[0] == '1':
                char = '1'
            else:
                char = x[1]

    return n_num

def get_possible_mem(mem_num):
    # Utilizare permutation donde cada X sera reemplazada por un [0, 1] obteniendo asílas posibles
    # opciones como un generador.

    num_expanded = [[0,1] for x in mem_num if x == 'X']


def main():
    file = open('additional/input_d14', 'r')
    address, mask_num = readfile(file)
    result_dict = dict()
    index = 0

    for pair in mask_num:
        n_num = mask_to_num(*pair)
        n_num = '0b' + n_num
        n_num = int(n_num, 2)
        result_dict[address[index]] = n_num
        index += 1

    counter = sum(list(result_dict.values()))

    print('La suma total es {}'.format(counter))
    

if __name__ == "__main__":
    main()
