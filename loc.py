#!/usr/bin/env python3

import sys

Archivo = open("hola.txt","a")

while True:
	UID = input("Escribe el UID: ")
	try:
		int(UID)
		Archivo.write(UID + ", ")
		break
	except:
		print('El UID debe ser un numero')

Nombre = input("Escribe el Nombre: ")
Archivo.write(Nombre + ", ")

while True:
	Beca = input("Escribe (ConBeca, SinBeca): ")
	if Beca == 'SinBeca' or Beca == 'ConBeca':
		break
Archivo.write(Beca + "\n")

Archivo.close()

sys.exit(0)
