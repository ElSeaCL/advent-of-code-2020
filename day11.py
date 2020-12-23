'''
fecha: 23-12-2020
title: advent of code 2020
subtitle: day 11
author: Sebastián gonzález
github: ElSeaCL

Siguiendo las reglas de uso/desuso de asientos en el área de espera de un terminal
de un ferry, determinar la cantidad de asientos acupados al momento en que no 
hayan más cambios.
'''

def input_seats(file):
    # Transforma el archivo del input en una array lineal de los asientos
    return ''.join([line for line in file])

def seats_data(seats):
    # Retorna los asientos como string único y devuelve el largo de cada fila original
    num_lines = seats.count('\n')
    seats = seats.replace('\n', '')
    len_lines = int(len(seats) / num_lines)
    return seats, len_lines

def cicle_seat(seats, len_lines):
    # Realiza un ciclo de cambio de estado en los asientos. Devuelve los asientos como string único.

    list_seat = [seat for seat in seats]

    def coord(n):
        # Devuelve las coordenadas del asiento en valores absolutos (0,0)
        n += 1
        y = n // 97
        x = n % 97
        if x == 0:
            y -= 1
            x = 97
        x -= 1
        return x, y

    def index_from_coord(coord):
        return 97 * coord[1] + coord[0]

    def vecindad(index):
        # Genera los indices de la vecindad tomando en cuenta los lìmites del string y aplica estos indices al string
        # generando así una lista con la vecindad para el indice especifico dado.
        
        index = coord(index)
        neighbor_factor = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
        
        return map(lambda indice: list_seat[indice], map(index_from_coord, [x for x in map(lambda factor: (index[0] + factor[0], index[1] + factor[1]), neighbor_factor) if x[0] >= 0 and x[0] <= 96 and x[1] >= 0 and x[1] <= 92]))

    def rules(seat, vecindad):
        # Toma la vecindad y retorna el cambio a realizar
        
        vec = list(vecindad)
        ocupados = vec.count('#')
        
        if seat == 'L' and ocupados == 0:
            return '#'
        elif seat == '#' and ocupados >= 4:
            return 'L'
        else:
            return seat
        
    new_seats = ''        
    for i in range(len(seats)):

        if seats[i] == '.':
            new_seats = new_seats + '.'
        else:
            vec = vecindad(i)
            new_seats = new_seats + rules(seats[i], vec)

    return new_seats

def main():
    
    file = open('additional/input_d11.txt', 'r')
    unformat_seats = input_seats(file)
    seats, len_lines = seats_data(unformat_seats)

    n_seats = ''
    nn_seats = seats
    counter = 0
    while seats != n_seats:
        seats = n_seats
        n_seats = cicle_seat(nn_seats, len_lines)
        nn_seats = n_seats
        counter += 1

    ocupados = n_seats.count('#')

    print('Se consiguienron los resultados estables tras {} ciclos\nAl final quedaron {} asientos ocupados'.format(counter, ocupados))
    
if __name__ == "__main__":
    main()
