'''
Desafío día 2
autor: Sebastián González
fecha: 08-12-2020

Desafío consta de determinar de una lista de passwords cuales no cumplen con su
protocolo.
'''

# Definimos la función que toma 1 linea, lee las reglas de su protocolo y
# determina si el password cumple con ellas.

def password_split(line):
    # Primero se separa el password del protocolo
    # Se separa por medio del espacio
    lista = line.split(" ")

    # Se obtiene el caracter a buscar
    caracter = lista[1][0]

    # Se obtiene el password
    passwd = lista[2]

    # Mínimo y máximo de caracteres
    min_caracter = int(lista[0].split("-")[0])
    max_caracter = int(lista[0].split("-")[1])

    return min_caracter, max_caracter, caracter, passwd

def number_char_validation(line):
    # Se obtienen los distintos elementos
    min_char, max_char, char, passwd = password_split(line)

    # Se verifica si el passwoord cumple con las reglas de numero de caracteres 
    cantidad = passwd.count(char)

    if cantidad < min_char or cantidad > max_char:
        return False
    else:
        return True

def position_char_validation(line):
    # Se obtienen los distintos elementos
    min_char, max_char, char, passwd = password_split(line)
    
    position_1 = passwd[min_char - 1]
    position_2 = passwd[max_char - 1]

    # Se compara ambos caracteres, la suma de ambas comparaciones debe ser 1
    comparation_1 = position_1 == char
    comparation_2 = position_2 == char

    if (comparation_1 + comparation_2) == 1:
        return True
    else:
        return False


def main():
    passwd_list = open("additional/passwd_d2", 'r')

    counter = 0
    for line in passwd_list:
        counter = counter + position_char_validation(line)

    print("Cantidad de passwords validos: {}".format(counter))


if __name__ == "__main__":
    main()

