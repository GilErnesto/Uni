#!/bin/bash
num=$1
txt=$2

case $num in
  [0-9] | [1-9][0-9] )
    echo "Primeiro argumento válido: $num"
    ;;
  * )
    echo "Erro: o primeiro argumento deve ser número entre 0 e 99."
    exit 1
    ;;
esac

case $txt in
  sec* )
    echo "Segundo argumento válido: $txt"
    ;;
  * )
    echo "Erro: o segundo argumento deve começar por 'sec'."
    exit 1
    ;;
esac
