#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main(int argc, char *argv[])
{
    int status;
    pid_t pid;

    // Imprime linha decorativa no topo
    printf("================================================\n");

    // Cria processo filho
    pid = fork();
    
    switch (pid) {
        case -1: /* fork falhou */
            perror("Erro no fork");
            return EXIT_FAILURE;
            
        case 0:  /* processo filho */
            // Executa o comando ls -la
            if (execl("/bin/ls", "ls", "-la", NULL) < 0) {
                perror("Erro no execl");
                return EXIT_FAILURE;
            }
            break;
            
        default: /* processo pai */
            // Espera que o processo filho termine
            wait(&status);
            
            // Verifica se o filho terminou normalmente
            if (WIFEXITED(status)) {
                // Imprime linha decorativa na base
                printf("================================================\n");
            } else {
                printf("Processo filho terminou anormalmente\n");
            }
            break;
    }

    return EXIT_SUCCESS;
}