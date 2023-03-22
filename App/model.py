"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TO DO: Inicializar las estructuras de datos
    data_structs = {"años": None,
                    "data": None}
    
    data_structs["años"] = {}
    return data_structs

# Funciones para agregar informacion al modelo

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    
    d = new_data(data["Año"], data["Código actividad económica"], data["Nombre actividad económica"],
                 data["Código sector económico"], data["Nombre sector económico"], data["Código subsector económico"],
                 data["Nombre subsector económico"], data["Total ingresos netos"], data["Total costos y gastos"],
                 data["Total saldo a pagar"], data["Total saldo a favor"], data["Total retenciones"],data["Costos y gastos nómina"])
    
    if data["Año"] in data_structs["años"]:
        lista_año = data_structs["años"][data["Año"]]
        lt.addLast(lista_año,d)
        
    else:
        lista_años = lt.newList(datastructure="ARRAY_LIST")
        lt.addLast(lista_años,d)
        data_structs["años"][data["Año"]] = lista_años


# Funciones para creacion de datos

def new_data(año, codigo, nom_act_ec, codigo_sec_ec,nombre_sec_ec, codigo_subsector,nombre_sebsector,
             total_ingr_netos, total_costos_gastos,saldo_a_pagar, saldo_favor,total_retenciones,costos_gastos_nomina):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TO DO: Crear la función para estructurar los datos
    data = {}
    data["Año"] = año
    data["Código actividad económica"] = codigo
    data["Nombre actividad económica"] = nom_act_ec
    data["Código sector económico"] = codigo_sec_ec
    data["Nombre sector económico"] = nombre_sec_ec
    data["Código subsector económico"]= codigo_subsector
    data["Nombre subsector económico"] = nombre_sebsector
    data["Total ingresos netos"] = total_ingr_netos
    data["Total costos y gastos"] = total_costos_gastos
    data["Total saldo a pagar"] = saldo_a_pagar
    data["Total saldo a favor"] = saldo_favor
    data["Total retenciones"] = total_retenciones
    data["Costos y gastos nómina"] = costos_gastos_nomina

    return data


# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def data_size(lista):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    size = lt.size(lista)
    return size

def req_1(data_structs,año,cod_sector_ec):
    """
    Función que soluciona el requerimiento 1
    """
    # TO DO: Realizar el requerimiento 1
    lista_año = data_structs["años"][año]
    list_esp_cod = lt.newList(datastructure="ARRAY_LIST")
    
    for actividad in lt.iterator(lista_año):
        if actividad["Código sector económico"] == cod_sector_ec:
            lt.addLast(list_esp_cod,actividad)
            
    mayor = 0
    for impuesto in lt.iterator(list_esp_cod):
        saldo_pagar = impuesto["Total saldo a pagar"]
        saldo_pagar_int = int(saldo_pagar)
        
        if saldo_pagar_int > mayor:
            mayor = saldo_pagar_int
            rta = impuesto      
    return rta


def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass

def get_3_last_and_first_list(lista):
    size = data_size(lista)
    first_3 = lt.subList(lista,1,3)
    last_3 = lt.subList(lista,(size-2),3)
    
    for elem in lt.iterator(last_3):
        lt.addLast(first_3,elem)
        
    return first_3

# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2, id):
    """
    Función encargada de comparar dos datos
    """
    #TO DO: Crear función comparadora de la lista
    if data_1[id] < data_2[id]:
        return True
    elif data_1[id] > data_2[id]:
        return False
    else:
        return "equal"

# Funciones de ordenamiento

def sort_criteria_actividad_ec(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TO DO: Crear función comparadora para ordenar
    year = compare(data_1, data_2, "Año")
    if year == "equal":
        return compare(data_1, data_2, "Código actividad económica")
    else:
        return year


def sort_codigo_act_ec(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TO DO: Crear función de ordenamiento
    for año in data_structs["años"]:
        lista_año = data_structs["años"][año]
        merg.sort(lista_año,sort_criteria_actividad_ec)
        
def sort_crit_total_saldo_pagar(data_1,data_2):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TO DO: Crear función de ordenamiento
    saldo = compare(data_1, data_2, "Total saldo a pagar")
    if saldo == "equal":
        return compare(data_1, data_2, "Código actividad económica")
    else:
        return saldo
        
        
def comparar_año(año1,año2):
    if año1 < año2:
        return True
    else:
        return False
    
def sort_año(data_structs):
    data_structs_ordenada =  dict(sorted(data_structs["años"].items(), key=lambda t: t[0]))
    data_structs["años"] = data_structs_ordenada
    
            
            
