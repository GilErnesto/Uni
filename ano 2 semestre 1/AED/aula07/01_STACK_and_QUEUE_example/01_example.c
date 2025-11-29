//
// TO DO : desenvolva um algoritmo para verificar se um numero inteiro positivo
//         e uma capicua
//         Exemplos: 12321 e uma capiacua, mas 123456 nao e
//         USE uma PILHA DE INTEIROS (STACK) e uma FILA DE INTEIROS (QUEUE)
//
// TO DO : design an algorithm to check if the digits of a positive decimal
//         integer number constitue a palindrome
//         Examples: 12321 is a palindrome, but 123456 is not
//         USE a STACK of integers and a QUEUE of integers
//

#include <stdio.h>

#include "IntegersQueue.h"
#include "IntegersStack.h"

int main(void) {
    int number;
    int temp;
    int digit;
    int digitCount = 0;
    
    printf("Digite um número inteiro positivo: ");
    if (scanf("%d", &number) != 1 || number <= 0) {
        printf("Erro: Por favor, digite um número inteiro positivo válido.\n");
        return 1;
    }
    
    temp = number;
    while (temp > 0) {
        digitCount++;
        temp /= 10;
    }
    
    Stack* stack = StackCreate(digitCount);
    Queue* queue = QueueCreate(digitCount);
    
    if (stack == NULL || queue == NULL) {
        printf("Erro: Falha na criação das estruturas de dados.\n");
        if (stack != NULL) StackDestroy(&stack);
        if (queue != NULL) QueueDestroy(&queue);
        return 1;
    }
    
    temp = number;
    while (temp > 0) {
        digit = temp % 10;
        StackPush(stack, digit);
        QueueEnqueue(queue, digit);
        temp /= 10;
    }
 
    int isCapicua = 1; 
    
    while (!StackIsEmpty(stack) && !QueueIsEmpty(queue)) {
        int stackDigit = StackPop(stack);
        int queueDigit = QueueDequeue(queue);
        
        if (stackDigit != queueDigit) {
            isCapicua = 0;
            break;
        }
    }
    
    if (isCapicua) {
        printf("O número %d É uma capicua!\n", number);
    } else {
        printf("O número %d NÃO é uma capicua.\n", number);
    }
    
    StackDestroy(&stack);
    QueueDestroy(&queue);
    
    return 0;
}
