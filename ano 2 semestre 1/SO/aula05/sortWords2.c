#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_WORDS 100
#define MAX_WORD_LENGTH 256

// Função de comparação para ordenação crescente (case-sensitive)
int compare_ascending(const void *a, const void *b) {
    return strcmp(*(char**)a, *(char**)b);
}

// Função de comparação para ordenação decrescente (case-sensitive)
int compare_descending(const void *a, const void *b) {
    return strcmp(*(char**)b, *(char**)a);
}

// Função de comparação para ordenação crescente (case-insensitive)
int compare_ascending_ignore_case(const void *a, const void *b) {
    return strcasecmp(*(char**)a, *(char**)b);
}

// Função de comparação para ordenação decrescente (case-insensitive)
int compare_descending_ignore_case(const void *a, const void *b) {
    return strcasecmp(*(char**)b, *(char**)a);
}

// Função para remover quebra de linha do final da string
void remove_newline(char *str) {
    int len = strlen(str);
    if (len > 0 && str[len-1] == '\n') {
        str[len-1] = '\0';
    }
}

int main()
{
    char **words;
    char buffer[MAX_WORD_LENGTH];
    char *sort_order;
    char *ignore_case_env;
    int ignore_case = 0;
    int ascending = 1;
    int word_count = 0;
    int valid_count = 0;
    char **valid_words;
    int i;
    
    printf("=== SORTWORDS2 - ORDENADOR INTERATIVO DE PALAVRAS ===\n\n");
    
    // Verificar variáveis de ambiente
    sort_order = getenv("SORTORDER");
    if (sort_order != NULL) {
        if (strcmp(sort_order, "desc") == 0 || strcmp(sort_order, "DESC") == 0) {
            ascending = 0;
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
    
    printf("Configuração atual:\n");
    printf("  Ordem: %s\n", ascending ? "Crescente" : "Decrescente");
    printf("  Ignorar maiúsculas/minúsculas: %s\n", ignore_case ? "Sim" : "Não");
    printf("  (Configure via variáveis SORTORDER e IGNORECASE)\n\n");
    
    // Alocar array para palavras
    words = (char**)malloc(MAX_WORDS * sizeof(char*));
    if (words == NULL) {
        printf("Erro: Não foi possível alocar memória!\n");
        return EXIT_FAILURE;
    }
    
    printf("Digite palavras (máximo %d). Digite 'fim' ou pressione Ctrl+D para terminar:\n", MAX_WORDS);
    
    // Ler palavras do usuário
    while (word_count < MAX_WORDS) {
        printf("%d> ", word_count + 1);
        
        if (fgets(buffer, sizeof(buffer), stdin) == NULL) {
            // EOF (Ctrl+D) ou erro
            break;
        }
        
        remove_newline(buffer);
        
        // Verificar se é comando de fim
        if (strcmp(buffer, "fim") == 0 || strcmp(buffer, "FIM") == 0 || 
            strcmp(buffer, "exit") == 0 || strcmp(buffer, "quit") == 0) {
            break;
        }
        
        // Ignorar linhas vazias
        if (strlen(buffer) == 0) {
            continue;
        }
        
        // Alocar memória para a palavra e copiar
        words[word_count] = (char*)malloc((strlen(buffer) + 1) * sizeof(char));
        if (words[word_count] == NULL) {
            printf("Erro: Não foi possível alocar memória para a palavra!\n");
            break;
        }
        
        strcpy(words[word_count], buffer);
        word_count++;
    }
    
    if (word_count == 0) {
        printf("\nNenhuma palavra foi inserida.\n");
        free(words);
        return EXIT_SUCCESS;
    }
    
    printf("\n=== ANÁLISE DAS PALAVRAS ===\n");
    
    // Contar palavras válidas (que começam com letra)
    for (i = 0; i < word_count; i++) {
        if (strlen(words[i]) > 0 && isalpha(words[i][0])) {
            valid_count++;
        }
    }
    
    if (valid_count == 0) {
        printf("Nenhuma palavra válida encontrada (palavras devem começar com letra).\n");
        
        // Liberar memória
        for (i = 0; i < word_count; i++) {
            free(words[i]);
        }
        free(words);
        return EXIT_SUCCESS;
    }
    
    // Criar array apenas com palavras válidas
    valid_words = (char**)malloc(valid_count * sizeof(char*));
    if (valid_words == NULL) {
        printf("Erro: Não foi possível alocar memória!\n");
        // Liberar memória já alocada
        for (i = 0; i < word_count; i++) {
            free(words[i]);
        }
        free(words);
        return EXIT_FAILURE;
    }
    
    // Copiar apenas palavras válidas
    int valid_index = 0;
    for (i = 0; i < word_count; i++) {
        if (strlen(words[i]) > 0 && isalpha(words[i][0])) {
            valid_words[valid_index] = words[i];
            printf("  ✓ '%s' (incluída)\n", words[i]);
            valid_index++;
        } else {
            printf("  ✗ '%s' (ignorada - não inicia com letra)\n", words[i]);
        }
    }
    
    printf("\nPalavras válidas: %d de %d\n", valid_count, word_count);
    
    // Ordenar usando a função apropriada
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
    
    // Imprimir resultado ordenado
    printf("\n=== PALAVRAS ORDENADAS ===\n");
    for (i = 0; i < valid_count; i++) {
        printf("%d. %s\n", i + 1, valid_words[i]);
    }
    
    // Comparação com comando sort
    printf("\n=== COMPARAÇÃO COM COMANDO 'sort' ===\n");
    printf("Para obter resultado similar com 'sort':\n");
    if (ignore_case && !ascending) {
        printf("  echo -e \"");
        for (i = 0; i < valid_count; i++) {
            printf("%s%s", valid_words[i], (i < valid_count-1) ? "\\n" : "");
        }
        printf("\" | sort -fr\n");
    } else if (ignore_case) {
        printf("  echo -e \"");
        for (i = 0; i < valid_count; i++) {
            printf("%s%s", valid_words[i], (i < valid_count-1) ? "\\n" : "");
        }
        printf("\" | sort -f\n");
    } else if (!ascending) {
        printf("  echo -e \"");
        for (i = 0; i < valid_count; i++) {
            printf("%s%s", valid_words[i], (i < valid_count-1) ? "\\n" : "");
        }
        printf("\" | sort -r\n");
    } else {
        printf("  echo -e \"");
        for (i = 0; i < valid_count; i++) {
            printf("%s%s", valid_words[i], (i < valid_count-1) ? "\\n" : "");
        }
        printf("\" | sort\n");
    }
    
    // Liberar memória
    for (i = 0; i < word_count; i++) {
        free(words[i]);
    }
    free(words);
    free(valid_words);
    
    return EXIT_SUCCESS;
}