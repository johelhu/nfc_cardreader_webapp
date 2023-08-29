# nfc_cardreader_webapp
Esto es un proyecto para bitacora de tarjetas NFC

## Visualizacion de pagina de bitacoras

https://danielhu7.github.io/nfc_cardreader_webapp/html/template/index.html

## Instalar (ubuntu)

Acontinuacion los comandos para actualizar el sistema e instalar las dependencias.

- apt update, actualiza la informacion del software disponible
- apt install python3-virtualenv, instala el comando virtualenv en el sistema
- virtualenv venv, crea un directorio llamado _venv_ que contiene un entorno python
- source ./venv/bin/activate, esto activa el entorno para que sea utilizado en lugar del python del sistema

```bash
sudo apt update
sudo apt install python3-virtualenv

virtualenv venv
source ./venv/bin/activate

bash run.sh

```
