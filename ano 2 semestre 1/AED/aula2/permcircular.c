#include <stdio.h>

void permute(int* a, int* b, int* c){
    int temp;

    temp = *a;
    (*a) = *b;
    (*b) = *c;
    (*c) = temp;

}

int main(void){
    int a = 10, b = 20, c = 30;

    permute(&a, &b, &c);
    printf("A permutação circular deu, a: %d b: %d c: %d \n", a, b, c);

    return 0;
}