#include <stdio.h>

int count = 0;
int operacoes = 0;


int check(int n, int a[]){
    int r = a[1] / a[0];

    for (int i = 1; i < n; i++) {
        operacoes++;
        
        if (a[i] == r * a[i-1]) { //utilize um algoritmo em lógica negativa
            continue;
        } else {return count;}
    }
    return count++;
}

int main(void){

    int array[] = {1,2,4,8,16,32,64,128,256,512};
    int n = sizeof(array) / sizeof(array[0]);

    check(n, array);

    printf("Resultado: %d\n", count); 
    printf("Nº de operacoes: %d\n", operacoes);

    return 0;
}