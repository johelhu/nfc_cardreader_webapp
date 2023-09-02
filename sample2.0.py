#!/usr/bin/env python

# Importación de bibliotecas y modulos
# Estas líneas importan varias bibliotecas y módulos necesarios para interactuar con lectores de tarjetas inteligentes y gestionar la
# comunicación con tarjetas NFC.

from os import system as bash # Libreria para correr comandos bash dentro del codigo
import pandas as pd # Es una biblioteca para trabajar con tablas de datos # as pd (leer como)

from smartcard.Exceptions import NoCardException           
from smartcard.Exceptions import CardConnectionException
from smartcard.System import readers
from smartcard.util import toHexString
from smartcard.scard import *
import signal  # Importa la biblioteca signal, modulo que permite trabajar con señales del sistema como Ctrl+C para interrumpir

from datetime import datetime as dt
from time import sleep

def sigint_handler(signal, frame): # Define una funcion "sigint_handler" que se ejecutara cuando resiba una señal
    print('Proceso interrumpido')
    exit(0)

# cuando el usuario presione Ctrl+C para interrumpir el programa, en lugar de cerrarse inmediatamente, el programa ejecutará la función
# sigint_handler. Esto permite que el programa realice un cierre controlado en lugar de detenerse abruptamente. 

signal.signal(signal.SIGINT, sigint_handler)

# Aquí, se inicializan dos variables, l_atr y oldATR, que se utilizarán para realizar un seguimiento del UID de la tarjeta NFC y detectar    
# cambios en ella.

l_atr = 1   # Guarda la UID actual de la tarjeta
oldATR = 0  # Guarda la UID antigua de la tarjeta en caso de algun cambio en medio del proceso de lectura

# Leer el UID mediante Codigos APDU:

APDU_command = [0xFF, 0xCA, 0x00, 0x00, 0x00]


def inicializar_datos():
    try:
        df = pd.read_excel("data.xlsx", converters={'card_uid': str}) #Abrir el excel y combierte una columna en str

    except FileNotFoundError: # Error de cuando no hay data.xlsx
        #df = pd.DataFrame(columns=['nombre', 'grupo', 'grado', 'beca', 'ne', 'card_uid'])
        #print(df)
        
        print('No se encontro el archivo de datos')
        exit(1)
        
    return df

# La función main es la función principal del programa
# Se establece el contexto del sistema de tarjetas inteligentes y se obtiene la lista de lectores disponibles
# Si no se encuentra se muestra un mensaje de conectar el lector 

def main():
    bash('clear')
    df = inicializar_datos() 

    try:
        hresult, hcontext = SCardEstablishContext(SCARD_SCOPE_USER)
        hresult, readers = SCardListReaders(hcontext, [])

        if not readers:
            print("Conecte el lector")
            exit(1)

        reader = readers[0]
    except ValueError:
        exit(1)
    
    # Este es el bucle principal del programa, que se ejecuta continuamente hasta una excepción manual
    # En cada iteración, el programa esperara 0.1s y luego seguira la ejecución
        
    print("Ejecutando programa. Por favor, ingrese una tarjeta NFC en el lector...")    
    while True:
        
        sleep(0.1)
        try:
            try:
                
                # Establece una conexion con el lector de tarjetas NFC
                # Envia el comando APDU para leer el UID de la tarjeta
                # Procesa la respuesta obtenida que contiene el UID de la tarjeta
                # Si ocurre una excepción durante este proceso se restablece la variable "oldATR" y se continua con la otra parte del bucle
                
                hresult, hcard, dwActiveProtocol = SCardConnect(
                    hcontext,
                    reader,
                    SCARD_SHARE_SHARED,
                    SCARD_PROTOCOL_T0 | SCARD_PROTOCOL_T1)

                hresult, response = SCardTransmit(
                    hcard, dwActiveProtocol, APDU_command)
                l_atr = str(response).replace(', ', '')
                l_atr = l_atr.replace('[', '')
                l_atr = l_atr.replace(']', '')

            except SystemError: # Error de cuando no hay lectura
                oldATR = 0
                continue

            # Compara el UID de la tarjeta actual con la UID anterior para saber si ha habido algun cambio

            try:
                if l_atr == oldATR:
                    continue
            except UnboundLocalError: # Error cuando se inicia con una tarjeta puesta en el lector
                pass                  # Para que continue

            oldATR = l_atr

            if len(l_atr):
                pass
            else:
                continue

            #print(f"{dt.now()}")               # Muesta la fecha y hora actual 
            #print(reader, 'El UID es:', l_atr) # Muesta la UID de la tarjeta de salida
            
            l_atr = f'ID{l_atr}' # Ingresa un "ID" previo al numero para igualar al formato del exel


            # Se imprime el contenido de las 2 variables para compararlas
            #print(f"El tipo de l_atr es {type(l_atr)}, el tipo de df[card_uid] es {type(df['card_uid'][0])}")
            #print(f"l_atr es {l_atr}, df[card_uid] es {df['card_uid'][0]}")
            
            row = df.loc[df['card_uid'] == l_atr] # Localiza una fila comparando el valor de una columna
            if not row.empty:
            
            # Imprime un texto con formato resaltando la fecha y el nombre, además de acomodar la fecha
            
                print(f" -> Lectura, fecha: \033[1;32m{dt.now().strftime('%d/%m/%Y, %H:%M:%S')}\033[0m, por \033[1;33m{row['nombre'].values[0]}\033[0m, contenido \n{row}\n")
            else:
                print(f' Nueva lectura desconocida, UID: {l_atr}') # Muesta la UID de la tarjeta de salida
    
            sleep(0.5)

        except ValueError as e: # Manejo de exepciones
            print(e)
            exit(1)

if __name__ == '__main__':
    main()


