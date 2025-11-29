#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Usando __int128 para maior capacidade
typedef __int128 big_int;

long long adicoes_recursiva = 0;
long long adicoes_iterativa = 0;
long long adicoes_memoization = 0;

#define MAX_SIZE 100
big_int memo[MAX_SIZE][MAX_SIZE];
int memo_initialized = 0;

// Função para imprimir __int128
void print_int128(big_int num) {
    if (num == 0) {
        printf("0");
        return;
    }
    
    char str[50];
    int i = 0;
    int negative = 0;
    
    if (num < 0) {
        negative = 1;
        num = -num;
    }
    
    while (num > 0) {
        str[i++] = '0' + (num % 10);
        num /= 10;
    }
    
    if (negative) printf("-");
    
    for (int j = i - 1; j >= 0; j--) {
        printf("%c", str[j]);
    }
}

void init_memo() {
    for (int i = 0; i < MAX_SIZE; i++)
        for (int j = 0; j < MAX_SIZE; j++)
            memo[i][j] = -1;
    memo_initialized = 1;
}

big_int delannoy_recursiva(int m, int n) {
    if (m == 0 || n == 0) return 1;
    big_int d1 = delannoy_recursiva(m - 1, n);
    big_int d2 = delannoy_recursiva(m - 1, n - 1);
    big_int d3 = delannoy_recursiva(m, n - 1);
    adicoes_recursiva += 2;
    return d1 + d2 + d3;
}

big_int delannoy_iterativa(int m, int n) {
    big_int **dp = malloc((m + 1) * sizeof(big_int *));
    for (int i = 0; i <= m; i++)
        dp[i] = malloc((n + 1) * sizeof(big_int));
    for (int i = 0; i <= m; i++) dp[i][0] = 1;
    for (int j = 0; j <= n; j++) dp[0][j] = 1;
    for (int i = 1; i <= m; i++)
        for (int j = 1; j <= n; j++) {
            dp[i][j] = dp[i-1][j] + dp[i-1][j-1] + dp[i][j-1];
            adicoes_iterativa += 2;
        }
    big_int resultado = dp[m][n];
    for (int i = 0; i <= m; i++) free(dp[i]);
    free(dp);
    return resultado;
}

big_int delannoy_memoization(int m, int n) {
    if (m < MAX_SIZE && n < MAX_SIZE && memo[m][n] != -1) return memo[m][n];
    big_int resultado;
    if (m == 0 || n == 0) resultado = 1;
    else {
        big_int d1 = delannoy_memoization(m - 1, n);
        big_int d2 = delannoy_memoization(m - 1, n - 1);
        big_int d3 = delannoy_memoization(m, n - 1);
        adicoes_memoization += 2;
        resultado = d1 + d2 + d3;
    }
    if (m < MAX_SIZE && n < MAX_SIZE) memo[m][n] = resultado;
    return resultado;
}

void reset_contadores() {
    adicoes_recursiva = 0;
    adicoes_iterativa = 0;
    adicoes_memoization = 0;
}

int encontrar_max_k_recursiva() {
    for (int k = 1; k <= 20; k++) {
        reset_contadores();
        clock_t inicio = clock();
        delannoy_recursiva(k, k);
        clock_t fim = clock();
        double tempo = ((double)(fim - inicio)) / CLOCKS_PER_SEC;
        if (tempo > 2.0) return k - 1;
    }
    return 20;
}



int main() {
   /* printf("=== NÚMEROS DE DELANNOY ===\n");
    reset_contadores();
    big_int r1 = delannoy_recursiva(3, 3);
    printf("Recursiva: ");
    print_int128(r1);
    printf(" %lld\n", adicoes_recursiva);
    reset_contadores();
    big_int r2 = delannoy_iterativa(3, 3);
    printf("Iterativa: ");
    print_int128(r2);
    printf(" %lld\n", adicoes_iterativa);
    init_memo();
    reset_contadores();
    big_int r3 = delannoy_memoization(3, 3);
    printf("Memoization: ");
    print_int128(r3);
    printf(" %lld\n", adicoes_memoization);
    int max_k = encontrar_max_k_recursiva();
    printf("Maior k: %d\n", max_k);
    
    printf("\n=== NÚMEROS DE DELANNOY DE 1 A 10 ===\n");
    for (int k = 1; k <= 10; k++) {
        reset_contadores();
        big_int resultado = delannoy_iterativa(k, k);
        printf("D(%d,%d) = ", k, k);
        print_int128(resultado);
        printf("\n");
    }*/
    printf("\n=== CALCULANDO MAIOR D(K,K) POSSÍVEL ===\n");
    int k = 50; // Começar com valor menor
    big_int ultimo_resultado = 0;
    int ultimo_k_valido = 0;
    
    while (1) {
        reset_contadores();
        clock_t inicio = clock();
        big_int resultado = delannoy_iterativa(k, k);
        clock_t fim = clock();
        double tempo = ((double)(fim - inicio)) / CLOCKS_PER_SEC;
        
        printf("D(%d,%d) = ", k, k);
        print_int128(resultado);
        printf(" (tempo: %.6f s, adições: %lld)\n", tempo, adicoes_iterativa);
        
        // Verifica se houve overflow - número negativo ou muito pequeno comparado ao anterior
        if (resultado < 0 || (ultimo_resultado > 0 && resultado < ultimo_resultado / 2)) {
            printf("Possível overflow detectado em k=%d\n", k);
            break;
        }
        
        // Para se demorar mais que 5 segundos
        if (tempo > 5.0) {
            printf("Tempo limite excedido em k=%d\n", k);
            break;
        }
        
        ultimo_resultado = resultado;
        ultimo_k_valido = k;
        k += 50; // Incremento menor para melhor precisão
        
        // Limite de segurança
        if (k > 5000) {
            printf("Limite de segurança atingido em k=%d\n", k);
            break;
        }
    }
    
    printf("Maior k calculado com sucesso: %d\n", ultimo_k_valido);
    printf("D(%d,%d) = ", ultimo_k_valido, ultimo_k_valido);
    print_int128(ultimo_resultado);
    printf("\n");
    return 0;
}
