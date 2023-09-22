# Dolphin SmartCard

Proyecto de lectura de tarjetas NFC con base de datos

## Documentación del proyecto

https://caroje.com/doc/dolphin_smartcard/

## Instalar
Acontinuacion los comandos para actualizar el sistema e instalar las dependencias.
### Arch

```bash
sudo pacman -Ss ## Actualiza la informacion del software disponible.
sudo pacman -Sy pcsclite
sudo pacman -S python-virtualenv

sudo systemctl start pcscd

virtualenv venv
source ./venv/bin/activate

pip install swig ## Instalar antes de los demas
pip install -r requirements.txt

```

### Ubuntu

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

## Ejectuar codigo (Ubuntu y Arch)

El archivo lectorUID.py se mantiene escuchando por tarjetas en el lector e imprime en terminal el UID de las mismas (UID seria la identidad de las tarjetas)

```bash

source ./venv/bin/activate

python3 interfazNativa.py

```
## Dependencias
 - apt update, actualiza la informacion del software disponible
- virtualenv venv, crea un directorio llamado _venv_ que contiene un entorno python
- source _./venv/bin/activate_, esto activa el entorno para que sea utilizado en lugar del python del sistema
- pip3 install smartcard, se uso el instalador de paquetes de python y se agrego el paquete de _smartcard_
- apt install python3-virtualenv, instala el comando virtualenv en el sistema
- apt install pcscd, instalar programa que se dedica a escuchar por lectores de tarjetas
- apt install libpcsclite-dev, subdependencia faltante
- apt install libcairo2-dev, dependencia de GTK para el renderizado de gráficos
- apt install libgirepository1.0-dev, simplifica el proceso de desarrollo de apps GUI basadas en GTK en lenguajes como python
## Requirements
- swig: Dependencia de pyscard
- pyscard: Biblioteca del lector de tarjetas
- pandas: Biblioteca para análisis de datos
- openpyxl: Biblioteca que necesita pandas para abrir un excel
- kivy: Libreria para hacer aplicaciónes
- pygobject: Simplifica la programación orientada a objetos y arquitectura diriguida por eventos
- pycairo: Biblioteca de renderizado avanzado de controles de aplicaciones

```

## TODO
- [x] Hacer un README
- [ ] Investigar la biblioteca pyscard
- [ ] Investigar los comandos de el lector ACR1252
- [x] Investigar librerias de python presentes en el codigo
- [x] Investigar comandos APDU
- [x] Leer biblioteca de Kivy
- [x] Arreglar Data (50%)
- [x] Leer biblioteca GTK
- [ ] Desarrollar GUI
- [ ] Hacer parametros (argparse)
- [ ] Hacer salida de imagen
- [x] Agregar .gitignore
- [ ] Comentar codigo legacy

## Colabaradores:
- Allan Hidalgo
- [Johel Hidalgo](https://caroje.com/profile/johelhu/)
- [Daniel Hidalgo](https://caroje.com/profile/danielhu/)
- [Jeancarlo Hidalgo](https://caroje.com/profile/jeancahu/)
- [Steven Murcia](https://caroje.com/profile/stevenms/)
