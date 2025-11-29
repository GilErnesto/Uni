/**
 * reg-cri
 *
 * Programa de ilustração da necessidade de controlo de
 * acesso a regiões críticas, baseado numa proposta inicial
 * do Pedro Mariano.
 *
 * Sintaxe: reg-cri [opcões]
 */

#include <unistd.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <sys/wait.h>
#include <stdlib.h>
#include <stdio.h>
#include <getopt.h>
#include <libgen.h>
#include <math.h>

#include "sharedMemory.h"
#include "semaphore.h"

#define SHMKEY 0x100
#define SEMKEY 0x101
#define NPROC      4
#define BIG     1000

/* mensagem de ajuda */
#define USAGE "Sintaxe: %s [opções]\n"\
    "\t----------+--------------------------------------------\n"\
    "\t   Opção  |          Descrição                         \n"\
    "\t----------+--------------------------------------------\n"\
    "\t -i num   | lança quatro processos, cada um incrementando a variável residente em mem. part. num vezes\n"\
    "\t -c       | cria uma região de memória partilhada onde é definida uma variável\n"\
    "\t -d       | destroi a região de memória partilhada\n"\
    "\t -s num   | inicializa a variável residente em memória partilhada\n"\
    "\t -p       | imprime no 'stdout' o valor da variável\n"\
    "\t -h       | esta ajuda                                 \n"\
    "\t----------+--------------------------------------------\n"

static int set(int value);
static int iter(int value);
static int print(void);
static int create(void);
static int destroy(void);

int main (int argc, char *argv[])
{
    /* processamento da linha de comando */
    const char *optstr = "i:cds:ph";
    int option;

    do { 
        switch ((option = getopt (argc, argv, optstr)))
        { 
            case 'i': return iter (atoi (optarg));
            case 's': return set (atoi (optarg));
            case 'p': return print ();
            case 'c': return create ();
            case 'd': return destroy ();
            case 'h': printf (USAGE, basename (argv[0]));
                 return EXIT_SUCCESS;
            default: fprintf (stderr, "Opção não válida\n");
            case -1: fprintf (stderr, USAGE, basename (argv[0]));
                 return EXIT_FAILURE;
        }
    } while (option >= 0);

    return EXIT_SUCCESS;
}

void delay(int nite)
{
    int k;
    double b = 0.0;
    double c = 0.0;
    double PI = 3.141516;

    for (k = 0; k < nite; k++)
    { 
        b = cos (c + PI/4);
        c = sqrt (fabs (b));
    }
}

static int create(void)
{
    /* cria a memória partilhada, falhando se já existir */
    if (shmemCreate (SHMKEY, sizeof (long)) == -1) { 
        perror ("shmemCreate");
        return EXIT_FAILURE;
    }
    
    /* cria o semáforo para exclusão mútua */
    int semid = semCreate (SEMKEY, 1);
    if (semid == -1) { 
        perror ("semCreate");
        shmemDestroy (shmemConnect (SHMKEY));
        return EXIT_FAILURE;
    }
    
    /* inicializa o semáforo (verde - disponível) */
    if (semSignal (semid) == -1) { 
        perror ("semSignal");
        semDestroy (semid);
        shmemDestroy (shmemConnect (SHMKEY));
        return EXIT_FAILURE;
    }
    
    return EXIT_SUCCESS;
}

static int destroy(void)
{
    /* ganha acesso à memória partilhada */
    int shmid = shmemConnect (SHMKEY);
    if (shmid == -1) { 
        perror ("shmemConnect");
        return EXIT_FAILURE;
    }

    /* destroi-a */
    if (shmemDestroy (shmid) == -1) { 
        perror ("shmemDestroy");
        return EXIT_FAILURE;
    }
    
    /* ganha acesso ao semáforo */
    int semid = semConnect (SEMKEY);
    if (semid == -1) { 
        perror ("semConnect");
        return EXIT_FAILURE;
    }
    
    /* destroi o semáforo */
    if (semDestroy (semid) == -1) { 
        perror ("semDestroy");
        return EXIT_FAILURE;
    }
    
    return EXIT_SUCCESS;
}

static int iter(int niter)
{
    int i, j, auxcnt;

    /* ganha acesso à memória partilhada */
    int shmid = shmemConnect (SHMKEY);
    if (shmid == -1) { 
        perror ("shmemConnect");
        return EXIT_FAILURE;
    }

    /* anexa a memória partilhada ao espaço de endereçamento próprio */
    int *cntp;
    if (shmemAttach (shmid, (void **) &cntp) == -1) { 
        perror ("shmemAttach");
        return EXIT_FAILURE;
    }
    
    /* ganha acesso ao semáforo */
    int semid = semConnect (SEMKEY);
    if (semid == -1) { 
        perror ("semConnect");
        return EXIT_FAILURE;
    }

    /* lança processos incrementadores e espera pelo seu termo */
    for (i = 0; i < NPROC; i++)
    { 
        switch (fork ())
        { 
            case -1: perror ("fork");
                 return EXIT_FAILURE;

            case 0:  // processo incrementador
                 for (j = 0; j < niter; j++)
                 { 
                     /* entra na região crítica */
                     if (semDown (semid, 0) == -1) { 
                         perror ("semDown");
                         return EXIT_FAILURE;
                     }
                     
                     /* faz cópia do contador em mem. part. */
                     auxcnt = *cntp;

                     /* generate a time delay */
                     delay (BIG);

                     /* incrementa a cópia e armazena-a em mem. part. */
                     *cntp = auxcnt + 1;

                     /* generate a time delay */
                     delay (BIG);
                     
                     /* sai da região crítica */
                     if (semUp (semid, 0) == -1) { 
                         perror ("semUp");
                         return EXIT_FAILURE;
                     }
                 }

                 /* desanexa a memória partilhada do espaço de endereçamento próprio */
                 if (shmemDettach (cntp) == -1) { 
                     perror ("incrementador - shmemDettach");
                     return EXIT_FAILURE;
                 }

                 return EXIT_SUCCESS;
        }
    }

    /* espera pelos termo dos incrementadores e sai */
    for (i = 0; i < NPROC; i++) {
        wait(NULL);
    }
    return EXIT_SUCCESS;
}

static int set(int value)
{
    /* ganha acesso à memória partilhada */
    int shmid = shmemConnect (SHMKEY);
    if (shmid == -1)
    { 
        perror ("shmemConnect");
        return EXIT_FAILURE;
    }

    /* anexa a memória partilhada ao espaço de endereçamento próprio */
    int *cntp;
    if (shmemAttach (shmid, (void **) &cntp) == -1) { 
        perror ("shmemAttach");
        return EXIT_FAILURE;
    }

    /* inicializa o contador em memória partilhada */
    *cntp = value;

    /* desanexa a memória partilhada do espaço de endereçamento próprio */
    if (shmemDettach (cntp) == -1) { 
        perror ("incrementador - shmemDettach");
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}

static int print(void)
{
    /* ganha acesso à memória partilhada */
    int shmid = shmemConnect (SHMKEY);
    if (shmid == -1) { 
        perror ("shmemConnect");
        return EXIT_FAILURE;
    }

    /* anexa a memória partilhada ao espaço de endereçamento próprio */
    int *cntp;
    if (shmemAttach (shmid, (void **) &cntp) == -1)
    { 
        perror ("shmemAttach");
        return EXIT_FAILURE;
    }

    /* imprime valor */
    printf("Value = %d\n", *cntp);

    /* desanexa a memória partilhada do espaço de endereçamento próprio */
    if (shmemDettach (cntp) == -1)
    { 
        perror ("incrementador - shmemDettach");
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}
