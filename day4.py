'''
fecha: 09-12-2020
title: advent of code 2020
subtitle: day 4
author: Sebastián gonzález
github: ElSeaCL

A partir de un registro de passportes, identificar cuantos son incorrectos por
no contar con toda la información necesaria.
'''

def passport_format(file):
    '''
    Como parámetro toma un listado de pasaportes y formatea la información
    como un diccionario donde cada key pertenece a uno de los atributos
    posible.

    param: text file
    return: list de diccionario donde cada diccionario es un passport
    '''
    
    return passport_list


def is_valid_passport():

    return is_valid

def main():
    # Iniciamos cargando el archivo
    file = open(r'additional/input_d4.txt','r')

    # Luego formateamos este archivo 
    passport_list = passport_format(file)
    
    # Una vez que tenemos los pasaportes en el formato adecuado vemos uno por
    # uno si cumple con los criterios
    
    valid = 0

    for passport in passport_list:
        valid = valid + is_valid_passport(passport)

    print("Los pasaportes validos en la lista son {}".format(valid))

if __name__ == "__main__":
    main()
