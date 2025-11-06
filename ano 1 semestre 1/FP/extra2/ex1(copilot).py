# Função para validar um número de telefone
def validar_chamada(num):
    if num.startswith('+'):
        if len(num) >= 4 and num[1:].isdigit():
            return True
        else:
            return False
    elif num.isdigit() and len(num) >= 3:
        return True
    else:
        return False

# Função para registar uma chamada
def registar_chamada(chamadas):
    num_origem = input('Telefone origem? ')
    if not validar_chamada(num_origem):
        print('Número de telefone inválido.')
        return
    
    num_destino = input('Telefone destino? ')
    if not validar_chamada(num_destino):
        print('Número de telefone inválido.')
        return
    
    duracao = int(input('Duração (s)? '))
    chamadas.append((num_origem, num_destino, duracao))
    print('Chamada registrada.')

# Função para ler chamadas de um ficheiro
def ler_ficheiro(chamadas):
    ficheiro = input('Ficheiro? ')
    try:
        with open(ficheiro, 'r') as f:
            for linha in f:
                num_origem, num_destino, duracao = linha.strip().split()
                duracao = int(duracao)
                chamadas.append((num_origem, num_destino, duracao))
        print('Chamadas carregadas do ficheiro.')
    except FileNotFoundError:
        print('Ficheiro não encontrado.')

# Função para listar clientes
def listar_clientes(chamadas):
    clientes = sorted({chamada[0] for chamada in chamadas})
    print('Clientes:', ' '.join(clientes))

# Função para calcular o custo de uma chamada
def calcular_custo(destino, duracao, origem):
    if destino.startswith('2'):
        return 0.02 * (duracao / 60)
    elif destino.startswith('+'):
        return 0.80 * (duracao / 60)
    elif destino.startswith(origem[:2]):
        return 0.04 * (duracao / 60)
    else:
        return 0.10 * (duracao / 60)

# Função para gerar fatura
def gerar_fatura(chamadas):
    cliente = input('Cliente? ')
    chamadas_cliente = [chamada for chamada in chamadas if chamada[0] == cliente]
    
    if not chamadas_cliente:
        print('Nenhuma chamada encontrada para este cliente.')
        return
    
    total_custo = 0
    print(f'Fatura do cliente {cliente}')
    print('Destino             Duração      Custo')
    for chamada in chamadas_cliente:
        destino, duracao = chamada[1], chamada[2]
        custo = calcular_custo(destino, duracao, cliente)
        total_custo += custo
        print(f'{destino:<20} {duracao:<10} {custo:<10.2f}')
    
    print(f'Total:       {total_custo:.2f}')

# Função principal
def main():
    chamadas = []
    
    while True:
        print('''\n1) Registar chamada
2) Ler ficheiro
3) Listar clientes
4) Fatura
5) Terminar
Opção?''')
        opcao = input('-> ')
        
        if opcao == '1':
            registar_chamada(chamadas)
        elif opcao == '2':
            ler_ficheiro(chamadas)
        elif opcao == '3':
            listar_clientes(chamadas)
        elif opcao == '4':
            gerar_fatura(chamadas)
        elif opcao == '5':
            print('Terminar o programa.')
            break
        else:
            print('Opção inválida. Tente novamente.')

if __name__ == "__main__":
    main()