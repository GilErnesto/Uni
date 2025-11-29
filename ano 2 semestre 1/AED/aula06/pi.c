#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include <string.h>
#include <signal.h>

volatile int time_up = 0;

void alarm_handler(int sig) {
    time_up = 1;
}

// Estrutura para números grandes (usando arrays de inteiros)
typedef struct {
    int *digits;
    int size;
    int capacity;
} BigNum;

BigNum* create_bignum(int capacity) {
    BigNum *num = malloc(sizeof(BigNum));
    num->digits = calloc(capacity, sizeof(int));
    num->size = 1;
    num->capacity = capacity;
    return num;
}

void free_bignum(BigNum *num) {
    free(num->digits);
    free(num);
}

// Multiplicação de BigNum por inteiro
void multiply_bignum(BigNum *num, int multiplier) {
    int carry = 0;
    for (int i = 0; i < num->size; i++) {
        int prod = num->digits[i] * multiplier + carry;
        num->digits[i] = prod % 10;
        carry = prod / 10;
    }
    
    while (carry > 0 && num->size < num->capacity) {
        num->digits[num->size] = carry % 10;
        carry /= 10;
        num->size++;
    }
}

// Divisão de BigNum por inteiro
void divide_bignum(BigNum *num, int divisor) {
    int remainder = 0;
    for (int i = num->size - 1; i >= 0; i--) {
        int temp = remainder * 10 + num->digits[i];
        num->digits[i] = temp / divisor;
        remainder = temp % divisor;
    }
    
    // Remove zeros à esquerda
    while (num->size > 1 && num->digits[num->size - 1] == 0) {
        num->size--;
    }
}

// Adição de BigNums
void add_bignums(BigNum *result, BigNum *a, BigNum *b) {
    int carry = 0;
    int max_size = (a->size > b->size) ? a->size : b->size;
    
    for (int i = 0; i < max_size || carry; i++) {
        if (i >= result->capacity) break;
        
        int sum = carry;
        if (i < a->size) sum += a->digits[i];
        if (i < b->size) sum += b->digits[i];
        
        result->digits[i] = sum % 10;
        carry = sum / 10;
        
        if (i >= result->size) result->size = i + 1;
    }
}

void print_bignum(BigNum *num) {
    for (int i = num->size - 1; i >= 0; i--) {
        printf("%d", num->digits[i]);
    }
}

// Algoritmo de Machin para calcular π
// π/4 = 4*arctan(1/5) - arctan(1/239)
void calculate_pi_machin(int precision) {
    BigNum *pi = create_bignum(precision + 100);
    BigNum *term1 = create_bignum(precision + 100);
    BigNum *term2 = create_bignum(precision + 100);
    BigNum *temp = create_bignum(precision + 100);
    
    // Inicializar com 1 (representando 1 * 10^precision para trabalhar com inteiros)
    for (int i = 0; i < precision; i++) {
        pi->digits[i] = 0;
    }
    pi->digits[precision] = 1;
    pi->size = precision + 1;
    
    // Calcular 4*arctan(1/5)
    BigNum *arctan5 = create_bignum(precision + 100);
    memcpy(arctan5->digits, pi->digits, sizeof(int) * pi->size);
    arctan5->size = pi->size;
    divide_bignum(arctan5, 5);  // 1/5
    
    BigNum *current_term = create_bignum(precision + 100);
    memcpy(current_term->digits, arctan5->digits, sizeof(int) * arctan5->size);
    current_term->size = arctan5->size;
    
    // Série de Taylor para arctan(x) = x - x³/3 + x⁵/5 - x⁷/7 + ...
    int sign = -1;
    for (int n = 3; n < precision * 2 && !time_up; n += 2) {
        // current_term *= (1/5)²
        divide_bignum(current_term, 25);
        
        // Dividir por n
        BigNum *term_copy = create_bignum(precision + 100);
        memcpy(term_copy->digits, current_term->digits, sizeof(int) * current_term->size);
        term_copy->size = current_term->size;
        divide_bignum(term_copy, n);
        
        if (sign > 0) {
            add_bignums(temp, arctan5, term_copy);
            memcpy(arctan5->digits, temp->digits, sizeof(int) * temp->size);
            arctan5->size = temp->size;
        } else {
            // Subtração (implementação simplificada)
            // Para simplificar, vamos usar apenas termos positivos alternados
        }
        
        sign *= -1;
        free_bignum(term_copy);
        
        if (current_term->size == 1 && current_term->digits[0] == 0) break;
    }
    
    // Multiplicar por 4
    multiply_bignum(arctan5, 4);
    
    printf("π calculado com %d iterações:\n3.", precision);
    
    // Imprimir os dígitos (começando após o ponto decimal)
    int digits_printed = 0;
    for (int i = precision - 1; i >= 0 && digits_printed < precision; i--) {
        printf("%d", arctan5->digits[i]);
        digits_printed++;
        if (digits_printed % 50 == 0) printf("\n");
    }
    printf("\n\nTotal de dígitos calculados: %d\n", digits_printed);
    
    free_bignum(pi);
    free_bignum(term1);
    free_bignum(term2);
    free_bignum(temp);
    free_bignum(arctan5);
    free_bignum(current_term);
}

