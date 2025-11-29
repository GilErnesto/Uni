#include <stdio.h>
#include <math.h>

int main(void){
    int i, n;

    printf("Introduza um número: ");
    scanf("%d", &i);
    for(n=1; n <= i; n++){
        printf("| Nº: %d | Nº2: %d | Nº½: %.2f |\n", n, n*n, sqrt(n));
    }

    return 0;
}
