#!/bin/bash
# This script checks the existence of a file
echo "Checking..."

if [ $# -ne 1 ]; then
  echo "Número de argumentos inválido "
  exit 1
fi

if [ -e "$1" ]; then
  echo "$1 existe."

  if [ -f "$1" ]; then
    echo "É um ficheiro normal."
  elif [ -d "$1" ]; then
    echo "É uma diretoria."
  else
    echo "É outro tipo de ficheiro."
  fi

if [ -r "$1" ]; then
  echo "Tem permissão de leitura."
else
  echo "Não tem permissão de leitura."
fi

if [ -w "$1" ]; then
  echo "Tem permissão de escrita."
else
  echo "Não tem permissão de escrita."
fi

if [ -x "$1" ]; then
  echo "Tem permissão de execução."
else
  echo "Não tem permissão de execução."
fi

else
  echo "$item não existe."
fi

echo "...done."
