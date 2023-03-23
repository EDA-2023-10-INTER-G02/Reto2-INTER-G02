﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf
from tabulate import tabulate as tab
import traceback

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller():
    """
        Se crea una instancia del controlador
    """
    #TO DO: Llamar la función del controlador donde se crean las estructuras de datos
    control = controller.new_controller()
    return control


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    #print("3- Ejecutar Requerimiento 2")
    print("3- Ejecutar Requerimiento 3")
    print("4- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("0- Salir")


def load_data(control):
    """
    Carga los datos
    """
    #TO DO: Realizar la carga de datos
    data = controller.load_data(control)
    return data
    
def print_tabla_load_data(control):
    for año in control["años"]:
        lista = control["años"][año]
        data = controller.get_3_last_and_first(lista)
        lista_de_listas = []
        
        for actividad in lt.iterator(data):
            titulos = list(actividad.keys())
            headerss = titulos[0:11]
            lista_actividad = list(actividad.values())
            valores = lista_actividad[0:11]
            lista_de_listas.append(valores)
            
        print("\nTres primeras y últimas actividades económicas del " + str(año))
        print(tab(lista_de_listas,tablefmt='grid',headers=headerss,
                colalign=['right','right','left','right','left','right','left','left','left','left',"left"], 
                maxcolwidths=[7,7,15,7,20,8,20,10,10,10,10], maxheadercolwidths=[7,7,15,7,20,8,20,10,10,10,10]))
        
def print_tabla_req1(impuesto,año,cod_sector_ec):
    lista_de_listas = []
    titulos = list(impuesto.keys())
    headerss = ["Código actividad económica","Nombre actividad económica"]
    lista_actividad = list(impuesto.values())
    valores = lista_actividad[1:3]
    
    for i in range(5,11):
        titulo = titulos[i]
        headerss.append(titulo)
        valor = lista_actividad[i]
        valores.append(valor)

    lista_de_listas.append(valores)
    print("\nActividad económica con el mayor saldo total de impuestos a pagar para el sector "+cod_sector_ec+" en el año " +año)
    
    print(tab(lista_de_listas,tablefmt='grid',headers=headerss,maxcolwidths=[12,22,15,22,15,12,12,12],
              maxheadercolwidths=[12,22,15,22,15,12,12,12]))
    
def print_tabla_req3_y_4(info,año):
    lista_de_listas = []
    headerss = list(info.keys())
    valor = list(info.values())
    lista_de_listas.append(valor)
    
    print(tab(lista_de_listas,tablefmt='grid',headers=headerss,maxcolwidths=[12,22,15,22,15,12,12,12,12],
              maxheadercolwidths=[12,22,15,22,15,12,12,12,12]))
    
def print_tabla_3y4b(act_aportes,criterio):
    lista_de_listas = []
    headerss = ["Código actividad económica","Nombre actividad económica", criterio,"Total ingresos netos","Total costos y gastos",
                "Total saldo a pagar", "Total saldo a favor"]
    
    for act in lt.iterator(act_aportes):
        valores = []
        valores.append(act["Código actividad económica"])
        valores.append(act["Nombre actividad económica"])
        valores.append(act[criterio])
        valores.append(act["Total ingresos netos"])
        valores.append(act["Total costos y gastos"])
        valores.append(act["Total saldo a pagar"])
        valores.append(act["Total saldo a favor"])
        lista_de_listas.append(valores)
    
    print(tab(lista_de_listas,tablefmt='grid',headers=headerss,maxcolwidths=[12,25,15,22,15,15,15],
              maxheadercolwidths=[12,25,15,22,15,15,15]))
    
def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento0
    pass

def print_req_1(control,año,cod_sector_ec):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TO DO: Imprimir el resultado del requerimiento 1
    impuesto,tiempo = controller.req_1(control,año,cod_sector_ec)
    print_tabla_req1(impuesto,año,cod_sector_ec)
    print("Memoria: " +str(tiempo)+" [kB]")


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TO DO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control,año):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TO DO: Imprimir el resultado del requerimiento 3
    info,act_aportes = controller.req_3(control,año)
    print("\nSubsector económico con el menor total de retenciones en el año " +str(año))
    print_tabla_req3_y_4(info,año)
    print("\nActividades económicas con menores y mayores aportes al valor total de retenciones del subsector")
    print_tabla_3y4b(act_aportes,"Total retenciones")


def print_req_4(control,año):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TO DO: Imprimir el resultado del requerimiento 4
    info,act_aportes = controller.req_4(control,año)
    print("\nSubsector económico con el mayor total de costos y gastos nómina en el año " +str(año))
    print_tabla_req3_y_4(info,año)
    print("\nActividades económicas con menores y mayores aportes al valor total de costos y gastos nómina del subsector")
    print_tabla_3y4b(act_aportes,"Costos y gastos nómina")


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea el controlador asociado a la vista
control = new_controller()

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        try:
            if int(inputs) == 1:
                print("Cargando información de los archivos ....\n")
                filas = controller.load_data(control)
                print("Se cargaron " + str(filas) + " filas")
                print_tabla_load_data(control)
                
            elif int(inputs) == 2:
                año = input("Elija un año: ")
                cod_sector_ec = input("Elija un sector económico: ")
                print_req_1(control, año,cod_sector_ec)

            elif int(inputs) == 3:
                año = input("Elija un año: ")
                print_req_3(control,año)

            elif int(inputs) == 4:
                año = input("Elija un año: ")
                print_req_4(control,año)

            elif int(inputs) == 5:
                print_req_4(control)

            elif int(inputs) == 6:
                print_req_5(control)

            elif int(inputs) == 7:
                print_req_6(control)

            elif int(inputs) == 8:
                print_req_7(control)

            elif int(inputs) == 9:
                print_req_8(control)

            elif int(inputs) == 0:
                working = False
                print("\nGracias por utilizar el programa")
                
            else:
                print("Opción errónea, vuelva a elegir.\n")
        except Exception as exp:
            print("ERR:", exp)
            traceback.print_exc()
    sys.exit(0)
