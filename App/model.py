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
                    "data": None,
                    "sector": None,
                    "subsector": None}
    
    data_structs["años"] = {}
    data_structs["sector"] = {}
    data_structs["subsector"] = {}
    return data_structs

# Funciones para agregar informacion al modelo

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TO DO: Crear la función para agregar elementos a una lista
    
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
        
    if data["Código sector económico"] in data_structs["sector"]:
        lista_sectores = data_structs["sector"][data["Código sector económico"]]
        lt.addLast(lista_sectores,d)
        
    else:
        lista_sectores = lt.newList(datastructure="ARRAY_LIST")
        lt.addLast(lista_sectores,d)
        data_structs["sector"][data["Código sector económico"]] = lista_sectores
    
    if data["Código subsector económico"] in data_structs["subsector"]:
        lista_subsectores = data_structs["subsector"][data["Código subsector económico"]]
        lt.addLast(lista_subsectores,d)
        
    else:
        lista_subsectores = lt.newList(datastructure="ARRAY_LIST")
        lt.addLast(lista_subsectores,d)
        data_structs["subsector"][data["Código subsector económico"]] = lista_subsectores

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
    #TO DO: Crear la función para obtener el tamaño de una lista
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
    # TO DO: Realizar el requerimiento 2
    pass


def req_3(data_structs,año):
    """
    Función que soluciona el requerimiento 3
    """
    # TO DO: Realizar el requerimiento 3
    lista_año  = data_structs["años"][año]
    map_sort_subsector = sort_list_year_subsector(lista_año)
    subsectores = mp.keySet(map_sort_subsector)
    map_subsectores_y_totales = mp.newMap(numelements=(lt.size(subsectores)))
    
    for subsec in lt.iterator(subsectores):
        pair_key_value = mp.get(map_sort_subsector,subsec)
        value = me.getValue(pair_key_value)
        total = sumar_elementos(value,"Total retenciones")
        mp.put(map_subsectores_y_totales,subsec,total)
    
    numero_subsec_menor_retenciones,valor = find_menor_o_mayor_mapa(map_subsectores_y_totales,"menor")
    pair_key_val_subsec_menor_ret = mp.get(map_sort_subsector,numero_subsec_menor_retenciones)
    lista_act_sub_sec_menor_ret = me.getValue(pair_key_val_subsec_menor_ret)
    merg.sort(lista_act_sub_sec_menor_ret,sort_crit_total_retenciones)
    
    info_totales_subsect = obtener_totales_subsector(lista_act_sub_sec_menor_ret)
    info_totales_subsect["Total retenciones del subsector económico"] = valor
    
    if lt.size(lista_act_sub_sec_menor_ret) > 6:
        act_aportes = get_3_last_and_first_list(lista_act_sub_sec_menor_ret)
    
    else:
        act_aportes = lista_act_sub_sec_menor_ret
    return info_totales_subsect,act_aportes
    
    
