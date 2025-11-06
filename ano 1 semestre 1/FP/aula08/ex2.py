def main():
    nomes = {}
    caminho_arquivo = r'C:\Users\giler\OneDrive - Universidade de Aveiro\FP\aula08\names.txt'
    
    # Abrir o ficheiro para leitura
    with open(caminho_arquivo, 'r') as fin:
        for line in fin:
            # Remover espaços em branco nas extremidades e dividir a linha em palavras
            Nome = line.strip().split()
            
            # Continuar se a linha estiver vazia
            if not Nome:
                continue
            
            # O último nome é a última palavra da linha
            ultimo_nome = Nome[-1]
            
            # O primeiro nome é todas as palavras exceto a última
            primeiro_nome = " ".join(Nome[:-1])
            
            # Adicionar o primeiro nome ao conjunto associado ao último nome
            if ultimo_nome in nomes:
                nomes[ultimo_nome].add(primeiro_nome)
            else:
                nomes[ultimo_nome] = {primeiro_nome}
    
    # Imprimir o dicionário de nomes
    for key in nomes:
        print(f"{key}: {', '.join(nomes[key])}")

if __name__ == "__main__":
    main()