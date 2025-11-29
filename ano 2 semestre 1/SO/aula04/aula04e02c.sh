#!/bin/bash

compara() {
	if [ "$1" -eq "$2" ]; then
		return 0
    	elif [ "$1" -gt "$2" ]; then
        	return 1
    	else
        	return 2
    	fi
}

read -p "Introduza o primeiro número: " num1
read -p "Introduza o segundo número: " num2

compara $num1 $num2
resultado=$?


case $resultado in
    	0)
        	echo "Os números são iguais."
        	;;
    	1)
        	echo "O maior número é: $num1"
        	;;
    	2)
        	echo "O maior número é: $num2"
        	;;
esac

