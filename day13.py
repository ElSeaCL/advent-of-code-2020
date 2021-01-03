'''
fecha: 01-01-2021
title: advent of code 2020
subtitle: day 13
author: Sebastián gonzález
github: ElSeaCL

Se cuenta con una lista de salidas de buses, hay que encontrar la salida más 
próxima al horario de interes para la primera parte.
En la segunda parte se solicita encontrar el horario màs temprano en el cual
tenemos salidas consecutivas de buses. Los buses X cuentan al momento de contar
los mínutos pero fuera de esto no imponen restricciones.
'''

def main():
    file = open('additional/input_d13', 'r')

    # Se obtiene la departura más próxima
    earliest = file.readline()

    # La lista de los buses
    dep_list = file.readline()

    # Realizamos copia del lista para el ejercicio dos
    dep_list_p2 = dep_list

    # Se realiza la limpieza y transformación de los datos
    earliest =int(earliest.rstrip('\n'))
    dep_list = dep_list.rstrip('\n')
    dep_list = [int(dep) for dep in dep_list.split(',') if dep.isdigit()]

    # El siguiente generador devuelve el timestamp más cercano a cada bus
    gen_min = map(lambda x: earliest + x - (earliest % x), dep_list)

    # Se une a su correspndiente codigo de bus como un zip
    dep_zip = zip(gen_min, dep_list)

    # Luego se filtra para obtener el valor menor
    solution = min(dep_zip)
    bus = solution[1]
    timestamp = solution[0]

    print('El bus más próximo es el que tiene código {} y el valor solicitado es:\n{}'.\
            format(bus, (timestamp - earliest) *bus))

    ### PARTE 2 ###

    dep_list = dep_list_p2.rstrip('\n')
    dep_list = dep_list.split(',')

    # Obtenemos los factores de tiempo para cada bus
    time_factor = []
    counter = 0
    for bus in dep_list:
        if bus != 'x':
            time_factor.append(counter)
        counter += 1

    dep_list = [int(dep) for dep in dep_list if dep.isdigit()]


    print(dep_list)
    print(time_factor)

    # Y luego los unimos con su código de bus respectivo
    bus_time = zip(dep_list, time_factor)
    bus_time = list(bus_time)

    n = 1
    #while True:
    #    if n% 10 == 0:
    #        print(n)
    #    bus_time_copy = bus_time
    #    flag = True
    #    ans_gen = map(lambda bus: (n + bus[1]) % bus[0], bus_time_copy)
    #    for ans in ans_gen:
    #        if ans != 0:
    #            flag = False
    #            break
    #    if flag is True:
    #        print('{} es la solución al problema 2'.format(n))
    #        break
    #    n += 1

    # Mètodo de máquina tragamonedas
    # Encontramos la frecuencia en la que se dan salidas consecutivas
    # primero de 2 buses y luego vamos aumentando

    # Iniciamos definiendo las funciones de mínimo común multiplo
    import math
    def lcm(a, b):
        return abs(a*b) // math.gcd(a, b)

    def lcm_adv(args):
        while True:
            lcm_num = lcm(args[0], args[1])
            args = args[2:]
            if len(args) == 0:
                return lcm_num
            args = [lcm_num] + args


    # Iniciamos un loop que toma la lista con los valores de n para cada bus
    # según su orden de salida, y en caso de obtener valores consecutivos de
    # salida, avanza al siguiente par tomando como incremento el m.c.m de los
    # buses comparados al momento.
    i = 0
    increment = 1
    while True:
        flag = True
        bus_time_copy = bus_time
        time_abs = [n + x[1] for x in bus_time_copy]    
        if time_abs[i] % dep_list[i] == 0 and \
                time_abs[i+1] % dep_list[i+1] == 0:
            increment = lcm_adv(dep_list[0:(i+2)])
            i += 1
            if i >= len(time_abs) - 1:
                break
        n += increment

    print('El valor final es {}'.format(n)) 
            
if __name__ == "__main__":
    main()
