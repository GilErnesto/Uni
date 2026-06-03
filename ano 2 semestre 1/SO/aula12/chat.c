#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <mqueue.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>
#include <fcntl.h>

#define QUEUE_NAME "/chat_queue"
#define MAX_MSG_SIZE 256
#define MAX_MESSAGES 10

void talker(mqd_t mq) {
    char buffer[MAX_MSG_SIZE];
    
    printf("Digite suas mensagens ('sair' termina):\n");
    
    while(1) {
        printf("-> ");
        fflush(stdout);
        
        if(fgets(buffer, MAX_MSG_SIZE, stdin) == NULL) {
            break;
        }
        
        // Remove o '\n' do final
        buffer[strcspn(buffer, "\n")] = 0;
        
        // Verifica se quer sair
        if(strcmp(buffer, "sair") == 0) {
            mq_send(mq, buffer, strlen(buffer) + 1, 0);
            break;
        }
        
        // Envia mensagem para a fila
        if(mq_send(mq, buffer, strlen(buffer) + 1, 0) == -1) {
            perror("mq_send");
            break;
        }
    }
    
    printf("Talker terminando...\n");
}

void receiver(mqd_t mq) {
    char buffer[MAX_MSG_SIZE];
    ssize_t bytes_read;
    
    printf("Aguardando mensagens...\n\n");
    
    while(1) {
        // Recebe mensagem da fila
        bytes_read = mq_receive(mq, buffer, MAX_MSG_SIZE, NULL);
        
        if(bytes_read == -1) {
            perror("mq_receive");
            break;
        }
        
        buffer[bytes_read] = '\0';
        
        // Verifica se é comando de saída
        if(strcmp(buffer, "sair") == 0) {
            printf("\nReceiver terminando...\n");
            break;
        }
        
        // Imprime a mensagem recebida
        printf("Mensagem recebida: %s\n", buffer);
    }
}

int main() {
    mqd_t mq;
    struct mq_attr attr;
    pid_t pid;
    
    // Configurar atributos da fila
    attr.mq_flags = 0;
    attr.mq_maxmsg = MAX_MESSAGES;
    attr.mq_msgsize = MAX_MSG_SIZE;
    attr.mq_curmsgs = 0;
    
    // Remover fila anterior se existir
    mq_unlink(QUEUE_NAME);
    
    // Criar a fila de mensagens
    mq = mq_open(QUEUE_NAME, O_CREAT | O_RDWR, 0644, &attr);
    if(mq == (mqd_t)-1) {
        perror("mq_open");
        exit(1);
    }
    
    // Criar processo filho
    pid = fork();
    
    if(pid == -1) {
        perror("fork");
        mq_close(mq);
        mq_unlink(QUEUE_NAME);
        exit(1);
    }
    
    if(pid == 0) {
        // Processo filho - RECEIVER
        receiver(mq);
        mq_close(mq);
        exit(0);
    } else {
        // Processo pai - TALKER
        sleep(1); // Pequeno delay para o receiver iniciar
        talker(mq);
        
        // Aguardar processo filho terminar
        wait(NULL);
        
        // Limpar recursos
        mq_close(mq);
        mq_unlink(QUEUE_NAME);
    }
    
    return 0;
}
