# nfc_cardreader_webapp
Esto es un proyecto para bitacora de tarjetas NFC

## Visualizacion de pagina de bitacoras

https://danielhu7.github.io/nfc_cardreader_webapp/html/template/index.html

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

virtualenv venv
source ./venv/bin/activate

pip3 install -r requirements.txt

```

## Ejectuar codigo (ubuntu)

El archivo sample_pcsclite.py se mantiene escuchando por tarjetas en el lector e imprime en terminal el UID de las mismas (UID seria la identidad de las tarjetas)

```bash

source ./venv/bin/activate

python3 sample_pcsclite.py

```
## Colabaradores:
- Allan Hidalgo
- Johel Hidalgo
