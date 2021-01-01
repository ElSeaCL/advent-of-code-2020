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

if __name__ == "__main__":
    main()
