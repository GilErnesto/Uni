#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    int i, total_length = 0;
    char *joined_text;
    
    if (argc < 2) {
        printf("Uso: %s <palavra1> <palavra2> ... <palavraN>\n", argv[0]);
        return EXIT_FAILURE;
    }
    
    for (i = 1; i < argc; i++) {
        total_length += strlen(argv[i]);
        if (i < argc - 1) {
            total_length += 1; 
        }
    }
    total_length += 1; 
    
    joined_text = (char*)malloc(total_length * sizeof(char));
    if (joined_text == NULL) {
        printf("Erro: Não foi possível alocar memória!\n");
        return EXIT_FAILURE;
    }
    
    strcpy(joined_text, "");
    
    for (i = 1; i < argc; i++) {
        strcat(joined_text, argv[i]);
        if (i < argc - 1) {
            strcat(joined_text, " ");
        }
    }
    
    printf("Frase completa: %s\n", joined_text);
    printf("Total de caracteres: %d\n", (int)strlen(joined_text));
    
    free(joined_text);
    return EXIT_SUCCESS;
}
