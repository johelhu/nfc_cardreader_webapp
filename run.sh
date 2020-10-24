#!/bin/bash

EJECUTABLE=./sample_pcsclite.py
#python3 $EJECUTABLE &

(
    while :
    do
	timeout 10 python $EJECUTABLE
   done
) &


while :
do
    read COMMAND
    case $COMMAND in
	quit|salir|'exit')
	    echo "Comando recibido $COMMAND"
	    kill -s 15 %%
	    exit 0
	    ;;
	clearlog)
	    >./ingreso.log
	    echo "Comando ejecutado"
	    ;;
	showlog)
	    cat ./ingreso.log
	    echo "Comando ejecutado"
	    ;;
	escribir)
	    ./loc.log
	    echo "Comando ejecutado"
	    ;;
	*)
	    echo "Comando no reconocido"
	    ;;
    esac

done
