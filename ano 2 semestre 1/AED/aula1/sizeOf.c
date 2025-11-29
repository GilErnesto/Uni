#include <stdio.h>

int main(void){
    printf("Para 64bits\n");
    printf("sizeof(void *) ...... %zu\nsizeof(void) ........ %zu\nsizeof(char) ........ %zu\nsizeof(short) ....... %zu\nsizeof(int) ......... %zu\nsizeof(long) ........ %zu\nsizeof(long long) ... %zu\nsizeof(float) ....... %zu\nsizeof(double) ...... %zu\n", sizeof(void*), sizeof(void), sizeof(char), sizeof(short), sizeof(int), sizeof(long), sizeof(long long), sizeof(float), sizeof(double));

    return 0;
}