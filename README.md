# Dolphin SmartCard

Proyecto de lectura de tarjetas NFC con base de datos

## Documentación del proyecto

https://caroje.com/doc/dolphin_smartcard/

## Instalar (ubuntu)

Acontinuacion los comandos para actualizar el sistema e instalar las dependencias.

- apt update, actualiza la informacion del software disponible
- apt install python3-virtualenv, instala el comando virtualenv en el sistema
- virtualenv venv, crea un directorio llamado _venv_ que contiene un entorno python
- source _./venv/bin/activate_, esto activa el entorno para que sea utilizado en lugar del python del sistema
- pip3 install smartcard, se uso el instalador de paquetes de python y se agrego el paquete de _smartcard_
- apt install pcscd, instalar programa que se dedica a escuchar por lectores de tarjetas
- apt install libpcsclite-dev, subdependencia faltante

```bash
sudo apt update
sudo apt install pcscd
sudo apt install libpcsclite-dev
sudo apt install python3-virtualenv
sudo apt install libcairo2-dev
sudo apt install libgirepository1.0-dev

virtualenv venv
source ./venv/bin/activate

pip3 install -r requirements.txt

```

## Ejectuar codigo (ubuntu)

El archivo sample_pcsclite.py se mantiene escuchando por tarjetas en el lector e imprime en terminal el UID de las mismas (UID seria la identidad de las tarjetas)

```bash

source ./venv/bin/activate

python3 sample_2.0.py

```

## Requirements

```bash

swig: Dependencia de pyscard
pyscard: Biblioteca del lector de tarjetas
pandas: Biblioteca para análisis de datos
openpyxl: Biblioteca que necesita pandas para abrir un excel
kivy: Libreria para hacer aplicaciónes

```

## TODO
- [x] Hacer un README
- [ ] Investigar la biblioteca pyscard
- [ ] Investigar los comandos de el lector ACR1252
- [x] Investigar librerias de python presentes en el codigo
- [x] Investigar comandos APDU
- [x] Leer biblioteca de Kivy
- [x] Arreglar Data (50%)

## Colabaradores:
- Allan Hidalgo
- Johel Hidalgo
- Daniel Hidalgo
- Jeancarlo Hidalgo
- Steven Murcia
