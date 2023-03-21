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
    
    data_structs["años"] = mp.newMap(numelements=2452,maptype= 'CHAINING', loadfactor= 8)
    #data_structs["data"] = lt.newList(datastructure="ARRAY_LIST")

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
    
    if mp.contains(data_structs["años"],data["Año"]):
        pair_key_val = mp.get(data_structs["años"],data["Año"])
        lista_año = me.getValue(pair_key_val)
        lt.addLast(lista_año,d)
        
    else:
        lista_años = lt.newList(datastructure="ARRAY_LIST")
        lt.addLast(lista_años,d)
        mp.put(data_structs["años"],data["Año"],lista_años)

    #lt.addLast(data_structs["data"],d)
    #merg.sort(data_structs["data"],sort_criteria_actividad_ec)
    sort_codigo_act_ec(data_structs)


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


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TO DO: Crear la función para obtener el tamaño de una lista
    llaves_años = mp.keySet(data_structs["años"])
    size = 0
    
    for año in lt.iterator(llaves_años):
        pair_llave_valor = mp.get(data_structs["años"],año)
        valor = me.getValue(pair_llave_valor)
        tamaño = lt.size(valor)
        size += tamaño
        
    return size

def req_1(data_structs):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    pass


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
    llaves = mp.keySet(data_structs["años"])
    for año in lt.iterator(llaves):
        llave_valor = mp.get(data_structs["años"],año)
        lista_año = me.getValue(llave_valor)
        merg.sort(lista_año,sort_criteria_actividad_ec)
        
def comparar_año(año1,año2):
    if año1 < año2:
        return True
    else:
        return False
            
            
