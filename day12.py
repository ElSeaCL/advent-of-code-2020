'''
fecha: 26-12-2020
title: advent of code 2020
subtitle: day 12
author: Sebastián gonzález
github: ElSeaCL

Siguiendo las reglas de uso/desuso de asientos en el área de espera de un terminal
de un ferry, determinar la cantidad de asientos acupados al momento en que no 
hayan más cambios.
'''

INITIAL_POS = ('E', (0,0))
INITIAL_WAY = (10, 1)

# El diccionario de dirección incluye el codigo de la dirección según
# la nomenclatura usada originalmente, su equivalente como vector y
# está ordenado desde norte a este.
DIRECTION_VECTOR = {'N':(0,1), 'E':(1,0), 'S':(0,-1), 'W':(-1,0)}
DIR_LIST = list(DIRECTION_VECTOR.keys())


def input_movement(file):
    # Transforma el archivo en un generador de las distintas ordenes de
    # movimiento.

    for line in file:
        line = line.rstrip('\n')
        order = tuple([line[0], int(line[1:])])
        yield order

def order_transform(present_order, position):
    # Toma como argumentos la orden presente y la posición actual
    # y devuelve el vector de movimiento
    
    direction = present_order[0]
    n_position = [0,0]

    def vector_mov(direction, magnitude):
        mov = [0,0]
        dir_vector = DIRECTION_VECTOR[direction]
        mov[0], mov[1] = dir_vector[0] * magnitude, dir_vector[1] * magnitude
        return tuple(mov)
    
    if direction in DIRECTION_VECTOR:
        mov = vector_mov(direction, present_order[1])
        n_direction = position[0]
    elif direction == 'F':
        mov = vector_mov(position[0], present_order[1])
        n_direction = position[0]
    else:
        mov = (0,0)
        n_turn = int(present_order[1] // 90)
        if direction == 'R':
            turn = 1
        else:
            turn = -1
        
        index_dir = DIR_LIST.index(position[0])
        n_index = index_dir + turn * n_turn
        abs_index_turn = n_index % 4
        n_direction = DIR_LIST[abs_index_turn]

    n_position[0], n_position[1] = position[1][0] + mov[0], position[1][1] + mov[1]
    n_position = tuple(n_position)

    return n_direction, n_position

def order_transform_part2(present_order, position):
    # Para la parte 2 las reglas cambian. En este cas otenemos un
    # punto de referencia que guia la dirección del barco (wayfoward)
    # Las distintas ordes ahora mueven el wayfoward, solo F mueve el 
    # barco un numero de veces igual la wayfoward.
    # por lo tanto es necesario estar pendiente dle wayfoward y del
    # barco

    direction = present_order[0]
    magnitud = present_order[1]
    n_wayfoward = list(position[0])
    n_position = list(position[1])

    if direction == 'F':
        n_position[0], n_position[1] = n_position[0] + n_wayfoward[0] * magnitud,\
                n_position[1] + n_wayfoward[1] * magnitud
    elif direction in DIR_LIST:
        mov = DIRECTION_VECTOR[direction]
        n_wayfoward[0], n_wayfoward[1] = n_wayfoward[0] + mov[0] * magnitud,\
                n_wayfoward[1] + mov[1] * magnitud
    else:
        turns = magnitud // 90
        
        if direction == 'R':
            turn = 1
        else:
            turn = -1
            
        while turns > 0:
            old_way = n_wayfoward.copy()
            n_wayfoward[0] = old_way[1] * turn
            if old_way[1] == 0:
                n_wayfoward[1] = - turn * old_way[0]
                turns -= 1
                continue
            n_wayfoward[1] = int(-old_way[0] * n_wayfoward[0] / old_way[1])
            turns -= 1

    return tuple(n_wayfoward), tuple(n_position)

def move(position, order_list, part = 'part1'):
    for order in order_list:
        if part == 'part1':
            position = order_transform(order, position)
        else:
            position = order_transform_part2(order,position)
        order_list = order_list[1:]
        return move(position, order_list, part)

    return position

def main():
    
    file = open('additional/input_d12' , 'r')

    order_generator = input_movement(file)
    order_list = list(order_generator)
    order_list_p2 = order_list.copy()

    position = move(INITIAL_POS, order_list)

    print('La position final es {} mirando hacia {}'.format(position[1], position[0]))
    print('La distancia de Manhattan es: {}'.format(abs(position[1][0]) + abs(position[1][1])))
    
    # PART2
    initial_pos_p2 = INITIAL_WAY, INITIAL_POS[1]

    position = move(initial_pos_p2, order_list, part = 'part2')

    print('La posicion final en la parte 2 es {} con un wayfoward relativo a {}'.format(position[1], position[0]))
    print('La distancia de Manhattan es: {}'.format(abs(position[1][0]) + abs(position[1][1])))

    
if __name__ == "__main__":
    main()
