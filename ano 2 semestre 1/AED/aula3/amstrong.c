#include <stdio.h>
#include <string.h>

// variaveis
int pot[] = {0, 1, 8, 27, 64, 125, 216, 343, 512, 729};
int armstrong_numbers[10];
int count=0;
char str[10];

int main(void){
    for(int i=100; i < 1000; i++){

        int test = 0;
        sprintf(str, "%d", i); // coverter

        for(int j=0; j<3; j++){ // soma das potencias dos numeros
            switch (str[j])
            {
            case '0':
                test += pot[0];
                break;
            case '1':
                test += pot[1];
                break;
            case '2':
                test += pot[2];
                break;
            case '3':
                test += pot[3];
                break;
            case '4':
                test += pot[4];
                break;
            case '5':
                test += pot[5];
                break;
            case '6':
                test += pot[6];
                break;
            case '7':
                test += pot[7];
                break;
            case '8':
                test += pot[8];
                break;
            case '9':
                test += pot[9];
                break;
            }
        }

            if(i == test){
                armstrong_numbers[count] = test;
                count++;
                printf("%d é um número de armstrong\n", test);
            }
    }


    printf("Por ordem, os número de Armstrong sao: ");
    for(int z=0; z < count; z++){
        if(z == count-1){
            printf("%d", armstrong_numbers[z]);
        } else {
            printf("%d; ", armstrong_numbers[z]);
        }
    }
    printf("\n");
    return 0;
}