#!/bin/bash
# For all the files in a folder, show their properties

if [ $# -ne 1 ]; then
  echo "Erro: foi usado mais do que um argumento"
  exit 1
fi

if [ ! -d "$1" ]; then
  echo "Erro: $1 não é uma diretoria válida."
  exit 1
fi

for f in "$1"/*
do
  file "$f"
done
