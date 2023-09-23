# Dolphin SmartCard

Proyecto de lectura de tarjetas **NFC** con base de datos

## Documentación del proyecto

https://caroje.com/doc/dolphin_smartcard/

## Instalar
A continuacion los comandos para actualizar el sistema e instalar las dependencias.
### Arch

```bash
## -Sy Actualiza la informacion del software disponible.
sudo pacman -Sy pcsclite ccid pcsc-tools # PCSCLite versión [=1.9.4]
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

El archivo **lectorUID.py** se mantiene escuchando por tarjetas en el lector e imprime en terminal el **UID** de las mismas (*UID seria la identidad de las tarjetas*)

```bash

source ./venv/bin/activate

python3 interfazNativa.py

```
## Dependencias
 - **apt update**, actualiza la informacion del software disponible
- **virtualenv venv**, crea un directorio llamado _venv_ que contiene un entorno python
- **source _./venv/bin/activate_**, esto activa el entorno para que sea utilizado en lugar del python del sistema
- **pip3 install smartcard**, se uso el instalador de paquetes de python y se agrego el paquete de _*smartcard*_
- **apt install python3-virtualenv**, instala el comando virtualenv en el sistema
- **apt install pcscd**, instalar programa que se dedica a escuchar por lectores de tarjetas
- **apt install libpcsclite-dev**, subdependencia faltante
- **apt install libcairo2-dev**, dependencia de GTK para el renderizado de gráficos
- **apt install libgirepository1.0-dev**, simplifica el proceso de desarrollo de apps GUI basadas en GTK en lenguajes como python
## Requirements
- **swig**: Dependencia de pyscard
- **pyscard**: Biblioteca del lector de tarjetas
- **pandas**: Biblioteca para análisis de datos
- **openpyxl**: Biblioteca que necesita pandas para abrir un excel
- **kivy**: Libreria para hacer aplicaciónes
- **pygobject**: Simplifica la programación orientada a objetos y arquitectura diriguida por eventos
- **pycairo**: Biblioteca de renderizado avanzado de controles de aplicaciones
## TODO
- [x] Hacer un **README**
- [x] Investigar la biblioteca **pyscard**
- [ ] Investigar los comandos de el lector **ACR1252**
- [x] Leer documentación de **python**
- [x] Leer documentacion de **GTK**
- [x] Leer documentacion del módulo **scard**
- [x] Investigar comandos **APDU**
- [x] Leer biblioteca de **Kivy**
- [x] Integrar Base de datos
- [x] Leer biblioteca **GTK**
- [x] Desarrollar GUI
- [ ] Hacer parametros (*argparse*)
- [x] Hacer salida de imagen
- [x] Agregar **.gitignore**
- [ ] Comentar codigo **legacy**
- [ ] Hacer logo
- [ ] Terminar documentación

## Troubleshooting (*Solución de problemas*)
 - Lector no reconocido: La version de la dependencia **pscslite** tiene que estar exactamente en la version **1.9.4** en caso de estar en una version mas actualizada que esa podria no recononcer el lector.
## Colabaradores:
- Allan Hidalgo
- [Johel Hidalgo](https://caroje.com/profile/johelhu/)
## Asesores:
- [Daniel Hidalgo](https://caroje.com/profile/danielhu/)
- [Jeancarlo Hidalgo](https://caroje.com/profile/jeancahu/)
- [Steven Murcia](https://caroje.com/profile/stevenms/)
