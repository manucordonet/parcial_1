def validar_rango(dato:int, minimo:int, maximo:int):  
        validar = dato
        while validar < minimo or validar > maximo:
            validar = pedir_int(f"ERROR, ingrese un valor dentro del rango ({minimo} - {maximo}): ")
        return validar

def validar_minimo(dato:int, minimo:int): 
        validar = dato
        while validar <= minimo:
            validar = pedir_int(f"ERROR, el valor ingresado no puede ser menor a {minimo}): ")
        return validar

def pedir_int(mensaje:str):
    ingreso = input(mensaje)
    while detectar_casteable(ingreso) == False:
        ingreso = input("ERROR, ingrese una opcion valida: ")
    return int(ingreso)
    
def validar_string_lista(lista:list, indice:int, string:str):
        encontrado = False
        for i in range(len(lista)):
            if (lista[i][indice]) == string:
                encontrado = True
                break
        return encontrado

def detectar_casteable(string:str)->bool:
    numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-"]
    casteable = True

    if string == "":
        casteable = False
    else:        
        for i in range(len(string)):
            if string[i] in numeros:
                pass
            else:
                casteable = False
                break
           
    return casteable