def req_4(data_structs,año):
    """
    Función que soluciona el requerimiento 4
    """
    # TO DO: Realizar el requerimiento 4
    lista_año = data_structs["años"][año]
    map_sort_subsector = sort_list_year_subsector(lista_año)
    subsectores = mp.keySet(map_sort_subsector)
    map_subsectores_y_totales = mp.newMap(numelements=(lt.size(subsectores)))
    
    for subsec in lt.iterator(subsectores):
        pair_key_value = mp.get(map_sort_subsector,subsec)
        value = me.getValue(pair_key_value)
        total = sumar_elementos(value,"Costos y gastos nómina")
        mp.put(map_subsectores_y_totales,subsec,total)
    
    numero_subsec_menor_retenciones,valor = find_menor_o_mayor_mapa(map_subsectores_y_totales,"mayor")
    pair_key_val_subsec_mayor_nom = mp.get(map_sort_subsector,numero_subsec_menor_retenciones)
    lista_act_sub_sec_mayor_nom = me.getValue(pair_key_val_subsec_mayor_nom)
    merg.sort(lista_act_sub_sec_mayor_nom,sort_crit_total_costos_nomina)
    
    info_totales_subsect = obtener_totales_subsector(lista_act_sub_sec_mayor_nom)
    info_totales_subsect["Total costos y gastos de nómina del subsector económico"] = valor
    info_totales_subsect.pop("Total retenciones del subsector económico",None)
    
    if lt.size(lista_act_sub_sec_mayor_nom) > 6:
        act_aportes = get_3_last_and_first_list(lista_act_sub_sec_mayor_nom)
    else:
        act_aportes = lista_act_sub_sec_mayor_nom
    return info_totales_subsect,act_aportes


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs,ano):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    data = lt.newList(datastructure='ARRAY_LIST')
    for sector in data_structs['años'][ano]['elements']:
        lt.addLast(data,{})
        elementos = ['Código sector económico','Nombre sector económico','Total ingresos netos','Total costos y gastos',
                         'Total saldo a pagar','Total saldo a favor']
        puesto = lt.size(data) - 1
        for elemento in range(len(elementos)):
            if elemento > 1 and elemento < 6:
                data['elements'][puesto][elementos[elemento] + " del sector económico"] = sector[elementos[elemento]]
            else:
                data['elements'][puesto][elementos[elemento]] = sector[elementos[elemento]]
    merg.sort(data,sort_total_ingresos)
    ma_ingresos = lt.subList(data,1,1)
    subsectores = lt.newList(datastructure='ARRAY_LIST')
    for sub in range(lt.size(data_structs["sector"][ma_ingresos['elements'][0]['Código sector económico']])):
        if data_structs["sector"][ma_ingresos['elements'][0]['Código sector económico']]['elements'][sub]['Año'] == ano:
            lt.addLast(subsectores,{})
            elements = ['Código subsector económico','Nombre subsector económico','Total ingresos netos','Total costos y gastos',
                         'Total saldo a pagar','Total saldo a favor']
            puesto = lt.size(subsectores) - 1
            for element in range(len(elements)):
                if element > 1 and element < 6:
                    subsectores['elements'][puesto][elements[element] + " del subsector económico"] = data_structs["sector"][ma_ingresos['elements'][0]['Código sector económico']]['elements'][sub][elements[element]]
                else:
                    subsectores['elements'][puesto][elements[element]] = data_structs["sector"][ma_ingresos['elements'][0]['Código sector económico']]['elements'][sub][elements[element]]
    if lt.size(subsectores) > 1:
        merg.sort(subsectores,sort_total_ingresos_sub)
    ma_ingresos['elements'][0]['Subsector económico que más aportó'] = lt.firstElement(subsectores)['Código subsector económico']
    ma_ingresos['elements'][0]['Subsector económico que menos aportó'] = lt.lastElement(subsectores)['Código subsector económico']
    lista_sub_mas = [lt.firstElement(subsectores)]
    lista_sub_menos = [lt.lastElement(subsectores)]
    mas_aporto = lt.newList(datastructure='ARRAY_LIST')
    for activity in range(lt.size(data_structs["subsector"][ma_ingresos['elements'][0]['Subsector económico que más aportó']])):
        if data_structs["subsector"][ma_ingresos['elements'][0]['Subsector económico que más aportó']]['elements'][activity]['Año'] == ano:
            lt.addLast(mas_aporto,{})
            elemens = ['Código actividad económica','Nombre actividad económica','Total ingresos netos','Total costos y gastos',
                         'Total saldo a pagar','Total saldo a favor']
            puesto = lt.size(mas_aporto) - 1
            for elemen in range(len(elemens)):
                mas_aporto['elements'][puesto][elemens[elemen]] = data_structs["subsector"][ma_ingresos['elements'][0]['Subsector económico que más aportó']]['elements'][activity][elemens[elemen]]
    merg.sort(mas_aporto,sort_total_ingresos_act)
    elems = ['Código actividad económica','Nombre actividad económica','Total ingresos netos','Total costos y gastos',
                         'Total saldo a pagar','Total saldo a favor']
    lista_sub_mas[0]['Actividad económica que más aportó'] = []
    for elem in elems:
        lista_sub_mas[0]['Actividad económica que más aportó'].append([elem,mas_aporto['elements'][0][elem]])
    lista_sub_mas[0]['Actividad económica que menos aportó'] = []
    for elem in elems:
        lista_sub_mas[0]['Actividad económica que menos aportó'].append([elem,mas_aporto['elements'][lt.size(mas_aporto)-1][elem]])
    menos_aporto = lt.newList(datastructure='ARRAY_LIST')
    for activity in range(lt.size(data_structs["subsector"][ma_ingresos['elements'][0]['Subsector económico que menos aportó']])):
        if data_structs["subsector"][ma_ingresos['elements'][0]['Subsector económico que menos aportó']]['elements'][activity]['Año'] == ano:
            lt.addLast(menos_aporto,{})
            elemens = ['Código actividad económica','Nombre actividad económica','Total ingresos netos','Total costos y gastos',
                         'Total saldo a pagar','Total saldo a favor']
            puesto = lt.size(menos_aporto) - 1
            for elemen in range(len(elemens)):
                menos_aporto['elements'][puesto][elemens[elemen]] = data_structs["subsector"][ma_ingresos['elements'][0]['Subsector económico que menos aportó']]['elements'][activity][elemens[elemen]]
    merg.sort(menos_aporto,sort_total_ingresos_act)
    lista_sub_menos[0]['Actividad económica que más aportó'] = []
    for elem in elems:
        lista_sub_menos[0]['Actividad económica que más aportó'].append([elem,menos_aporto['elements'][0][elem]])
    lista_sub_menos[0]['Actividad económica que menos aportó'] = []
    for elem in elems:
        lista_sub_menos[0]['Actividad económica que menos aportó'].append([elem,menos_aporto['elements'][lt.size(menos_aporto)-1][elem]])
    return ma_ingresos,lista_sub_mas,lista_sub_menos


