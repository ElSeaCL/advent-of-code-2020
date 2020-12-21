'''
fecha: 17-12-2020
title: advent of code 2020
subtitle: day 10
author: Sebastián González
github: ElSeaCL

Realizar el conteo de respuestas positivas por grupos. el primer problema 
cuenta la cantidad total de respuestas únicas, mientras que el segundo
cuanta la cantidad total de respuestas repetidas.
'''
OUTLET_JOLT = 0

def adapter_list(file):
    adap_list = []
    for line in file:
        line = int(line.rstrip('\n'))
        adap_list.append(line)

    return adap_list

def jolt_difference(adapters):
    adapters.sort()
    dif_dict = {}
    jolt = OUTLET_JOLT
    for adapter in adapters:
        dif = adapter - jolt
        if dif not in dif_dict:
            dif_dict[dif] = 1
        else:
            dif_dict[dif] += 1
        jolt = adapter

    # Se agrega una diferencia de 3 que corresponde al valor de dif del celular
    dif_dict[3] += 1

    return dif_dict

def different_combinations(adapters):
    
    start = OUTLET_JOLT
    finish = max(adapters)
    
    # Cualquier combinación valida, la sumatoria entre las diferencias
    # inmediatas debe dar igual a finish - start

    # Una idea momentanea: Crear un diccionario donde cada key sea una de las 
    # diferencias posibles y el valor sea una lista de tuples, cada una con los 
    # dos valores que definen la diferencia. Esta primera estructura nos dará
    # los boques para construcir las distintas listas respuestas.
    # a partir de este diccionario se construyen listas que deben cumplir con
    # los dos siguientes requisitos para que sean una respuesta correcta:
    #   1.- Una de las tuples debe contener un mìnimo viables (1, 2 o 3) para
    #       conectarse con la funete de poder.
    #   2.- Una de lasa tuples debe contener el valor màximo de los adaptadores
    #   3.- La suma de todas diferencias (suma de los keys de cada uno de las
    #       tuples) debe ser equivalente a valor del finish - start
    #   4.- Nùmeros en la misma posicion no se pueden repetir.

    # Creamos el diccionario
    dif_dict = {1: [], 2: [], 3: []}

    import itertools as it

    for a, b in it.combinations(adapters, 2):
        dif = b - a
        if dif > 0 and dif < 4:
            dif_dict[dif].append((a,b))




    return dif_dict

def dif_combinations(adapters):
    start = OUTLET_JOLT
    finish = max(adapters)
    total_dif = finish - start
    min_list = total_dif // 3
    adapters.sort()

    answers = []

    import itertools as it
    
    for i in range(5, len(adapters)):

        print('numero de elementos {}'.format(i))
        for combination in it.combinations(adapters, i):
            comb = start, *combination
            #if comb[1] - start > 3:
             #    continue
            if finish not in comb:
                continue
            dif_list = []
            for j in range(1, i+1):
                checker = True
                dif = comb[j] - comb[j - 1]
                if dif > 3:
                    checker = False
                    break
                dif_list.append(dif)
            if checker is False:
                continue
                #if sum(dif_list) != (finish - start):
                #    continue
            yield comb

