#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>

#define NTIMES 50

static int interrupt_count = 0;  // Contador de interrupções

static void Interrupt(int signum);

int main(void)
{
    unsigned int i;
    struct sigaction sigact;

    printf("PID = %u\n", getpid());

    /* instalar rotina de atendimento do sinal */
    sigact.sa_handler = Interrupt;
    sigemptyset(&sigact.sa_mask);
    sigact.sa_flags = 0;
    sigaction(SIGINT, &sigact, NULL);

    for (i = 0; i < NTIMES; i++) {
        printf("\r%08u ", i);
        fflush(stdout);
        sleep(1);
    }

    printf("\n");
    return EXIT_SUCCESS;
}

static void Interrupt(int signum)
{
    if (signum == SIGINT) {
        interrupt_count++;
        
        if (interrupt_count < 5) {
            printf("\nInterrupção %d/5 - Calma, ainda não cheguei a %d!\n", 
                   interrupt_count, NTIMES);
        } else {
            printf("\nQuinta interrupção! Restaurando comportamento padrão...\n");
            
            // Reinstala o handler padrão para SIGINT
            struct sigaction default_action;
            default_action.sa_handler = SIG_DFL;  // Handler padrão
            sigemptyset(&default_action.sa_mask);
            default_action.sa_flags = 0;
            sigaction(SIGINT, &default_action, NULL);
            
            printf("Próximo CTRL-C irá terminar o programa.\n");
        }
    }
}