def req_7(data_structs,top,ano,codigo):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    data = lt.newList(datastructure='ARRAY_LIST')
    total = {'Total ingresos netos':0,'Total costos y gastos':0,'Total saldo a pagar':0,'Total saldo a favor':0}
    for actividad in data_structs['años'][ano]['elements']:
        if actividad['Código subsector económico'] == codigo:
            elementos = ['Código actividad económica','Nombre actividad económica','Código sector económico','Nombre sector económico',
                         'Total ingresos netos','Total costos y gastos','Total saldo a pagar','Total saldo a favor']
            total['Total ingresos netos'] += int(actividad['Total ingresos netos'])
            total['Total costos y gastos'] += int(actividad['Total costos y gastos'])
            total['Total saldo a pagar'] += int(actividad['Total saldo a pagar'])
            total['Total saldo a favor'] += int(actividad['Total saldo a favor'])
            lt.addLast(data,{})
            puesto = lt.size(data) - 1
            for elemento in range(len(elementos)):
                if elemento > 3:
                    data['elements'][puesto][elementos[elemento] + " consolidados para el periodo"] = actividad[elementos[elemento]]
                else:
                    data['elements'][puesto][elementos[elemento]] = actividad[elementos[elemento]]
    merg.sort(data, sort_total_costos_gastos)
    if lt.size(data) > top:
        for place in range(top):
            for elemento in range(4,len(elementos)):
                data['elements'][place][elementos[elemento] + " consolidados para el periodo"] = total[elementos[elemento]]
        return lt.subList(data,1,top),top
    else:
        for place in range(lt.size(data)):
            for elemento in range(4,len(elementos)):
                data['elements'][place][elementos[elemento] + " consolidados para el periodo"] = total[elementos[elemento]]
        return data,lt.size(data)


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


def sort_crit_total_retenciones(data_1,data_2):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TO DO: Crear función de ordenamiento
    ddata_1 = data_1["Total retenciones"]
    ddata_2 = data_2["Total retenciones"]

    int_data_1 = int(ddata_1)
    int_data_2 = int(ddata_2)
    
    if int_data_1 < int_data_2:
        return True
    else:
        return False
    
def sort_crit_total_costos_nomina(data_1,data_2):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TO DO: Crear función de ordenamiento
    ddata_1 = data_1["Costos y gastos nómina"]
    ddata_2 = data_2["Costos y gastos nómina"]

    int_data_1 = int(ddata_1)
    int_data_2 = int(ddata_2)
    
    if int_data_1 < int_data_2:
        return True
    else:
        return False
    
    
