#include <stdio.h>

int count = 0;
int operacoes = 0;


int check(int n, int a[]){
    // i < j < k
    // a[k] = a[i] + a[j]
    for (int i=0; i < n-3; i++) {
        for (int j=0; j<n-2; j++) {
            if (i<j){
                for (int k=0; k<n-1; k++) {
            

                    if(a[k] == a[i] + a[j]){


                    }
                }
            }
            break;
        }
    }
}

int main(void){

    int array[] = {};
    int n = sizeof(array) / sizeof(array[0]);

    check(n, array);

    printf("Resultado: %d\n", count); 
    printf("Nº de operacoes: %d\n", operacoes);

    return 0;
}