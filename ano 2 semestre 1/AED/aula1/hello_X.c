#include <stdio.h>

int main(void){
    char nome[50];

    fgets(nome, 50, stdin);
    printf("Hello, %s!", nome);

    return 0;
}