def comparar(data_1, data_2, id):
    return int(data_1[id]) < int(data_2[id])


def sort_total_costos_gastos(data_1, data_2):
    return comparar(data_1, data_2, 'Total costos y gastos consolidados para el periodo')


def mayor(data_1, data_2, id):
    return int(data_1[id]) > int(data_2[id])


def sort_total_ingresos(data_1, data_2):
    return mayor(data_1, data_2, 'Total ingresos netos del sector económico')


def sort_total_ingresos_sub(data_1, data_2):
    return mayor(data_1, data_2, 'Total ingresos netos del subsector económico')


def sort_total_ingresos_act(data_1, data_2):
    return mayor(data_1, data_2, 'Total ingresos netos')
        
        
def comparar_año(año1,año2):
    if año1 < año2:
        return True
    else:
        return False
    
def sort_list_year_subsector(lista_año):
    map_subsectores = mp.newMap(numelements=(lt.size(lista_año)))
    
    for actividad in lt.iterator(lista_año):
        subsector = actividad["Código subsector económico"]
        
        if mp.contains(map_subsectores,subsector):
            pair_key_value = mp.get(map_subsectores,subsector)
            lista_sebsec = me.getValue(pair_key_value)
            lt.addLast(lista_sebsec,actividad)
            
        else:
            lista_subsectores = lt.newList(datastructure="ARRAY_LIST")
            lt.addLast(lista_subsectores,actividad)
            mp.put(map_subsectores,subsector,lista_subsectores)
            
        
    return map_subsectores

def sumar_elementos(lista_actividades,criterio):
    total = 0
    for impuesto in lt.iterator(lista_actividades):
        valor_a_sumar = impuesto[criterio]
        valor = int(valor_a_sumar)
        total += valor
    return total

def find_menor_o_mayor_mapa(mapa,criterio):
    llaves = mp.keySet(mapa)
    mayor = 0
    menor = 1000000000000
    for subsector in lt.iterator(llaves):
        pair_key_value = mp.get(mapa,subsector)
        valor = me.getValue(pair_key_value)
        
        if criterio == "menor":
            if valor < menor:
                menor = valor
                llave_rta = me.getKey(pair_key_value)
                valor_tot = me.getValue(pair_key_value)
                
        if criterio == "mayor":
            if valor > mayor:
                mayor = valor
                llave_rta = me.getKey(pair_key_value)
                valor_tot = me.getValue(pair_key_value)
                
    return llave_rta,valor_tot

def obtener_totales_subsector(lista_subsector):
    info = {"Código sector económico": None,
            "Nombre sector económico": None,
            "Código subsector económico":None,
            "Nombre subsector económico": None,
            "Total retenciones del subsector económico": None,
            "Total ingresos netos del subsector económico":0,
            "Total costos y gastos del subsector económico":0,
            "Total saldo a pagar del subsector económico": 0,
            "Total saldo a favor del subsector económico":0}
     
    for actividad in lt.iterator(lista_subsector):
        ingresos_netos = actividad["Total ingresos netos"]
        costos_gastos = actividad["Total costos y gastos"]
        saldo_pagar = actividad["Total saldo a pagar"]
        saldo_favor = actividad["Total saldo a favor"]
        
        int_ingresos_netos = int(ingresos_netos)
        int_costos_gastos = int(costos_gastos)
        int_saldo_pagar = int(saldo_pagar)
        int_saldo_favor = int(saldo_favor)
        
        info["Total ingresos netos del subsector económico"] += int_ingresos_netos
        info["Total costos y gastos del subsector económico"] += int_costos_gastos
        info["Total saldo a pagar del subsector económico"] += int_saldo_pagar
        info["Total saldo a favor del subsector económico"] += int_saldo_favor
    
    info["Código sector económico"] = actividad["Código sector económico"]
    info["Nombre sector económico"] = actividad["Nombre sector económico"]
    info["Código subsector económico"] = actividad["Código subsector económico"]
    info["Nombre subsector económico"] = actividad["Nombre subsector económico"]
        
    return info

    
def sort_año(data_structs):
    data_structs_ordenada =  dict(sorted(data_structs["años"].items(), key=lambda t: t[0]))
    data_structs["años"] = data_structs_ordenada
    
            
            
