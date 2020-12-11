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

    def year_value(year_passport, year1, year2):
        try:
            year1 = int(year1)
            year2 = int(year2)
        except:
            return False

        if (year_passport >= year1) and (year_passport <= year2):
            return True
        else:
            return False

    def height_value(height):
        unit = height[-2:]
        valor = height[:-2]
        
        try:
            valor = int(valor)
        except:
            return False

        if unit == 'cm':
            required = [150, 193]
        elif unit == 'in':
            required = [59, 76]
        else:
            return False

        if valor >= required[0] and valor <= required[1]:
            return True
        else:
            return False

    def hair_value(hair_color):
        values = '0123456789abcdef'

        if hair_color[0] != '#':
            return False
        
        hair_color = hair_color[1:]

        for char in hair_color:
            if char not in values:
                return False

        return True

    def eye_value(eye_color):
        values = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

        if eye_color in values:
            return True
        else:
            return False
        
    def id_value(passport_id):
        return passport_id.isnumeric()
    
    def cid_value(country_id):
        return True

   # Definimos el diccionario con los casos
   dict = {
        'byr' : [year_value, 1920, 2002],
        'iyr' : [year_value, 2010, 2020],
        'eyr' : [year_value, 2020, 2030],
        'hgt' : [height_value],
        'hcl' : [hair_value],
        'ecl' : [eye_value],
        'pid' : [id_value],
        'cid' : [cid_value]
        }


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
