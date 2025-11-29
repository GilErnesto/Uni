#!/bin/bash

function imprime_msg()
{
    echo "A minha primeira funcao"
    return 0
}

function mostra_info()
{
    echo "Data: $(date)"
    echo "PC: $(hostname)"
    echo "Utilizador: $(whoami)"
    return 0
}