def combination_gen(lista, n):
    # Crea un generador que devuelve una de las combinaciones posibles
    # a partir de una lista de nùmeros y el nùmero de elementos que 
    # quiero seleccionar, esto tomando en cuenta las reglas de combinación
    # entre conectores

    # El voltaje de inicio y el voltaje de equipo final
    start = OUTLET_JOLT
    finish = max(lista)

    def check_list(lista):
        # Toma una lista y revisa si cumple con las reglas establecidas
        # Si es así retorna True.
        if finish not in lista:
            return False

        dif_list = []
        for j in range(1, len(lista) + 1):
           dif = lista[j] - lista[j - 1]
           if dif > 3:
               return False
        
        return True

    selection_list = lista.copy()
    #selection_list.append(0)
    selection_list.sort()
    ans_list = selection_list[:n]

    print("la primera lista es \n")
    print(ans_list)

    position_index = list(range(n))[::-1]

    for x in position_index:
        # Primer loop el cual se mueve por la posiciòn de la lista de respuesta
        # en orden inverso
        print(x)
        start_index = x
        while start_index < n:
            # Se avanza desde la posición inicial hasta el final de la lista
            # cambiando los valores en la medida que cumple con lass reglas
            copy_ans = ans_list.copy()
            for y in range(len(selection_list)):
                # Se revisa si la lista actual cumple con el requisito
                if check_list(copy_ans):
                    print('se cumplen las reglas totales, se devuelve una lista correcta')
                    yield copy_ans

                # Se revisa cada elemento de la lista original y se evalúa
                # el agregarlo a lista de solución
                option = selection_list[y]
                opt_dif = option - copy_ans[start_index - 1]

                # Se ve si ya se encuentra en lo que llevamos de lista al momento
                if option in copy_ans[:start_index]:
                    #print('ya se encuentra en la lista')
                    continue
                # Se ve si la opción es menor a valor que se busca reemplazar
                elif option < copy_ans[start_index]:
                    #print('{} es menor que el valor actual, {}'.format(option, copy_ans[start_index]))
                    continue
                # Se ve si la dif entre la opción y el valor anterior es mayor a 3
                elif opt_dif > 3:
                    start_index += 1
                    #print(' se encuentra el valor mayor por lo que se avanza de indice')
                    break
                else:
                    print('se cumplen las reglas, se cambia de valor')
                    copy_ans[start_index] = option
                    print(copy_ans)

            
    
def combinarion_gen_final(lista, n):
    # Toma una lista de adaptadores y devuelve un generador 
    # que entrega todas las lista posbiles que contengan n 
    # elementos
    
    # Valores de inicio y finales de voltaje
    start = OUTLET_JOLT
    finish = max(lista)

    def check_list(lista):
        # Función que comprueba si la lista cumple con las reglas ser una
        # conexión valida

        # El valor màs alto debe estar en la lista
        if finish not in lista:
            return False
        
        # El valor inicial debe ser 1, 2 o 3
        if lista[0] not in range(1, 4):
            return False

        # Las diferencias entre valores consecutivos deben ser menores a 4
        for i in range(1, len(lista) + 1):
            dif = lista[i] - lista[i - 1]
            if dif > 3:
                return False

        return True

    # Se genera una copia de la lista y se ordena de menor a menor
    selection_list = lista.copy()
    selection_list.sort()

    def list_generator(lista, index):
        # Toma una lista y la va modificando a partir del indice indicado
        # reemplazando sus valores por los de la lista principal (selection_list)
        
        # Se consigue la cantidad de elementos de la lista inicial
        len_list = len(lista)

        # Se avanza en los indices de la lista modificando sus valores para 
        # cumplir con las reglas
        while index < len_list:

            # Se ven los valores de la lista original (las opciones de reemplazo)
            # y si cumplen con unas reglas básicas se reemplazan
            for option in selection_list:
                # Diferencia hipotetica de terminos consecutivos
                opt_dif = option - lista[index - 1]

                # Si la opción se encuentra en la lista se continua al siguiente
                if option in lista[:index]:
                    continue
                # Si la opción es menor al termino por reemplazar se continúa
                elif option < lista[index]:
                    continue
                # Si la diferencia hipotetica es mayor a 3 se continua
                elif opt_dif > 3:
                    index += 1
                    break
                # Si se pasan las pruebas anterirores se cambia el termino y se 
                # llama a list_generator con la lista modificada y el termino
                # siguiente
                else:
                    lista[index] = option
                    yield list_generator(lista, index + 1)

        # Una vez que se avanzo por todos los indices la única opción es devolver
        # la lista resultante
        yield lista

    #Comenzamos a crear las posibles listas a partir de la lista menor
    ans_list = selection_list[:n]
    
    # Se crea una lista de indices en orden inverso para avanzar por la lista
    # a modificar
    position_index = list(range(n))[::-1]

    # Se itera por la lista mediante la lista de orden inverso
    # Se llama a list_generator y se obtienen las opciones con la función
    # nexto sobre el generador. Estas listas se evaluan para ver si cumplen
    # con todas la reglas, en caso de ser cierto se devuelve la lista
    for x in position_index:
        options_gen = list_generator(ans_list, x)
        option_list = next(options_gen)

        if check_list(option_list):
            yield option_list








































            
def main():
    adapters = adapter_list(open('additional/input_d10', 'r'))
    diferences = jolt_difference(adapters)

    print(diferences)
    print('La respuesta es {}'.format(diferences[1] * diferences[3]))


if __name__ == "__main__":
    main()
