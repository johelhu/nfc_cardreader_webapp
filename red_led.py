#!/bin/python
import sys
from smartcard.scard import *

hresult, hcontext = SCardEstablishContext(SCARD_SCOPE_USER)

assert hresult==SCARD_S_SUCCESS

hresult, readers = SCardListReaders(hcontext, [])

# Hay lectores conectados
assert len(readers)>0

# Selecciona por defecto el primer lector en lista
reader = readers[0]

try:
    hresult, hcard, dwActiveProtocol = SCardConnect(
        hcontext,
        reader,
        SCARD_SHARE_SHARED,
        SCARD_PROTOCOL_T0 | SCARD_PROTOCOL_T1)
except:
    print("He fallado :c")
    sys.exit(1)

#APDU_command = [0xFF,0xCA,0x00,0x00,0x00]

# Poner el LED rojo:
APDU_command = [0xFF,0x00,0x40,0x0D,0x04,0x00,0x00,0x00,0x00]

# Leer el UID:
APDU_command = [0xFF,0xCA,0x00,0x00,0x00]
hresult, response = SCardTransmit(hcard,dwActiveProtocol,APDU_command)
                                  
print(response)

sys.exit(0)
