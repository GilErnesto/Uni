#include <stdio.h>
#include <stdlib.h>
#include <errno.h>

/* SUGESTÂO: utilize as páginas do manual para conhecer mais sobre as funções usadas:
 man fscanf
 man qsort
*/

#define MAX_NUMBERS 100

int compareInts(const void *px1, const void *px2)
{
    int x1 = *((int *)px1);
    int x2 = *((int *)px2);
    return(x1 < x2 ? -1 : x1 == x2 ? 0 : 1);
}

int main(int argc, char *argv[])
{
    FILE *fp = NULL;
    int numbers[MAX_NUMBERS];
    int count = 0;
    int number;
    int i;

    /* Validate number of arguments */
    if (argc != 2)
    {
        printf("USAGE: %s fileName\n", argv[0]);
        return EXIT_FAILURE;
    }

    /* Open the file */
    errno = 0;
    fp = fopen(argv[1], "r");
    if (fp == NULL)
    {
        perror("Error opening file");
        return EXIT_FAILURE;
    }

    /* Read numbers from file using fscanf() */
    while (fscanf(fp, "%d", &number) == 1 && count < MAX_NUMBERS)
    {
        numbers[count] = number;
        count++;
    }

    fclose(fp);

    /* Check if we read any numbers */
    if (count == 0)
    {
        printf("No numbers found in the file.\n");
        return EXIT_SUCCESS;
    }

    /* Sort the numbers using qsort */
    qsort(numbers, count, sizeof(int), compareInts);

    /* Print the sorted numbers */
    printf("Sorted numbers from file %s:\n", argv[1]);
    for (i = 0; i < count; i++)
    {
        printf("%d\n", numbers[i]);
    }

    return EXIT_SUCCESS;
}