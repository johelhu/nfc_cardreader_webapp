#!/usr/bin/env python

# Importación de bibliotecas y modulos
# Estas líneas importan varias bibliotecas y módulos necesarios para interactuar con lectores de tarjetas inteligentes y gestionar la
# comunicación con tarjetas NFC.

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

# La función main es la función principal del programa
# Se establece el contexto del sistema de tarjetas inteligentes y se obtiene la lista de lectores disponibles
# Si no se encuentra se muestra un mensaje de conectar el lector 

def main():
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
            except:
                oldATR = 0
                continue

            # Compara el UID de la tarjeta actual con la UID anterior para saber si ha habido algun cambio

            if l_atr == oldATR:
                continue

            oldATR = l_atr

            if len(l_atr):
                pass
            else:
                continue

            print(f"{dt.now()}")               # Muesta la fecha y hora actual 
            print(reader, 'El UID es:', l_atr) # Muesta la UID de la tarjeta de salida
            sleep(0.5)

        except ValueError as e: # Manejo de exepciones
            print(e)
            exit(1)

if __name__ == '__main__':
    main()


