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
    # Comenzamos definiendo las distintas funciones que realizaran el chequeo
    # Estas contienen las reglas a verificar.

    # Verificación de atributos por año
    def year_value(year_passport, year1, year2):
        try:
            year_passport = int(year_passport)
        except:
            return False

        if (year_passport >= year1) and (year_passport <= year2):
            return True
        else:
            return False

    # Verificación por altura
    def height_value(height, *unused):
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

    # Verificación de color de pelo
    def hair_value(hair_color, *unused):
        values = '0123456789abcdef'

        if hair_color[0] != '#':
            return False
        
        hair_color = hair_color[1:]

        for char in hair_color:
            if char not in values:
                return False

        return True

    # Verificación de color de ojos
    def eye_value(eye_color, *unused):
        values = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

        if eye_color in values:
            return True
        else:
            return False
        
    # Verificación de id
    def id_value(passport_id, *unused):
        if len(passport_id) != 9:
            return False
        return passport_id.isnumeric()
    
    # Verificación de id del país
    def cid_value(country_id, *unused):
        return True


    def switch_casos(argumento):
        # Definimos el diccionario con los casos
        func_dict = {
             'byr' : [year_value, 1920, 2002],
             'iyr' : [year_value, 2010, 2020],
             'eyr' : [year_value, 2020, 2030],
             'hgt' : [height_value],
             'hcl' : [hair_value],
             'ecl' : [eye_value],
             'pid' : [id_value],
             'cid' : [cid_value]
             }
        
        # Obtengo la función del diccionario
        func_list = func_dict.get(argumento, lambda: "Invalid attribute")
        
        return func_list

    # Leo los atributos del pasaporte recibido
    for atributo in passport:
        func_list = switch_casos(atributo)
        
        if func_list[0](passport[atributo], *func_list[1:]) is False:
            return False

    return True


def main():
    # Iniciamos cargando el archivo
    file = open(r'additional/input_d4.txt','r')

    # Luego formateamos este archivo 
    passport_list = passport_format(file)
    
    # Una vez que tenemos los pasaportes en el formato adecuado vemos uno por
    # uno si cumple con los criterios
    
    valid = 0
    first_passport_filter = []

    for passport in passport_list:
        # Primer filtro, si contiene todos los atributos mínimos
        result = is_valid_passport(passport)
        if result is True:
            # Segundo filtro, si los valores de dichos atributos cumple
            # con las reglas
            valid = valid + is_valid_value(passport)

    print("Los pasaportes validos en la lista son {}".format(valid))

if __name__ == "__main__":
    main()