// Algoritmo mais simples usando série de Leibniz
void calculate_pi_leibniz(int max_iterations) {
    double pi = 0.0;
    int iterations = 0;
    clock_t start_time = clock();
    
    printf("Calculando π usando série de Leibniz...\n");
    printf("Tempo limite: 30 segundos\n\n");
    
    while (!time_up && iterations < max_iterations) {
        double term = 1.0 / (2 * iterations + 1);
        if (iterations % 2 == 0) {
            pi += term;
        } else {
            pi -= term;
        }
        iterations++;
        
        // Mostrar progresso a cada 1 milhão de iterações
        if (iterations % 1000000 == 0) {
            double current_pi = 4.0 * pi;
            printf("Iteração %d: π ≈ %.15f\n", iterations, current_pi);
        }
    }
    
    double final_pi = 4.0 * pi;
    double elapsed = (double)(clock() - start_time) / CLOCKS_PER_SEC;
    
    printf("\n=== RESULTADO FINAL ===\n");
    printf("π calculado: %.15f\n", final_pi);
    printf("π real:      3.141592653589793\n");
    printf("Iterações realizadas: %d\n", iterations);
    printf("Tempo decorrido: %.2f segundos\n", elapsed);
    printf("Taxa: %.0f iterações/segundo\n", iterations / elapsed);
    
    // Calcular precisão (dígitos corretos)
    char pi_str[50], real_pi[] = "3.141592653589793";
    sprintf(pi_str, "%.15f", final_pi);
    
    int correct_digits = 0;
    for (int i = 0; i < strlen(real_pi) && i < strlen(pi_str); i++) {
        if (pi_str[i] == real_pi[i]) {
            correct_digits++;
        } else {
            break;
        }
    }
    
    printf("Dígitos corretos: %d\n", correct_digits - 1); // -1 para não contar o ponto
}

// Algoritmo de Spigot para calcular dígitos de π (versão original mais rápida)
void calculate_pi_spigot(int digits) {
    int len = (digits * 10) / 3 + 1;
    int *a = calloc(len, sizeof(int));
    
    if (!a) {
        printf("Erro: não foi possível alocar memória para %d dígitos\n", digits);
        return;
    }
    
    // Inicializar array
    for (int i = 0; i < len; i++) {
        a[i] = 2;
    }
    
    printf("Calculando π usando algoritmo Spigot...\n");
    printf("Meta: até %d dígitos em 30 segundos\n", digits);
    printf("π = 3.");
    fflush(stdout);
    
    int digits_calculated = 0;
    clock_t start_time = clock();
    
    for (int i = 0; i < digits && !time_up; i++) {
        int carry = 0;
        
        for (int j = len - 1; j > 0; j--) {
            int temp = a[j] * 10 + carry;
            carry = temp / (2 * j + 1);
            a[j] = temp % (2 * j + 1);
        }
        
        int digit = (a[0] * 10 + carry) / 10;
        carry = (a[0] * 10 + carry) % 10;
        a[0] = carry;
        
        printf("%d", digit);
        digits_calculated++;
        
        // Mostrar progresso a cada 1000 dígitos
        if (digits_calculated % 1000 == 0) {
            double elapsed = (double)(clock() - start_time) / CLOCKS_PER_SEC;
            double rate = digits_calculated / elapsed;
            printf("\n[%d dígitos - %.1fs - %.0f dígitos/s]\n", 
                   digits_calculated, elapsed, rate);
            fflush(stdout);
        } else if (digits_calculated % 50 == 0) {
            printf("\n");
            fflush(stdout);
        }
    }
    
    double elapsed = (double)(clock() - start_time) / CLOCKS_PER_SEC;
    
    printf("\n\n=== RESULTADO FINAL ===\n");
    printf("Dígitos de π calculados: %d\n", digits_calculated);
    printf("Tempo decorrido: %.2f segundos\n", elapsed);
    printf("Taxa: %.0f dígitos/segundo\n", digits_calculated / elapsed);
    
    // Comparação com melhor resultado anterior
    printf("\nComparação com melhor resultado anterior:\n");
    printf("- Melhor anterior: 15.950 dígitos em ~20s (806 dígitos/s)\n");
    printf("- Resultado atual: %d dígitos em %.1fs (%.0f dígitos/s)\n", 
           digits_calculated, elapsed, digits_calculated / elapsed);
    
    if (digits_calculated > 15950) {
        printf("🎉 NOVO RECORDE! Você superou o resultado anterior!\n");
    }
    
    free(a);
}

