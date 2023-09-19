#!/usr/bin/env python 

import pandas as pd # importar libreria pandas, se usa para interactuar con tablas de datos

def inicializar_datos(archivo): # inicia la funcion 
    try: # intenta hacer
        # lee el excel llamado archivo, y convierte el card_uid en un str, todo lo guarda en dataframe(df)
        df = pd.read_excel(archivo, converters={'card_uid': str}) 
        print('Se encontró el archivo de datos')

    except FileNotFoundError: # excepto si 
        # si no se encuentra el data entonces imprima el error y salga del programa
        print('No se encontró el archivo de datos')
        exit(1)

    return df # se retorna el valor y acaba la función en este caso nos guarda que que guardamos en df para usarlo en otro lugar
