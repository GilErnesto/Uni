#include <stdio.h>
#include <assert.h>

int count = 0; 
int comparacoes = 0;  

int check(int n, int array[]){
    for (int i = 1; i < n - 1; i++) {
        comparacoes++;
        if (array[i] == array[i - 1] + array[i + 1]) {
            count++;
        }
    }
    return count;
}

int main(void) {
    int array[] = {0 ,2 ,2 ,0 ,3 ,3, 0 ,4, 4, 0 };
    int n = sizeof(array) / sizeof(array[0]);

    check(n, array);

    printf("Resultado: %d\n", count); // respeita a prop
    printf("Nº de comparações: %d\n", comparacoes);

    return 0;
}
