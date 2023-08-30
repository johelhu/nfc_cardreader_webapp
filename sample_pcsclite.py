#!/usr/bin/env python

from __future__ import print_function
from smartcard.Exceptions import NoCardException
from smartcard.Exceptions import CardConnectionException
from smartcard.System import readers
from smartcard.util import toHexString
from smartcard.scard import *
from os import system as bash # Para correr comandos de BASH

from datetime import datetime as dt

from sys import exit

import signal
from time import sleep

raspberry=True
try:
    import RPi.GPIO as GPIO

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)
    GPIO.output(7, False)

except ModuleNotFoundError:
    print(f"Ejecución fuera de un entorno Raspberry Pi")
    raspberry=False

#bash('clear')

def sigint_handler(signal, frame):
    print('Interrupted')
    exit(0)
signal.signal(signal.SIGINT, sigint_handler)

l_atr =1
oldATR=0

## Codigos APDU
# Poner el LED rojo:
#APDU_command = [0xFF,0x00,0x40,0x0D,0x04,0x00,0x00,0x00,0x00]

# Leer el UID:
APDU_command = [0xFF,0xCA,0x00,0x00,0x00]


def main():
    while True:
        if raspberry:
            GPIO.output(7, False)
        sleep(0.1)
        try:
            hresult, hcontext = SCardEstablishContext(SCARD_SCOPE_USER)
            #assert hresult==SCARD_S_SUCCESS
            hresult, readers = SCardListReaders(hcontext, [])
            # Hay lectores conectados
            #assert len(readers)>0
            reader = readers[0]
        except:
            bash('./restart_servive_hack.sh')
            sleep(0.5)
            continue
        try:
            # Leer el UID:
            try:
                hresult, hcard, dwActiveProtocol = SCardConnect(
                    hcontext,
                    reader,
                    SCARD_SHARE_SHARED,
                    SCARD_PROTOCOL_T0 | SCARD_PROTOCOL_T1)

                hresult, response = SCardTransmit(
                    hcard,dwActiveProtocol,APDU_command)
                l_atr = str(response).replace(', ','')
                l_atr = l_atr.replace('[','')
                l_atr = l_atr.replace(']','')
                #print(response, l_atr)
                #print(hresult)
            except:
                oldATR=0
                continue
                #print("He fallado :c")
                #exit(1)

            if ( l_atr == oldATR ):
                #exit(1)
                continue

            oldATR=l_atr

            if ( len(l_atr) ):
                pass
            else:
                #exit(1)
                continue
            if raspberry:
                GPIO.output(7, True)
            print(f"{dt.now()}")
            bash('printf "#$( date ): " >> /var/www/html/ingreso.log.txt')
            print(reader, 'El UID es:', l_atr)
            bash('grep ^'+l_atr+' base_de_datos_plana.txt')
            bash('grep ^'+l_atr+' base_de_datos_plana.txt | cut -f 2,3 -d, >> /var/www/html/ingreso.log.txt')
            sleep(0.5)

        except ValueError as e:
            print(e)
            exit(1)

        except CardConnectionException:
            pass
        except NoCardException:
            if ( oldATR ):
                oldATR=0
                print(f"{dt.now()}")
                print(reader, 'La tarjeta se ha retirado')
                if raspberry:
                    GPIO.output(7, False)

if __name__ == '__main__':
    main()
