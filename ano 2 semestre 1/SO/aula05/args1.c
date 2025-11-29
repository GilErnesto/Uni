#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    int i;

    if(argc != 3){
        printf("Erro: O programa deve receber exatamente dois argumentos!\n");
        printf("Uso: %s <arg1> <arg2>\n", argv[0]);
        return EXIT_FAILURE;
    }

    for(i = 0 ; i < argc ; i++)
    {
        printf("Argument %02d: \"%s\"\n", i, argv[i]);        
    }

    return EXIT_SUCCESS;
}
