from validaciones import *
from listas import *

def agregar_lista(lista):
    nombre = input("Ingrese el nombre del heroe: ")
    identidad = input("Ingrese la identidad del heroe: ")
    empresa = validar_str_lista(input("Ingrese la empresa del heroe"
    " (“DC Comics” o “Marvel Comics”): "), empresas_validas)
    altura = validar_minimo(pedir_int("Ingrese la altura del heroe: "), 0)
    peso = validar_minimo(pedir_int("Ingrese el peso del heroe: "), 0)
    genero = validar_str_lista(input("Ingrese el genero del heroe (M, F, NB): "), generos_validos)
    color_ojos = validar_str_exacto(input("Ingrese el color de ojos del heroe: "), "")
    color_pelo = validar_str_exacto(input("Ingrese el color de pelo del heroe: "), "")
    fuerza = validar_minimo(pedir_int("Ingrese la fuerza: "), 0)
    inteligencia = validar_str_lista(input("Ingrese la inteligencia del heroe "
    "(“low”, “average”, “good”, “high”, “genius”): "), inteligencia_valida)

    lista.append([nombre, identidad, empresa, altura, peso, genero, color_ojos, color_pelo, fuerza, inteligencia])

def eliminar_lista(lista):
    borrar = input("Ingrese el nombre del heroe a borrar: ")
    for i in range(len(lista)):
        if (lista[i][0]) == borrar:
            lista.pop(i)
            break

def ordenar_lista(lista):
    for i in range (len(lista)):
        for i in range (len(lista)-1):
            if lista[i][0] > lista[i+1][0]:
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
    return lista    

def ver_maximo(lista:str, indice:int):
    valor_max = 0
    maximo = ""
    for i in range(len(lista)):
        if float((lista[i][indice])) > valor_max:
            valor_max = float((lista[i][indice]))
            maximo = lista[i]
    mostrar_heroe(maximo)


def ver_minimo(lista:str, indice:int):
    valor_min = 0
    minimo = ""
    flag = True
    for i in range(len(lista)):
        if flag == True:
            valor_min = float((lista[i][indice]))
            minimo = lista[i]
            flag = False
        elif float((lista[i][indice])) < valor_min:
            valor_min = float((lista[i][indice]))
            minimo = lista[i]
        
    mostrar_heroe(minimo)



def mostrar_heroe(lista):
        print(f"""              
-Nombre: {lista[0]}
-Identidad: {lista[1]}
-Empresa: {lista[2]}
-Altura: {lista[3]}
-Peso: {lista[4]}
-Genero: {lista[5]}
-Color de ojos: {lista[6]}
-Colo de pelo: {lista[7]}
-Fuerza: {lista[8]}
-Inteligencia: {lista[9]}

-----------------------------------------
        """)

def mostrar_lista(lista):
    for i in range(len(lista)):
        mostrar_heroe(lista[i])
