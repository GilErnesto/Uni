#!/bin/bash
# This script checks the existence of a file
echo "Checking..."

if [ $# -ne 1 ]; then
  echo "Número de argumentos inválido "
  exit 1
fi

if [[ -f $1 ]]
then
  echo "$1 existe."
else
  echo "$1 não existe"
fi
  echo "...done."
