'''
fecha: 11-12-2020
title: advent of code 2020
subtitle: day 6
author: Sebastián gonzález
github: ElSeaCL

Realizar el conteo de respuestas positivas por grupos. el primer problema 
cuenta la cantidad total de respuestas únicas, mientras que el segundo
cuanta la cantidad total de respuestas repetidas.
'''



def main():

    file = open('additional/input_d6.txt', 'r')
    char_group = []
    counter = 0
    for line in file:
        line = line.rstrip('\n')
        char_list = [char for char in line]
        char_group = char_group + char_list

        if line == '':
            counter += len(set(char_group))
            char_group = []

    counter += len(set(char_group))

    
    print("La cantidad total de respuestas unicas es de {}".format(counter))

    file = open('additional/input_d6.txt', 'r')
    char_group = []
    counter = 0
    for line in file:
        line = line.rstrip('\n')

        # Si se encuentra una linea en blanco
        if line == '':
            # Se retira el primer elemento de la lista
            set_ans = char_group.pop(0)
            set_ans = set_ans.intersection(*char_group)

            # Se realiza el conteo de elementos y se suma al contador
            counter = counter + len(set_ans)

            # Se resetean los contenedores
            char_list = []
            char_group = []

            # Se continua con el siguiente elemento
            continue
 
        char_list = [char for char in line]
        char_list = set(char_list)
        char_group.append(char_list)


    set_ans = char_group.pop(0)
    set_ans = set_ans.intersection(*char_group)
    counter = counter + len(set_ans)
                
    print("La cantidad total de respuestas intersección son {}".format(counter))

if __name__ == "__main__":
    main()
