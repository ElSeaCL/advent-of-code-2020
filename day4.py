'''
fecha: 09-12-2020
title: advent of code 2020
subtitle: day 4
author: Sebastián gonzález
github: ElSeaCL

A partir de un registro de passportes, identificar cuantos son incorrectos por
no contar con toda la información necesaria.
'''

def line_to_dict(line):
    line = line.rstrip(' ').lstrip(' ').split()
    line = [x.split(':') for x in line]
    line = {x[0]:x[1] for x in line}

    return line

def passport_format(file):
    '''
    Como parámetro toma un listado de pasaportes y formatea la información
    como un diccionario donde cada key pertenece a uno de los atributos
    posible.

    param: text file
    return: list de diccionario donde cada diccionario es un passport
    '''
    '''
    Se ve horrible...lo sé, seguramente hay una forma más elegante y eficiente
    de pasar estos datos en forma de diccionario. Aun así esta función logra
    su cometido, así que la dejaré tranquilita por ahora
    '''

    # Iniciamos la lista que va a contener los pasaportes formateados
    passport_list = []
    
    # Iniciamos una lista que contendra los pasaportes individuales
    passport_line = ""

    # Se lee la primera linea
    line = file.readline()

    while line:
        line = line.rstrip('\n')
        line = line + ' '
        if line == ' ':
            # Si no topamos con una linea en blanco se agrega el pasaporte 
            # a la lista principal y se reinicia la variable
            passport_line = line_to_dict(passport_line)
            passport_list.append(passport_line)
            passport_line = ""
        
        passport_line = passport_line + line

        # Leemos la siguiente linea para repetir el ciclo
        line = file.readline()

    # Ya que usamos '\n' para definir el cierre de datos para el pasaporte, pasa que el último lo
    # terminamos descartando. Se agregan estas dos últimas lineas para evitar esto.
    passport_line = line_to_dict(passport_line)
    passport_list.append(passport_line)

    return passport_list


def is_valid_passport(passport):
    '''
    Toma como argumento un pasaporte en formato valido (diccionario field:value)
    y devuelve si contiene los campos requeridos o no.
    '''
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    passport_keys = list(passport.keys())
    
    # Se comparan ambas, si tienen los mismos campos entonces el pasaporte es valido
    required_fields.sort()
    passport_keys.sort()
    
    try:
        passport_keys.remove('cid')
    except:
        pass

    is_valid = (required_fields == passport_keys)

    return is_valid

def is_valid_value(passport):
    '''
    En este caso creo que es conveniente definir las funciones de comparación y luego
    llamarlas mediante un switch-case. De este modo no repito tanto código.

    En caso de que uno de los requerimiento no se cumpla se rompe el loop y se devuelve
    inmediatamente un False.
    '''

    def year_value(year1, year2):
        
        return True

    def number_digit(num):

        return True

    def 


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
