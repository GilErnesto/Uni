#include <stdio.h>
#include <stdlib.h>
#include <errno.h>

/* SUGESTÂO: utilize as páginas do manual para conhecer mais sobre as funções usadas:
 man fopen
 man fgets
*/

#define LINEMAXSIZE 80 /* or other suitable maximum line size */

int main(int argc, char *argv[])
{
    FILE *fp = NULL;
    char line [LINEMAXSIZE]; 

    /* Validate number of arguments */
    if( argc < 2 )
    {
        printf("USAGE: %s fileName\n", argv[0]);
        return EXIT_FAILURE;
    }
    
    for(int i = 1; i < argc; i++)
    {
        /* Open file */
        errno = 0;
        fp = fopen(argv[i], "r");
        if( fp == NULL )
        {
            perror ("Error opening file");
            printf("File: %s\n", argv[i]);
            return EXIT_FAILURE;
        }

        /* Read all the lines of the file */
    while (fgets(line, sizeof(line), fp) != NULL) {
        /* fgets lê o '\n' que é o final da linha */
      printf("-> %s", line);
    }

    fclose(fp);
    }
    return EXIT_SUCCESS;
}
