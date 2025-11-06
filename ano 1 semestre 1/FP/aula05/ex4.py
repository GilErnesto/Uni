def obter_nomes_equipas():
    """Obtém os nomes das equipas do utilizador e retorna uma lista de equipas."""
    equipas = []
    while True:
        nome = input("Digite o nome da equipa (ou 'fim' para terminar): ")
        if nome.lower() == 'fim':
            break
        equipas.append(nome)
    return equipas

def gerar_jogos(equipas):
    """Gera uma lista com todos os jogos possíveis (pares de equipas)."""
    jogos = []
    for i in range(len(equipas)):
        for j in range(i + 1, len(equipas)):
            jogos.append((equipas[i], equipas[j]))
    return jogos

def registar_resultados(jogos):
    """Pergunta ao utilizador o resultado de cada jogo e retorna um dicionário com os resultados."""
    resultados = {}
    for jogo in jogos:
        equipa1, equipa2 = jogo
        golos1 = int(input(f"Golos marcados por {equipa1}: "))
        golos2 = int(input(f"Golos marcados por {equipa2}: "))
        resultados[jogo] = (golos1, golos2)
    return resultados

def atualizar_tabela(resultados, equipas):
    """Atualiza a tabela de classificação com base nos resultados dos jogos."""
    tabela = {equipa: [0, 0, 0, 0, 0, 0] for equipa in equipas}
    
    for (equipa1, equipa2), (golos1, golos2) in resultados.items():
        # Atualiza golos marcados e sofridos
        tabela[equipa1][3] += golos1
        tabela[equipa1][4] += golos2
        tabela[equipa2][3] += golos2
        tabela[equipa2][4] += golos1
        
        # Atualiza vitórias, empates, derrotas e pontos
        if golos1 > golos2:
            tabela[equipa1][0] += 1  # Vitórias
            tabela[equipa2][2] += 1  # Derrotas
            tabela[equipa1][5] += 3  # Pontos
        elif golos1 < golos2:
            tabela[equipa2][0] += 1  # Vitórias
            tabela[equipa1][2] += 1  # Derrotas
            tabela[equipa2][5] += 3  # Pontos
        else:
            tabela[equipa1][1] += 1  # Empates
            tabela[equipa2][1] += 1  # Empates
            tabela[equipa1][5] += 1  # Pontos
            tabela[equipa2][5] += 1  # Pontos
    
    return tabela

def apresentar_tabela(tabela):
    """Apresenta a tabela de classificação ordenada por pontos e diferença de golos."""
    print("{:<20} {:<10} {:<10} {:<10} {:<15} {:<15} {:<10}".format(
        "Equipa", "Vitórias", "Empates", "Derrotas", "G. Marcados", "G. Sofridos", "Pontos"
    ))
    for equipa, stats in sorted(tabela.items(), key=lambda item: (item[1][5], item[1][3] - item[1][4]), reverse=True):
        print("{:<20} {:<10} {:<10} {:<10} {:<15} {:<15} {:<10}".format(
            equipa, stats[0], stats[1], stats[2], stats[3], stats[4], stats[5]
        ))

def determinar_campeao(tabela):
    """Determina e retorna a equipa campeã."""
    campeao = max(tabela, key=lambda equipa: (tabela[equipa][5], tabela[equipa][3] - tabela[equipa][4]))
    return campeao

def main():
    """Função principal que organiza a execução do programa."""
    # Obter nomes das equipas
    equipas = obter_nomes_equipas()
    
    # Gerar todos os jogos possíveis
    jogos = gerar_jogos(equipas)
    
    # Registar os resultados dos jogos
    resultados = registar_resultados(jogos)
    
    # Atualizar a tabela de classificação
    tabela = atualizar_tabela(resultados, equipas)
    
    # Apresentar a tabela de classificação
    apresentar_tabela(tabela)
    
    # Determinar e apresentar a equipa campeã
    campeao = determinar_campeao(tabela)
    print(f"A equipa campeã é: {campeao}")

# O programa começa aqui
main()