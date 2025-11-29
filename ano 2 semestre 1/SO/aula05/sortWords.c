#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int compare_ascending(const void *a, const void *b) {
    return strcmp(*(char**)a, *(char**)b);
}

int compare_descending(const void *a, const void *b) {
    return strcmp(*(char**)b, *(char**)a);
}

int compare_ascending_ignore_case(const void *a, const void *b) {
    return strcasecmp(*(char**)a, *(char**)b);
}

int compare_descending_ignore_case(const void *a, const void *b) {
    return strcasecmp(*(char**)b, *(char**)a);
}

int main(int argc, char *argv[])
{
    int i, valid_count = 0;
    char **valid_words;
    char *sort_order;
    char *ignore_case_env;
    int ignore_case = 0;
    int ascending = 1; 
    
    if (argc < 2) {
        printf("Uso: %s <palavra1> <palavra2> ... <palavraN>\n", argv[0]);
        printf("Nota: Apenas argumentos que começam com letra serão ordenados.\n");
        printf("Variáveis de ambiente:\n");
        printf("  SORTORDER: 'asc' ou 'desc' (padrão: asc)\n");
        printf("  IGNORECASE: 'yes' para ignorar maiúsculas/minúsculas (padrão: no)\n");
        return EXIT_FAILURE;
    }
    
    sort_order = getenv("SORTORDER");
    if (sort_order != NULL) {
        if (strcmp(sort_order, "desc") == 0 || strcmp(sort_order, "DESC") == 0) {
            ascending = 0;
        } else if (strcmp(sort_order, "asc") == 0 || strcmp(sort_order, "ASC") == 0) {
            ascending = 1;
        } else {
            printf("Aviso: SORTORDER='%s' inválido. Usando ordenação crescente.\n", 
                   sort_order);
            printf("Valores válidos: 'asc', 'desc', 'ASC', 'DESC'\n\n");
        }
    }
    
    ignore_case_env = getenv("IGNORECASE");
    if (ignore_case_env != NULL) {
        if (strcmp(ignore_case_env, "yes") == 0 || 
            strcmp(ignore_case_env, "YES") == 0 ||
            strcmp(ignore_case_env, "1") == 0) {
            ignore_case = 1;
        }
    }
    
    for (i = 1; i < argc; i++) {
        if (strlen(argv[i]) > 0 && isalpha(argv[i][0])) {
            valid_count++;
        }
    }
    
    if (valid_count == 0) {
        printf("Nenhum argumento válido encontrado (argumentos devem começar com letra).\n");
        return EXIT_SUCCESS;
    }
    
    valid_words = (char**)malloc(valid_count * sizeof(char*));
    if (valid_words == NULL) {
        printf("Erro: Não foi possível alocar memória!\n");
        return EXIT_FAILURE;
    }
    
    int index = 0;
    for (i = 1; i < argc; i++) {
        if (strlen(argv[i]) > 0 && isalpha(argv[i][0])) {
            valid_words[index] = argv[i];
            index++;
        }
    }
    
    printf("=== CONFIGURAÇÃO DE ORDENAÇÃO ===\n");
    printf("Ordem: %s\n", ascending ? "Crescente" : "Decrescente");
    printf("Ignorar maiúsculas/minúsculas: %s\n", ignore_case ? "Sim" : "Não");
    printf("Argumentos válidos encontrados: %d\n\n", valid_count);
    
    if (ignore_case) {
        if (ascending) {
            qsort(valid_words, valid_count, sizeof(char*), compare_ascending_ignore_case);
        } else {
            qsort(valid_words, valid_count, sizeof(char*), compare_descending_ignore_case);
        }
    } else {
        if (ascending) {
            qsort(valid_words, valid_count, sizeof(char*), compare_ascending);
        } else {
            qsort(valid_words, valid_count, sizeof(char*), compare_descending);
        }
    }
    
    printf("=== ARGUMENTOS PROCESSADOS ===\n");
    for (i = 1; i < argc; i++) {
        if (strlen(argv[i]) > 0 && isalpha(argv[i][0])) {
            printf("  ✓ '%s' (incluído)\n", argv[i]);
        } else {
            printf("  ✗ '%s' (ignorado - não inicia com letra)\n", argv[i]);
        }
    }
    
    printf("\n=== PALAVRAS ORDENADAS ===\n");
    for (i = 0; i < valid_count; i++) {
        printf("%d. %s\n", i + 1, valid_words[i]);
    }
    
    free(valid_words);
    return EXIT_SUCCESS;
}