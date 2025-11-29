#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main(int argc, char *argv[])
{
    int i, total_length = 0, valid_args = 0;
    char *joined_text;
    
    if (argc < 2) {
        printf("Uso: %s <palavra1> <palavra2> ... <palavraN>\n", argv[0]);
        printf("Nota: Apenas argumentos que começam com letra serão incluídos.\n");
        return EXIT_FAILURE;
    }
    
    for (i = 1; i < argc; i++) {
        if (strlen(argv[i]) > 0 && isalpha(argv[i][0])) {
            total_length += strlen(argv[i]);
            valid_args++;
            if (valid_args > 1) {
                total_length += 1; 
            }
        }
    }
    
    if (valid_args == 0) {
        printf("Nenhum argumento válido encontrado (argumentos devem começar com letra).\n");
        return EXIT_SUCCESS;
    }
    
    total_length += 1; 
    
    joined_text = (char*)malloc(total_length * sizeof(char));
    if (joined_text == NULL) {
        printf("Erro: Não foi possível alocar memória!\n");
        return EXIT_FAILURE;
    }
    
    strcpy(joined_text, "");
    
    int first_valid = 1;
    for (i = 1; i < argc; i++) {
        if (strlen(argv[i]) > 0 && isalpha(argv[i][0])) {
            if (!first_valid) {
                strcat(joined_text, " ");
            }
            strcat(joined_text, argv[i]);
            first_valid = 0;
        }
    }
    
    printf("Argumentos processados:\n");
    for (i = 1; i < argc; i++) {
        if (strlen(argv[i]) > 0 && isalpha(argv[i][0])) {
            printf("  ✓ '%s' (válido - inicia com letra '%c')\n", argv[i], argv[i][0]);
        } else {
            printf("  ✗ '%s' (ignorado - não inicia com letra)\n", argv[i]);
        }
    }
    
    printf("\nFrase final: %s\n", joined_text);
    printf("Argumentos válidos: %d de %d\n", valid_args, argc - 1);
    printf("Total de caracteres na frase: %d\n", (int)strlen(joined_text));
    
    free(joined_text);
    return EXIT_SUCCESS;
}