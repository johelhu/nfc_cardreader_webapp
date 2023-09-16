#!/usr/bin/env python #Le dice al sistema como debe interpretar y ejecutar el archivo

from os import system as bash 
from smartcard.Exceptions import NoCardException           
from smartcard.Exceptions import CardConnectionException
from smartcard.System import readers
from smartcard.util import toHexString
from smartcard.scard import *
import signal  
from datetime import datetime as dt
from time import sleep

from administradorDatos import inicializar_datos

def leer():

    def sigint_handler(signal, frame): 
        print('Proceso interrumpido')
        exit(0)

    signal.signal(signal.SIGINT, sigint_handler)

    l_atr = 1   
    oldATR = 0  

    APDU_command = [0xFF, 0xCA, 0x00, 0x00, 0x00]

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
          
    print("Ejecutando programa. Por favor, ingrese una tarjeta NFC en el lector...")    
    while True:
        
        sleep(0.1)
        try:
            try:
                    
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

            except SystemError: 
                oldATR = 0
                continue

            try:
                if l_atr == oldATR:
                    continue
            except UnboundLocalError: 
                pass                  

            oldATR = l_atr

            if len(l_atr):
                pass
            else:
                continue
   
            l_atr = f'ID{l_atr}' 
            row = df.loc[df['card_uid'] == l_atr] 
            if not row.empty:

                print(f" -> Lectura, fecha: \033[1;32m{dt.now().strftime('%d/%m/%Y, %H:%M:%S')}\033[0m, por \033[1;33m{row['nombre'].values[0]}\033[0m, contenido \n{row}\n")

            else:

                print(f' Nueva lectura desconocida, UID: {l_atr}')
    
            sleep(0.5)

        except ValueError as e: 
            print(e)
            exit(1)
          

if __name__ == '__main__':
    leer()