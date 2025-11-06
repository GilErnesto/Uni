def escrever_ficheiro(file, clubes_encontrados):
    with open(file, 'w', encoding='UTF-8') as fout:
        for clube in clubes_encontrados:
            nome, ranking, pais, score = clube[0], clube[1], clube[2], clube[3]
            fout.write(f"-------\nClube: {nome}, Ranking: {ranking}, Score: {score}\n")

def imprimir_clubes_por_pais(clubes, pais):
    clubes_encontrados = [clube for clube in clubes if clube[2] == pais]
    
    if clubes_encontrados:
        for clube in clubes_encontrados:
            nome, ranking, pais, score = clube[0], clube[1], clube[2], clube[3]
            print(f"Clube: {nome}, Ranking: {ranking}, Score: {score}")
    else:
        print(f"Nenhum clube encontrado para o país: {pais}")

    file = input("Quer adicionar a um ficheiro? (s/n): ")
    if file == 's':
        file = r'C:\Users\giler\OneDrive - Universidade de Aveiro\FP\tp12-soccer-20241217T110615Z-001\clubes.txt'
        escrever_ficheiro(file, clubes_encontrados)

def ler_ficheiro(nome_ficheiro):
    clubes = []
    with open(nome_ficheiro, 'r', encoding='UTF-8') as fin:
        for line in fin:
            data = line.strip().split(',')
            clubes.append(tuple(data))
    return clubes

def clube_mais_subiu(clubes):
    # Assumindo que a posição anterior está na quarta posição (índice 3) do tuplo
    # e a posição atual no índice 1
    clubes.sort(key=lambda x: int(x[3]) - int(x[1]), reverse=True)
    return clubes[0]

def imprimir_dados_clube(clubes, nome_clube):
    clube_encontrado = [clube for clube in clubes if clube[0] == nome_clube]
    if clube_encontrado:
        nome, ranking, pais, score = clube_encontrado[0]
        print(f"Clube: {nome}, Ranking: {ranking}, País: {pais}, Score: {score}")
    else:
        print(f"Clube {nome_clube} não encontrado.")

def ranking_medio_por_pais(clubes):
    from collections import defaultdict
    ranking_paises = defaultdict(list)

    for clube in clubes:
        pais = clube[2]
        ranking = int(clube[1])
        ranking_paises[pais].append(ranking)

    ranking_medio = {pais: sum(ranks) / len(ranks) for pais, ranks in ranking_paises.items()}
    return ranking_medio

def imprimir_ranking_medio_ordenado(clubes):
    ranking_medio = ranking_medio_por_pais(clubes)
    ranking_medio_ordenado = sorted(ranking_medio.items(), key=lambda x: x[1])
    
    for pais, media in ranking_medio_ordenado:
        print(f"País: {pais}, Ranking Médio: {media:.2f}")

def menu():
    nome_ficheiro = r'C:\Users\giler\OneDrive - Universidade de Aveiro\FP\tp12-soccer-20241217T110615Z-001\tp12-soccer\Soccer_Football_Clubs_Ranking.csv'
    clubes = ler_ficheiro(nome_ficheiro)
    
    while True:
        print('''\nMenu:
1) Imprimir clubes por país
2) Clube que mais subiu no ranking
3) Imprimir dados de um clube
4) Ranking médio por país
5) Países por ordem crescente do ranking médio
0) Terminar
Opção?''')
        opcao = input('-> ')

        if opcao == '1':
            pais = input('País: ')
            imprimir_clubes_por_pais(clubes, pais)
        elif opcao == '2':
            clube = clube_mais_subiu(clubes)
            print(f"O clube que mais subiu no ranking é: {clube[0]} com a posição {clube[1]} e score {clube[3]}")
        elif opcao == '3':
            nome_clube = input("Nome do clube: ")
            imprimir_dados_clube(clubes, nome_clube)
        elif opcao == '4':
            ranking_medio = ranking_medio_por_pais(clubes)
            for pais, media in ranking_medio.items():
                print(f"País: {pais}, Ranking Médio: {media:.2f}")
        elif opcao == '5':
            imprimir_ranking_medio_ordenado(clubes)
        elif opcao == '0':
            print('Terminar o programa.')
            break
        else:
            print('Opção inválida. Tente novamente.')

if __name__ == "__main__":
    menu()