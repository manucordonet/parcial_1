from validaciones import *
from funciones_lista import *

def menu ():
    lista_heroes = []
    menu = True
    while menu == True:
        print("""
    --------------- MENU ---------------
        
    1) Importar la lista de heroes
    2) Listar todos los heroes registrados
    3) Agregar un heroe a la lista
    4) Eliminar un heroe de la lista
    5) Ordenar la lista por nombre
    6) Ver el heroe mas alto
    7) Ver el heroe mas fuerte
    8) Ver el heroe mas delgado      
    9) Salir   
        
    ------------------------------------
    """)
        
        eleccion = pedir_int("Elija la opcion deseada: ")

        match validar_rango(eleccion, 1, 9):
            case 1:
                from listas import lista_heroes 
                print("Lista importada correctamente")
            case 2:
                mostrar_lista(lista_heroes)
            case 3:
                agregar_lista(lista_heroes)
            case 4:
                eliminar_lista(lista_heroes, "Ingrese el nombre del heroe a eliminar: ",
                                "El heroe ingresado no esta registrado", 0)
            case 5:
                ordenar_lista(lista_heroes)
                mostrar_lista(lista_heroes)
            case 6:
                ver_maximo(lista_heroes, 3)
            case 7:
                ver_maximo(lista_heroes, 8)
            case 8:
                ver_minimo(lista_heroes, 4)
            case 9:
                print("Sesion finalizada")
                menu = False
