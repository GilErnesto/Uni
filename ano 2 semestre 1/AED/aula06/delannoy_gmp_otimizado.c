#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <gmp.h>

long long adicoes_iterativa = 0;

void delannoy_iterativa_gmp_otimizada(int m, int n, mpz_t resultado) {
    // Com números GMP grandes, cada elemento pode ocupar centenas de bytes
    // Ser muito mais conservador para evitar esgotar a RAM
    int max_linhas_cache = 3000; // Limite muito mais seguro
    
    if (m <= max_linhas_cache && n <= max_linhas_cache) {
        // Para valores pequenos/médios, usar matriz completa (mais rápido)
        printf("    [Usando matriz completa %dx%d = %d elementos]\n", m+1, n+1, (m+1)*(n+1));
        
        mpz_t **dp = malloc((m + 1) * sizeof(mpz_t *));
        for (int i = 0; i <= m; i++) {
            dp[i] = malloc((n + 1) * sizeof(mpz_t));
            for (int j = 0; j <= n; j++) {
                mpz_init(dp[i][j]);
            }
        }
        
        // Inicializar bordas
        for (int i = 0; i <= m; i++) mpz_set_ui(dp[i][0], 1);
        for (int j = 0; j <= n; j++) mpz_set_ui(dp[0][j], 1);
        
        // Preencher matriz
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                mpz_add(dp[i][j], dp[i-1][j], dp[i-1][j-1]);
                mpz_add(dp[i][j], dp[i][j], dp[i][j-1]);
                adicoes_iterativa += 2;
            }
        }
        
        mpz_set(resultado, dp[m][n]);
        
        // Liberar memória
        for (int i = 0; i <= m; i++) {
            for (int j = 0; j <= n; j++) {
                mpz_clear(dp[i][j]);
            }
            free(dp[i]);
        }
        free(dp);
    } else {
        // Para valores grandes (k>3000), usar duas linhas (economia de memória)
        printf("    [Usando duas linhas para economia de memória]\n");
        
        mpz_t *linha_anterior = malloc((n + 1) * sizeof(mpz_t));
        mpz_t *linha_atual = malloc((n + 1) * sizeof(mpz_t));
        
        // Inicializar as duas linhas
        for (int j = 0; j <= n; j++) {
            mpz_init(linha_anterior[j]);
            mpz_init(linha_atual[j]);
            mpz_set_ui(linha_anterior[j], 1);
        }
        
        // Processar linha por linha
        for (int i = 1; i <= m; i++) {
            mpz_set_ui(linha_atual[0], 1);
            
            for (int j = 1; j <= n; j++) {
                mpz_add(linha_atual[j], linha_anterior[j], linha_anterior[j-1]);
                mpz_add(linha_atual[j], linha_atual[j], linha_atual[j-1]);
                adicoes_iterativa += 2;
            }
            
            // Trocar as linhas
            mpz_t *temp = linha_anterior;
            linha_anterior = linha_atual;
            linha_atual = temp;
        }
        
        mpz_set(resultado, linha_anterior[n]);
        
        // Liberar memória
        for (int j = 0; j <= n; j++) {
            mpz_clear(linha_anterior[j]);
            mpz_clear(linha_atual[j]);
        }
        free(linha_anterior);
        free(linha_atual);
    }
}

int main() {
    printf("=== NÚMEROS DE DELANNOY COM GMP OTIMIZADO ===\n");
    printf("(Limite conservador: matriz completa até k=3000)\n\n");
    
    // Agora valores grandes
    printf("\n=== VALORES GRANDES ===\n");
    int valores[] = {50, 100, 500, 1000, 2000, 3000, 5000, 10000, 20000, 100000};
    int num_valores = sizeof(valores) / sizeof(valores[0]);
    
    for (int i = 0; i < num_valores; i++) {
        int k = valores[i];
        mpz_t resultado;
        mpz_init(resultado);
        adicoes_iterativa = 0;
        
        printf("Calculando D(%d,%d)...", k, k);
        fflush(stdout);
        clock_t inicio = clock();
        delannoy_iterativa_gmp_otimizada(k, k, resultado);
        clock_t fim = clock();
        double tempo = ((double)(fim - inicio)) / CLOCKS_PER_SEC;
        
        printf(" CONCLUÍDO!\n");
        printf("D(%d,%d) tem %zu dígitos\n", k, k, mpz_sizeinbase(resultado, 10));
        
        // Mostrar qual estratégia foi usada
        if (k <= 3000) {
            printf("Estratégia: Matriz completa O(%d) - velocidade máxima\n", k*k);
        } else {
            printf("Estratégia: Duas linhas O(%d) - economia de memória\n", k);
        }
        
        // Só mostrar o número completo se tiver menos de 100 dígitos
        if (mpz_sizeinbase(resultado, 10) <= 100) {
            printf("D(%d,%d) = ", k, k);
            mpz_out_str(stdout, 10, resultado);
            printf("\n");
        } else {
            // Mostrar apenas início e fim do número
            char *str = mpz_get_str(NULL, 10, resultado);
            int len = strlen(str);
            printf("D(%d,%d) = %.*s...%s\n", k, k, 30, str, str + len - 30);
            free(str);
        }
        
        printf("Tempo: %.6f segundos, Adições: %lld\n", tempo, adicoes_iterativa);
        printf("────────────────────────────────────────\n\n");
        
        mpz_clear(resultado);
        
        // Para se demorar mais de 300 segundos (5 minutos)
        if (tempo > 300.0) {
            printf("Parando aqui devido ao tempo...\n");
            break;
        }
    }
    
    return 0;
}