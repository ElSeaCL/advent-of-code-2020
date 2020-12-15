'''
fecha: 14-12-2020
title: advent of code 2020
subtitle: day 8
author: Sebastián gonzález
github: ElSeaCL

Realizar el conteo de respuestas positivas por grupos. el primer problema 
cuenta la cantidad total de respuestas únicas, mientras que el segundo
cuanta la cantidad total de respuestas repetidas.
'''

def instruction_set(file):
    # transforma el archivo de instrucciones en una lista

    instructions = []
    for line in file:
        line = line.rstrip('\n').split()
        line[1] = int(line[1])
        instructions.append(line)

    return instructions



def single_value_instruction(file):
    # Variables iniciales
    accumulator = 0
    instructions = file
    instruction_run = []
    position = 0

    while position not in instruction_run:

        # La instruccion presente
        present_inst = instructions[position]

        # Se agregega la instrucción a la lista de instrucciones corridas
        instruction_run.append(position)

        # Se ejecuta la instrucción        
        print('Se ejecuta la instrucción position {} que corresponde a:\nCódigo: {}\nNúmero: {}\n'.format(position, present_inst[0], present_inst[1]))

        if present_inst[0] == 'acc':
            accumulator += present_inst[1]
        elif present_inst[0] == 'jmp':
            position += present_inst[1] - 1

        # Se salta a la siguiente posición
        position += 1

        if position == 617:
            position = 0
            return 0

    print('El acumulador al momento de repetirse la instrucción es {}'.format(accumulator))

    return position - 1


def main():
    accumulator = 0
    file = open('additional/input_d8.txt', 'r')
    instructions = instruction_set(file)
    # El nùmero de la última instruccion
    last_inst = 616

    last_value = 1

    while last_value != 0:
        copy_instructions = instructions[:]
        for inst in copy_instructions:
            if 


    


if __name__ == "__main__":
    main()
