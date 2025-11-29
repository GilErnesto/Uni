#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>

#define MAX_PEOPLE 100

typedef struct
{
    int age;
    double height;
    char name[64];
} Person;

void printPersonInfo(Person *p)
{
    printf("Person: %s, %d, %f\n", p->name, p->age, p->height);
}

int main (int argc, char *argv[])
{
    FILE *fp = NULL;
    Person people[MAX_PEOPLE];
    int totalPeople = 0;
    int newPeople = 0;
    int i;
    char option;

    /* Validate number of arguments */
    if(argc != 2)
    {
        printf("USAGE: %s fileName\n", argv[0]);
        return EXIT_FAILURE;
    }

    /* Try to open the file for reading */
    errno = 0;
    fp = fopen(argv[1], "rb");
    if(fp != NULL)
    {
        /* Read existing people from file to array */
        while(fread(&people[totalPeople], sizeof(Person), 1, fp) == 1 && totalPeople < MAX_PEOPLE)
        {
            totalPeople++;
        }
        fclose(fp);
        
        printf("Ficheiro encontrado com %d pessoa(s) existente(s):\n", totalPeople);
        printf("--- PESSOAS EXISTENTES ---\n");
        for(i = 0; i < totalPeople; i++)
        {
            printf("%d. ", i + 1);
            printPersonInfo(&people[i]);
        }
    }
    else
    {
        printf("Ficheiro não encontrado. Será criado um novo ficheiro.\n");
        totalPeople = 0;
    }

    /* Ask if user wants to add more people */
    printf("\nDeseja adicionar mais pessoas? (s/n): ");
    if(scanf(" %c", &option) != 1)
    {
        printf("Erro ao ler opção!\n");
        return EXIT_FAILURE;
    }

    if(option == 's' || option == 'S')
    {
        /* Ask for number of new people to add */
        printf("Quantas pessoas pretende adicionar? ");
        if(scanf("%d", &newPeople) != 1 || newPeople <= 0)
        {
            printf("Erro: Número de pessoas inválido!\n");
            return EXIT_FAILURE;
        }

        /* Check if we don't exceed maximum */
        if(totalPeople + newPeople > MAX_PEOPLE)
        {
            printf("Erro: Não é possível adicionar %d pessoas. Máximo permitido: %d (já existem %d)\n", 
                   newPeople, MAX_PEOPLE - totalPeople, totalPeople);
            return EXIT_FAILURE;
        }

        /* Read information for new people */
        for(i = 0; i < newPeople; i++)
        {
            printf("\n--- Nova Pessoa %d ---\n", i + 1);
            
            printf("Nome: ");
            if(scanf("%63s", people[totalPeople + i].name) != 1)
            {
                printf("Erro ao ler o nome!\n");
                return EXIT_FAILURE;
            }
            
            printf("Idade: ");
            if(scanf("%d", &people[totalPeople + i].age) != 1)
            {
                printf("Erro ao ler a idade!\n");
                return EXIT_FAILURE;
            }
            
            printf("Altura (em metros): ");
            if(scanf("%lf", &people[totalPeople + i].height) != 1)
            {
                printf("Erro ao ler a altura!\n");
                return EXIT_FAILURE;
            }
            
            printf("Pessoa adicionada: %s, %d anos, %.2f m\n", 
                   people[totalPeople + i].name, 
                   people[totalPeople + i].age, 
                   people[totalPeople + i].height);
        }

        totalPeople += newPeople;

        /* Write all people (existing + new) back to file */
        errno = 0;
        fp = fopen(argv[1], "wb");
        if(fp == NULL)
        {
            perror("Erro ao abrir ficheiro para escrita!");
            return EXIT_FAILURE;
        }

        for(i = 0; i < totalPeople; i++)
        {
            if(fwrite(&people[i], sizeof(Person), 1, fp) != 1)
            {
                printf("Erro ao escrever pessoa %d no ficheiro!\n", i + 1);
                fclose(fp);
                return EXIT_FAILURE;
            }
        }

        fclose(fp);
        printf("\nFicheiro atualizado com sucesso! Total de pessoas: %d\n", totalPeople);
    }

    /* Display final list of all people */
    printf("\n--- LISTA FINAL DE TODAS AS PESSOAS ---\n");
    for(i = 0; i < totalPeople; i++)
    {
        printf("%d. ", i + 1);
        printPersonInfo(&people[i]);
    }

    return EXIT_SUCCESS;
}