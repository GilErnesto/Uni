#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <math.h>
#include <string.h>

/* Demonstração das diferenças entre atof() e strtod() */

void demonstrar_atof_vs_strtod() {
    printf("\n=== DEMONSTRAÇÃO: atof() vs strtod() ===\n\n");
    
    // Casos de teste
    char *testes[] = {
        "123.45",      // Número válido
        "123.45abc",   // Número seguido de caracteres inválidos
        "abc123.45",   // Caracteres inválidos no início
        "",            // String vazia
        "   456.78  ", // Número com espaços
        "inf",         // Infinito
        "nan",         // Not a Number
        NULL
    };
    
    printf("%-15s %-15s %-15s %s\n", "String", "atof()", "strtod()", "Observações");
    printf("%-15s %-15s %-15s %s\n", "======", "======", "========", "===========");
    
    for (int i = 0; testes[i] != NULL; i++) {
        char *endptr;
        double atof_result, strtod_result;
        
        // Usando atof
        atof_result = atof(testes[i]);
        
        // Usando strtod
        errno = 0;
        strtod_result = strtod(testes[i], &endptr);
        
        printf("%-15s %-15.2f %-15.2f", testes[i], atof_result, strtod_result);
        
        // Análise do resultado do strtod
        if (errno != 0) {
            printf("ERRO: %s", strerror(errno));
        } else if (endptr == testes[i]) {
            printf("Nenhuma conversão");
        } else if (*endptr != '\0') {
            printf("Caracteres inválidos: '%s'", endptr);
        } else {
            printf("Conversão completa");
        }
        printf("\n");
    }
    
    printf("\nVANTAGENS do strtod():\n");
    printf("1. Detecta erros de conversão\n");
    printf("2. Informa onde a conversão parou\n");
    printf("3. Permite validação rigorosa\n");
    printf("4. Detecta overflow/underflow\n");
    printf("\nDESVANTAGENS do atof():\n");
    printf("1. Não detecta erros\n");
    printf("2. Retorna 0.0 para entradas inválidas\n");
    printf("3. Não permite validação\n");
}

int main(int argc, char *argv[])
{
    double num1, num2, resultado;
    char *endptr1, *endptr2;

    printf("=== CALCULADORA AVANÇADA ===\n");
    
    if (argc == 1) {
        demonstrar_atof_vs_strtod();
        return 0;
    }

    if(argc != 4){
        printf("Uso: %s <numero1> <operacao> <numero2>\n", argv[0]);
        printf("Operações disponíveis: +, -, x, /, p (potência)\n");  
        printf("Números podem ser inteiros ou decimais (ex: 3.14, -2.5)\n");
        printf("\nPara ver demonstração de atof vs strtod, execute sem argumentos.\n");
        return EXIT_FAILURE;
    }

    // Validação rigorosa usando strtod
    errno = 0;
    num1 = strtod(argv[1], &endptr1);
    
    if (errno == ERANGE) {
        printf("Erro: Primeiro número fora do intervalo válido!\n");
        return EXIT_FAILURE;
    }
    if (endptr1 == argv[1]) {
        printf("Erro: Primeiro argumento não é um número válido: '%s'\n", argv[1]);
        return EXIT_FAILURE;
    }
    if (*endptr1 != '\0') {
        printf("Erro: Primeiro argumento contém caracteres inválidos: '%s' (parou em: '%s')\n", 
               argv[1], endptr1);
        return EXIT_FAILURE;
    }

    errno = 0;
    num2 = strtod(argv[3], &endptr2);
    
    if (errno == ERANGE) {
        printf("Erro: Segundo número fora do intervalo válido!\n");
        return EXIT_FAILURE;
    }
    if (endptr2 == argv[3]) {
        printf("Erro: Terceiro argumento não é um número válido: '%s'\n", argv[3]);
        return EXIT_FAILURE;
    }
    if (*endptr2 != '\0') {
        printf("Erro: Terceiro argumento contém caracteres inválidos: '%s' (parou em: '%s')\n", 
               argv[3], endptr2);
        return EXIT_FAILURE;
    }

    // Validação do operador
    if (argv[2][1] != '\0') {
        printf("Erro: Operador deve ser um único caractere, recebido: '%s'\n", argv[2]);
        return EXIT_FAILURE;
    }

    switch (argv[2][0])
    {
    case '+':
        resultado = num1 + num2;
        printf("%.6g + %.6g = %.6g\n", num1, num2, resultado);
        break;
    
    case '-':
        resultado = num1 - num2;
        printf("%.6g - %.6g = %.6g\n", num1, num2, resultado);
        break;
    
    case 'x':
    case 'X':
        resultado = num1 * num2;
        printf("%.6g × %.6g = %.6g\n", num1, num2, resultado);
        break;

    case '/':
        if(num2 == 0.0){
            printf("Erro: Divisão por zero não é permitida!\n");
            return EXIT_FAILURE;
        }
        resultado = num1 / num2;
        printf("%.6g ÷ %.6g = %.6g\n", num1, num2, resultado);
        break;

    case 'p':
    case 'P':
        if(num1 == 0.0 && num2 < 0.0){
            printf("Erro: 0 elevado a potência negativa é indefinido!\n");
            return EXIT_FAILURE;
        }
        resultado = pow(num1, num2);
        printf("%.6g ^ %.6g = %.6g\n", num1, num2, resultado);
        break;

    default:
        printf("Erro: Operador inválido '%c'\n", argv[2][0]);
        printf("Operadores válidos: +, -, x (ou X), /, p (ou P)\n");
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}