'''
title: Advent of code
subtitle: day 7
author: Sebastián González
date: 11-12-20
github: ElSeaCL
'''

def bag_rule(line_rule):
    '''
    Toma una regla individual y devuelve el saco principal junto a un 
    diccionario compuesto por los sacos que pueden ir dentro del
    principal y su cantidad.
    '''
    line = line_rule.split('bags')
    line.pop(-1)

    # Obtenemos la key principal, el nombre del saco que contiene los otros
    key = line.pop(0).rstrip()

    # Obtenemos la lista de sacos que están contenidos en le principal
    # y la cantidad de sacos que se pueden almacenar
    keys_list = []
    values_list = []
    for rule in line:
        rule = rule.rstrip().split()
        bag_key = rule[-2] + ' ' + rule[-1]
        value = rule[-3]

        keys_list.append(bag_key)
        values_list.append(value)
    
    # Se crea un diccionario con los sacos y cantidad de lo contenido
    # en el principal
    dict_bags = {keys_list[i]:values_list[i] for i in range(len(keys_list))}

    return key, dict_bags

def rule_dict(file):
    '''
    A partir del listado total de reglas, genera un diccionario con los distintos
    sacos y lo que pueden contener según el formato definido en la función anterior.
    '''
    rules_dict = {}

    for line in file:
        rules = bag_rule(line)
        rules_dict[rules[0]] = rules[1]

    return rules_dict


# Como variable global para el scrip obtenemos el diccionario de las reglas
file = open('additional/input_d7', 'r')
rules_dict = rule_dict(file)


def bag_contains(bag):
    '''
    Como argumento usa un nombre valido de saco y obtiene
    todos los distintos sacos que pueden ser almacenados diresta he indirectamente
    en el.
    '''
    
    final_list = []

    

    








def main():
    return True


if __name__ == '__main__':
    main()

