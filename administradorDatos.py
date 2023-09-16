#!/usr/bin/env python 

from os import system as bash 
import pandas as pd 

def inicializar_datos():
    try:
        df = pd.read_excel("data.xlsx", converters={'card_uid': str}) 
        print('Se encontró el archivo de datos')
    except FileNotFoundError: 
        print('No se encontró el archivo de datos')
        exit(1)
    return df
