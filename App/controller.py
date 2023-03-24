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
 """

import config as cf
import model
import time
import csv
import tracemalloc
"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller():
    """
    Crea una instancia del modelo
    """
    #TO DO: Llamar la función del modelo que crea las estructuras de datos
    control = model.new_data_structs()
    return control


# Funciones para la carga de datos

def load_data(control):
    """
    Carga los datos del reto
    """
    # TO DO: Realizar la carga de datos
    filas = 0
    file = cf.data_dir + "DIAN/Salida_agregados_renta_juridicos_AG-small.csv"
    input_file = csv.DictReader(open(file, encoding="utf-8"))
    
    for impuesto in input_file:
        model.add_data(control, impuesto)
        filas += 1
        
    model.sort_codigo_act_ec(control)
    model.sort_año(control)
    return filas
# Funciones de ordenamiento

def sort(control):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    pass

# Funciones de consulta sobre el catálogo
def get_3_last_and_first(lista):
    lista = model.get_3_last_and_first_list(lista)
    return lista
    
def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass


def req_1(control,año,cod_sector_ec):
    """
    Retorna el resultado del requerimiento 1
    """
    # TO DO: Modificar el requerimiento 1
    #inicio_time = get_time()
    tracemalloc.start()
    memoria_i = get_memory()
    data = model.req_1(control,año,cod_sector_ec)
    #final_time = get_time()
    memoria_f = get_memory()
    tracemalloc.stop()
    tiempo = delta_memory(memoria_f,memoria_i)
    
    return data, tiempo


def req_2(control):
    """
    Retorna el resultado del requerimiento 2
    """
    # TO DO: Modificar el requerimiento 2
    pass


def req_3(control,año):
    """
    Retorna el resultado del requerimiento 3
    """
    # TO DO: Modificar el requerimiento 3
    #tracemalloc.start()
    tiempo_i = get_time()
    data = model.req_3(control,año)
    tiempo_f = get_time()
    #tracemalloc.stop()
    tiempo = delta_time(tiempo_i,tiempo_f)
    #print("Tiempo: " +str(tiempo))
    
    return data


def req_4(control,año):
    """
    Retorna el resultado del requerimiento 4
    """
    # TO DO: Modificar el requerimiento 4
    tracemalloc.start()
    #tiempo_i = get_time()
    memoria_i = get_memory()
    data = model.req_4(control,año)
    memoria_f = get_memory()
    #tiempo_f = get_time()
    #tiempo = delta_time(tiempo_i,tiempo_f)
    tracemalloc.stop()
    tiempo = delta_memory(memoria_f,memoria_i)
    print("Memoria: " +str(tiempo))
    return data


def req_5(control):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(control):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(control):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

def get_memory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def delta_memory(stop_memory, start_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory


def size(control):
    tamaño = model.data_size(control)
    return tamaño