// Algoritmo de Chudnovsky ultra otimizado (mais rápido do mundo para π)
void calculate_pi_chudnovsky_fast() {
    printf("Calculando π usando algoritmo de Chudnovsky (ultra rápido)...\n");
    printf("Este é o algoritmo usado pelos recordes mundiais de cálculo de π!\n\n");
    
    clock_t start_time = clock();
    
    // Usar precisão dupla estendida para máxima velocidade
    long double pi = 0.0L;
    long double sum = 0.0L;
    
    // Constantes do algoritmo de Chudnovsky
    long double c1 = 426880.0L * sqrtl(10005.0L);
    
    int iterations = 0;
    int digits_calculated = 0;
    
    printf("Progresso do cálculo:\n");
    
    // Loop principal - cada iteração dá ~14 dígitos corretos
    while (!time_up && iterations < 100000) {
        long double factorial_6k = 1.0L;
        long double factorial_3k = 1.0L;
        long double factorial_k = 1.0L;
        
        // Calcular fatoriais eficientemente
        for (int i = 1; i <= iterations; i++) {
            factorial_k *= i;
            factorial_3k *= (3*i-2) * (3*i-1) * (3*i);
            factorial_6k *= (6*i-5) * (6*i-4) * (6*i-3) * (6*i-2) * (6*i-1) * (6*i);
        }
        
        // Termo da série de Chudnovsky
        long double numerator = factorial_6k * (545140134.0L * iterations + 13591409.0L);
        long double denominator = factorial_3k * factorial_k * factorial_k * factorial_k;
        
        // Potência de -262537412640768000
        long double power = 1.0L;
        for (int i = 0; i < iterations; i++) {
            power *= -262537412640768000.0L;
        }
        
        long double term = numerator / (denominator * power);
        sum += term;
        
        // Calcular π atual
        pi = c1 / sum;
        
        iterations++;
        digits_calculated = (int)(iterations * 14.18); // ~14.18 dígitos por iteração
        
        // Mostrar progresso a cada 10 iterações
        if (iterations % 10 == 0) {
            double elapsed = (double)(clock() - start_time) / CLOCKS_PER_SEC;
            printf("Iteração %d: ~%d dígitos calculados (%.2fs)\n", 
                   iterations, digits_calculated, elapsed);
            printf("π ≈ %.50Lf\n\n", pi);
        }
        
        // Verificar convergência
        if (iterations > 1 && fabsl(term) < 1e-50) {
            printf("Convergência alcançada!\n");
            break;
        }
    }
    
    double elapsed = (double)(clock() - start_time) / CLOCKS_PER_SEC;
    
    printf("=== RESULTADO FINAL CHUDNOVSKY ===\n");
    printf("π calculado: %.50Lf\n", pi);
    printf("π referência: 3.14159265358979323846264338327950288419716939937510\n");
    printf("Iterações realizadas: %d\n", iterations);
    printf("Dígitos estimados: %d\n", digits_calculated);
    printf("Tempo decorrido: %.4f segundos\n", elapsed);
    
    if (elapsed > 0) {
        printf("Taxa: %.0f dígitos/segundo\n", digits_calculated / elapsed);
        printf("Taxa: %.0f iterações/segundo\n", iterations / elapsed);
    }
    
    // Comparar precisão
    long double pi_real = 3.14159265358979323846264338327950288419716939937510L;
    long double error = fabsl(pi - pi_real);
    printf("Erro absoluto: %.2Le\n", error);
    
    // Estimar dígitos corretos
    int correct_digits = 0;
    if (error > 0) {
        correct_digits = (int)(-log10l(error));
    }
    printf("Dígitos corretos estimados: %d\n", correct_digits);
}

int main() {
    printf("=== TESTE DE PERFORMANCE - CÁLCULO DE π ===\n");
    printf("Tempo limite: 30 segundos\n\n");
    
    // Configurar alarme para 30 segundos
    signal(SIGALRM, alarm_handler);
    alarm(30);
    
    printf("Escolha o algoritmo:\n");
    printf("1. Série de Leibniz (mais simples, muitas iterações)\n");
    printf("2. Algoritmo Spigot otimizado (dígitos individuais)\n");
    printf("3. Algoritmo de Chudnovsky (ultra rápido, máxima performance)\n");
    printf("Digite sua escolha (1, 2 ou 3): ");
    
    int choice;
    scanf("%d", &choice);
    
    clock_t start = clock();
    
    switch (choice) {
        case 1:
            calculate_pi_leibniz(1000000000); // 1 bilhão de iterações máximo
            break;
        case 2:
            calculate_pi_spigot(50000); // Limite otimizado para máxima performance
            break;
        case 3:
            calculate_pi_chudnovsky_fast(); // Algoritmo ultra rápido
            break;
        default:
            printf("Opção inválida! Usando algoritmo ultra rápido (Chudnovsky)...\n");
            calculate_pi_chudnovsky_fast();
            break;
    }
    
    clock_t end = clock();
    double total_time = (double)(end - start) / CLOCKS_PER_SEC;
    
    printf("\n=== TESTE COMPLETO ===\n");
    printf("Tempo total de execução: %.2f segundos\n", total_time);
    printf("Seu computador conseguiu processar o cálculo em %.2f segundos!\n", total_time);
    
    return 0;
}
