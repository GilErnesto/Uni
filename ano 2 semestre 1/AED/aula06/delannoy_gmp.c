#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <gmp.h>

long long adicoes_iterativa = 0;

void delannoy_iterativa_gmp(int m, int n, mpz_t resultado) {
    // Criar matriz dinâmica de mpz_t
    mpz_t **dp = malloc((m + 1) * sizeof(mpz_t *));
    for (int i = 0; i <= m; i++) {
        dp[i] = malloc((n + 1) * sizeof(mpz_t));
        for (int j = 0; j <= n; j++) {
            mpz_init(dp[i][j]);
        }
    }
    
    // Inicializar bordas com 1
    for (int i = 0; i <= m; i++) mpz_set_ui(dp[i][0], 1);
    for (int j = 0; j <= n; j++) mpz_set_ui(dp[0][j], 1);
    
    // Preencher a matriz
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            mpz_add(dp[i][j], dp[i-1][j], dp[i-1][j-1]);
            mpz_add(dp[i][j], dp[i][j], dp[i][j-1]);
            adicoes_iterativa += 2;
        }
    }
    
    // Copiar resultado
    mpz_set(resultado, dp[m][n]);
    
    // Liberar memória
    for (int i = 0; i <= m; i++) {
        for (int j = 0; j <= n; j++) {
            mpz_clear(dp[i][j]);
        }
        free(dp[i]);
    }
    free(dp);
}

int main() {
    printf("=== NÚMEROS DE DELANNOY COM GMP ===\n");
    /*
    // Teste com valores pequenos primeiro
    printf("\n=== TESTE PEQUENOS ===\n");
    for (int k = 1; k <= 10; k++) {
        mpz_t resultado;
        mpz_init(resultado);
        adicoes_iterativa = 0;
        
        delannoy_iterativa_gmp(k, k, resultado);
        
        printf("D(%d,%d) = ", k, k);
        mpz_out_str(stdout, 10, resultado);
        printf("\n");
        
        mpz_clear(resultado);
    }*/
    
    // Agora valores grandes
    printf("\n=== VALORES GRANDES ===\n");
    int valores[] = {50, 100, 200, 500, 1000, 5000, 20000, 100000};
    int num_valores = sizeof(valores) / sizeof(valores[0]);
    
    for (int i = 0; i < num_valores; i++) {
        int k = valores[i];
        mpz_t resultado;
        mpz_init(resultado);
        adicoes_iterativa = 0;
        
        printf("Calculando D(%d,%d)...", k, k);
        fflush(stdout); // Forçar output imediato
        clock_t inicio = clock();
        delannoy_iterativa_gmp(k, k, resultado);
        clock_t fim = clock();
        double tempo = ((double)(fim - inicio)) / CLOCKS_PER_SEC;
        
        printf(" CONCLUÍDO!\n");
        printf("D(%d,%d) tem %zu dígitos\n", k, k, mpz_sizeinbase(resultado, 10));
        
        // Só mostrar o número completo se tiver menos de 200 dígitos
        if (mpz_sizeinbase(resultado, 10) <= 200) {
            printf("D(%d,%d) = ", k, k);
            mpz_out_str(stdout, 10, resultado);
            printf("\n");
        } else {
            // Mostrar apenas início e fim do número
            char *str = mpz_get_str(NULL, 10, resultado);
            int len = strlen(str);
            printf("D(%d,%d) = %.*s...%s\n", k, k, 50, str, str + len - 50);
            free(str);
        }
        
        printf("Tempo: %.6f segundos, Adições: %lld\n\n", tempo, adicoes_iterativa);
        
        mpz_clear(resultado);
        
        // Para se demorar mais de 600 segundos (10 minutos)
        if (tempo > 600.0) {
            printf("Parando aqui devido ao tempo...\n");
            break;
        }
    }
    
    return 0;
}