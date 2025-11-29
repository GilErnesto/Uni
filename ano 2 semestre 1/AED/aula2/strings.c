#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(void){

    char str1[30] = "Isto é UMA String ";
    char str2[30] = "Isto TAMbém é UMA String ";
    char str1_a[30] = "", str2_a[30] = "", lower1, lower2; 
    char str2_copy[30], concatenated[60];
    size_t c;
    int alpha = 0, upper = 0;

    for (c = 0; c < strlen(str1); c++) {
        if(isalpha(str1[c])){
            alpha++;
        }

        if(isupper(str1[c])){
            lower1 = tolower(str1[c]);
            strncat(str1_a, &lower1, 1);
        } else {strncat(str1_a, &str1[c], 1);}
    }

    for (c = 0; c < strlen(str2); c++) {
        if(isupper(str2[c])){
            upper++;
            lower2 = tolower(str2[c]);
            strncat(str2_a, &lower2, 1);
        }else {strncat(str2_a, &str2[c], 1);}
    }

    printf("String 1: %s\n", str1);
    printf("String 2: %s\n", str2);
    printf("Caracteres alfabéticos em str1: %d\n", alpha);
    printf("Número de caracteres maiúsculos em str2: %d\n", upper);
    printf("Caracteres maiúsculos em str1: %s\n", str1_a);
    printf("Caracteres maiúsculos em str2: %s\n\n", str2_a);

    if (strcmp(str1, str2) == 0) {
        printf("As duas strings são iguais.\n\n");
    } else {
        printf("As strings são diferentes. Em ordem lexicográfica:\n");
        if (strcmp(str1, str2) < 0) {
            printf("1º: %s\n", str1);
            printf("2º: %s\n\n", str2);
        } else {
            printf("1º: %s\n", str2);
            printf("2º: %s\n\n", str1);
        }
    }

    // Criar uma cópia da segunda string
    strcpy(str2_copy, str2);
    printf("Cópia da segunda string: %s\n\n", str2_copy);

    // Concatenar a segunda string com sua cópia
    strcpy(concatenated, str2);
    strcat(concatenated, str2_copy);
    printf("Concatenação de str2 com sua cópia: %s\n", concatenated);

    return 0;
}