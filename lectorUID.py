#!/usr/bin/env python #Le dice al sistema como debe interpretar y ejecutar el archivo

from smartcard.Exceptions import NoCardException         # Maneja situaciones en las que no se detecta ninguna tarjeta  
from smartcard.Exceptions import CardConnectionException # Proporciona una excepcion para problemas de conexion de tarjeta
from smartcard.System import readers    # Funciones para interactuar con los lectores
from smartcard.util import toHexString  # Convierte datos en formato hexadecimal
from smartcard.scard import *           # Funciones y constantes relacionadas al contexto de tarjetas inteligentes
from datetime import datetime as dt     # Módulo para majenar fechas y horas en python
from time import sleep                  # Se utiliza para poder hacer pausas
import subprocess                       # Permite generar procesos secundarios

from administradorDatos import inicializar_datos # Funcion para administrar datos en un excel

def leer(funcion_salida): # llama la funcion leer
    subprocess.run(['clear'], shell=True) # Limpia la terminal (similar a "bash('clear')", necesario por ser un subprocess)
    id_tarjeta = 1   # Iniciamos 2 variables
    id_tarjeta_pasada = 0  

    APDU_command = [0xFF, 0xCA, 0x00, 0x00, 0x00] # Leer UID mediante comandos APDU

    df = inicializar_datos("data.xlsx") # Sacamos la variable df de la funcion inicializar_datos

    try: # Manejar posibles excepciones

        hresult, hcontext = SCardEstablishContext(SCARD_SCOPE_USER)  # Establece el contexto de comunicación
        hresult, readers = SCardListReaders(hcontext, []) # Lista los lectores disponibles

        if not readers: # Si no se encuentran lectores
            print("Conecte el lector")
            exit(1)

        reader = readers[0] # cambia la variable
    except ValueError: # Si ocurre un erros salir del programa
        exit(1)
          
    print("Ejecutando programa. Por favor, ingrese una tarjeta NFC en el lector...")   

    while True:

        sleep(0.6)
        try:        
            hresult, hcard, dwActiveProtocol = SCardConnect( # Funcion que  establece conexion con una tarjeta intelijente
                hcontext, # Contexto previamente establecido
                reader,  # Nombre del lector al cual se quiere conectar
                SCARD_SHARE_SHARED,  # Especifica como se conectara el lector
                SCARD_PROTOCOL_T0 | SCARD_PROTOCOL_T1) # Especifica como se compartira el lector
            hresult, response = SCardTransmit( # Envia un comando APDU a la tarjeta y resive la respuesta
                hcard, dwActiveProtocol, APDU_command) # Contiene el resultado y la respuesta de la tarjeta
            # [1, 2, 2, 3, 2, 1]
            id_tarjeta = str(response).replace(', ', '') # "[122321]"
            id_tarjeta = id_tarjeta.replace('[', '') # "122321]"
            id_tarjeta = id_tarjeta.replace(']', '') # "122321"

            if not len(id_tarjeta): # Si esta vació regresamos al while
                continue

            if id_tarjeta == id_tarjeta_pasada: # Si estamos leyendo la misma tarjeta regresamos al while
                continue

            id_tarjeta_pasada = id_tarjeta  # La tarjeta reciente se convierte en la pasada    
            id_tarjeta = f'ID{id_tarjeta}' # Lo igualamos al formato en el excel

            salida_df = df.loc[df['card_uid'] == id_tarjeta] # Compara el id de la tarjeta con el de la base de datos
            if not salida_df.empty: # si no esta vacío inicia el if
                
                str_contenido = salida_df # Guarda toda la variable de salida
                print(salida_df) # La imprime

                funcion_salida( # Guarda datos de la df de salida en variables
                        nombre = f"{salida_df['nombre'].values[0]}  {salida_df['primer_apellido'].values[0]}  {salida_df['segundo_apellido'].values[0]}",
                        fecha = dt.now().strftime('%d/%m/%Y, %H:%M:%S'),
                        grupo = f"{salida_df['grado'].values[0]} - {salida_df['grupo'].values[0]}",
                        beca = salida_df['beca'].values[0],
                        uid = salida_df['card_uid'].values[0],
                        ne = salida_df['necesidades_especiales'].values[0],
                    )
            else:

                # Pasa si hay una lectura y no esta en la base de datos
                str_contenido = f' Nueva lectura desconocida, UID: {id_tarjeta}'
                print(str_contenido)
                
                funcion_salida( # Ya que es una lectura desconocida no tiene datos
                        nombre = "Desconocido",
                        fecha = dt.now().strftime('%d/%m/%Y, %H:%M:%S'),
                        grupo = 0,
                        beca = 0,
                        uid = id_tarjeta,
                        ne = 0,
                    )
            
        except SystemError: # SystemError ocurre porque no hay tarjeta en el lector
            id_tarjeta_pasada = 0

        except ValueError as e: # Manejo de excepciones
            print(e)
            exit(1)

        except UnboundLocalError as e: 
            print(e)
            exit(1)

        except TypeError as e: # Error que ocurre cuando la lista se convierte en un (int)
            print(e)
            exit(1)


if __name__ == '__main__': # Verifica que este sea el modulo principal
    leer() # Si lo es corre toda la funcion