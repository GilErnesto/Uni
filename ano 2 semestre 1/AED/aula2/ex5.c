#include <stdio.h>
#include <stdlib.h>

// Display the contents of array a with n elements 
// Pre-Conditions: a != NULL and n > 0 
// Example of produced output: Array = [ 1.00, 2.00, 3.00 ] 
void DisplayArray(double* a, size_t n) {
    if (a == NULL || n == 0) {
        printf("Array = [ ]\n");
        return;
    }
    
    printf("Array = [ ");
    for (size_t i = 0; i < n; i++) {
        printf("%.2f", a[i]);
        if (i < n - 1) {
            printf(", ");
        }
    }
    printf(" ]\n");
}



// Read the number of elements, allocate the array and read its elements 
// Condition: number of elements > 0 
// Pre-Condition: size_p != NULL 
// Return NULL if memory allocation fails 
// Set *size_p to ZERO if memory allocation fails 
double* ReadArray(size_t* size_p) {
    if (size_p == NULL) {
        return NULL;
    }
    
    size_t n;
    printf("Digite o número de elementos: ");
    scanf("%zu", &n);
    
    if (n == 0) {
        *size_p = 0;
        return NULL;
    }
    
    double* array = (double*)malloc(n * sizeof(double));
    if (array == NULL) {
        *size_p = 0;
        return NULL;
    }
    
    printf("Digite os %zu elementos:\n", n);
    for (size_t i = 0; i < n; i++) {
        printf("Elemento %zu: ", i + 1);
        scanf("%lf", &array[i]);
    }
    
    *size_p = n;
    return array;
} 



// Allocate and return a new array with (size_1 + size_2) elements 
// which stores the elements of array_1 followed by the elements of array_2 
// Pre-Conditions: array_1 != NULL and array_2 != NULL 
// Pre-Conditions: size_1 > 0 and size_2 > 0 
// Return NULL if memory allocation fails 
double* Append(double* array_1, size_t size_1, double* array_2, size_t size_2) {
    if (array_1 == NULL || array_2 == NULL || size_1 == 0 || size_2 == 0) {
        return NULL;
    }
    
    size_t total_size = size_1 + size_2;
    double* result = (double*)malloc(total_size * sizeof(double));
    
    if (result == NULL) {
        return NULL;
    }
    
    // Copiar elementos do primeiro array
    for (size_t i = 0; i < size_1; i++) {
        result[i] = array_1[i];
    }
    
    // Copiar elementos do segundo array
    for (size_t i = 0; i < size_2; i++) {
        result[size_1 + i] = array_2[i];
    }
    
    return result;
} 


 
// Test example:    Array = [ 1.00, 2.00, 3.00 ] 
//                  Array = [ 4.00, 5.00, 6.00, 7.00 ] 
//                  Array = [ 1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00 ]
int main(void){
    size_t size1, size2;
    
    printf("=== Teste das Funções de Array ===\n\n");
    
    // Teste 1: Ler primeiro array
    printf("--- Lendo primeiro array ---\n");
    double* array1 = ReadArray(&size1);
    if (array1 != NULL) {
        DisplayArray(array1, size1);
    } else {
        printf("Erro ao ler o primeiro array.\n");
        return 1;
    }
    
    // Teste 2: Ler segundo array
    printf("\n--- Lendo segundo array ---\n");
    double* array2 = ReadArray(&size2);
    if (array2 != NULL) {
        DisplayArray(array2, size2);
    } else {
        printf("Erro ao ler o segundo array.\n");
        free(array1);
        return 1;
    }
    
    // Teste 3: Concatenar arrays
    printf("\n--- Array concatenado ---\n");
    double* concatenated = Append(array1, size1, array2, size2);
    if (concatenated != NULL) {
        DisplayArray(concatenated, size1 + size2);
        free(concatenated);
    } else {
        printf("Erro ao concatenar os arrays.\n");
    }
    
    // Liberar memória
    free(array1);
    free(array2);
    
    return 0;
}