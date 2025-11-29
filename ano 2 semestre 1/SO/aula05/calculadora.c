#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <math.h>

int main(int argc, char *argv[])
{
    double num1, num2, resultado;
    char *endptr1, *endptr2;

    if(argc != 4){
        printf("Uso: %s <numero1> <operacao> <numero2>\n", argv[0]);
        printf("Operações disponíveis: +, -, x, /, p (potência)\n");
        printf("Números podem ser inteiros ou decimais (ex: 3.14, -2.5)\n");
        return EXIT_FAILURE;
    }

    errno = 0;
    num1 = strtod(argv[1], &endptr1);
    num2 = strtod(argv[3], &endptr2);

    if (errno || endptr1 == argv[1] || *endptr1 || endptr2 == argv[3] || *endptr2) {
        printf("Erro: argumento inválido!\n");
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
        resultado = num1 * num2;
        printf("%.6g x %.6g = %.6g\n", num1, num2, resultado);
        break;

    case '/':
        if(num2 == 0.0){
            printf("Erro: Divisão por zero não é permitida!\n");
            return EXIT_FAILURE;
        }
        resultado = num1 / num2;
        printf("%.6g / %.6g = %.6g\n", num1, num2, resultado);
        break;

    case 'p':
        if(num2 < 0 && num1 == 0.0){
            printf("Erro: 0 elevado a potência negativa é indefinido!\n");
            return EXIT_FAILURE;
        }
        resultado = pow(num1, num2);
        printf("%.6g ^ %.6g = %.6g\n", num1, num2, resultado);
        break;

    default:
        printf("Operação inválida: %s\n", argv[2]);
        printf("Operações disponíveis: +, -, x, /, p (potência)\n");
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}
