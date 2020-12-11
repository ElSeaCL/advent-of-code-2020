'''
title: Desafío día 5
autor: Sebastián González
fecha: 11-12-2020

Primera parte del desafío consta en codificar el número de fila y columna 
de cada asiento en la lista, obtener su id y determinar el mayor.ñ

'''

def seat_coder(code):
    '''
    Determina a partir del código de 10 caracteres en número de fila y
    columna del asiento. Devuelve una tuple de (row, column)
    '''
    # Dado que estamos tratando con código binario transformamos las
    # letras en 1s y 0s
    dict_code = {
            'F':'0',
            'B':'1',
            'R':'1',
            'L':'0'
            }

    # Con el diccionario taducimos el código
    for char in dict_code:
        code = code.replace(char, dict_code[char])

    # Ya con el código en modo binario traducimos a decimal
    row = int(code[:7], 2)
    col = int(code[7:], 2)

    return (row, col)

def id_seat(code):

    row_col = seat_coder(code)
    return row_col[0] * 8 + row_col[1]


def main():
    from collections import Counter

    highest_id = 0
    seat_list = []    

    for line in open('additional/input_d5.txt', 'r'):
        line = line.rstrip('\n')
        
        seat_list.append(seat_coder(line))

        new_value = id_seat(line)
        
        if new_value > highest_id:
            highest_id = new_value

    # Para el segundo desafío se deben identificar las filas que tengan 
    # menos de 8 mas de 1. Con este dato vemos que de esta selección
    # que filas tienen un asiento vacio con sus adyacentes usados
    
    used_seats_row = Counter(elem[0] for elem in seat_list)
    options_row = [k for k,v in used_seats_row.items() if v > 1 and v < 8]


    options = list(range(0,8))
    
    # Para cada opción de row se ven sus columnas usadas
    for row in options_row:
        list_cols = [cols for rows, cols in seat_list if rows == row]
        unused_cols = set(options) - set(list_cols)
        col , *_ = unused_cols
        
        print("El asiento desocupado es la fila {} y columna {}".format(row, col))
        print("El id de este es {}".format(row*8+col))


    print("El id de asiento más alto es {}".format(highest_id))


if __name__ == "__main__":
    main()

