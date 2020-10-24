#!/usr/bin/env python

from __future__ import print_function
from smartcard.Exceptions import NoCardException
from smartcard.Exceptions import CardConnectionException
from smartcard.System import readers
from smartcard.util import toHexString
from smartcard.scard import *
import os, sys # Para correr comandos de BASH
import signal
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.output(7, False)

#os.system('clear')

def sigint_handler(signal, frame):
    print('Interrupted')
    sys.exit(0)
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
            os.system('./restart_servive_hack.sh')
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
                #sys.exit(1)

            if ( l_atr == oldATR ):
                #sys.exit(1)
                continue
            
            oldATR=l_atr

            if ( len(l_atr) ):
                pass
            else:
                #sys.exit(1)
                continue
            GPIO.output(7, True)
            os.system('date')
            os.system('printf "#$( date ): " >> /var/www/html/ingreso.log.txt')
            print(reader, 'El UID es:', l_atr)
            os.system('grep ^'+l_atr+' base_de_datos_plana.txt')
            os.system('grep ^'+l_atr+' base_de_datos_plana.txt | cut -f 2,3 -d, >> /var/www/html/ingreso.log.txt')
            sleep(0.5)

        except CardConnectionException:
            pass
        except NoCardException:
            if ( oldATR ):
                oldATR=0
                os.system('date')
                print(reader, 'La tarjeta se ha retirado')
                GPIO.output(7, False)
                
if __name__ == '__main__':
    main()
