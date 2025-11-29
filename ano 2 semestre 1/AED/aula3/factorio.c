#include <stdio.h>

// Array com os fatoriais dos dígitos 0-9 (pré-calculado para eficiência)
int factorial[] = {1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880};
//                 0! 1! 2! 3! 4!  5!   6!   7!    8!     9!

// Contador para a operação determinante (extração de dígitos)
long long digit_extractions = 0;

// Função para calcular a soma dos fatoriais dos dígitos
int sum_factorial_digits(int n) {
    int sum = 0;
    int temp = n;
    
    // Caso especial para 0
    if (n == 0) {
        digit_extractions++;
        return factorial[0];
    }
    
    // Extrair cada dígito e somar seu fatorial
    while (temp > 0) {
        digit_extractions++; // Contar operação crítica
        int digit = temp % 10;
        sum += factorial[digit];
        temp /= 10;
    }
    
    return sum;
}

int main(void) {
    printf("Procurando factoriões menores que 1.000.000...\n\n");
    printf("Factoriões encontrados:\n");
    
    int factorions_found = 0;
    
    // Verificar todos os números de 0 até 999.999
    for (int i = 0; i < 1000000; i++) {
        if (i == sum_factorial_digits(i)) {
            printf("%d\n", i);
            factorions_found++;
        }
    }
    
    printf("\nResumo:\n");
    printf("Total de factoriões encontrados: %d\n", factorions_found);
    printf("Número de extrações de dígitos realizadas: %lld\n", digit_extractions);
    printf("Operação crítica: extração de dígitos (divisão por 10 e módulo 10)\n");
    
    // Análise de eficiência
    printf("\nAnálise de eficiência:\n");
    printf("- Factoriais pré-calculados (0! a 9!) evitam recálculo\n");
    printf("- Operação crítica: extração de dígitos O(log n) por número\n");
    printf("- Complexidade total: O(n * log n) onde n = 1.000.000\n");
    
    return 0;
}
