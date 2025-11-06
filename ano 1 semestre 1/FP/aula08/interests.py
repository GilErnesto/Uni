def main():
    A = "reading"
    B = "eating"
    C = "traveling"
    D = "writing"
    E = "running"
    F = "music"
    G = "movies"
    H = "programming"

    interests = {
        "Marco": {A, D, E, F},
        "Anna": {E, A, G},
        "Maria": {G, D, E},
        "Paolo": {B, D, F},
        "Frank": {D, B, E, F, A},
        "Teresa": {F, H, C, D}
    }

    print("a) Table of common interests:")
    commoninterests = {}
    # Iterar sobre cada par de pessoas
    for key1 in interests:
        for key2 in interests:
            if key1 != key2:
                common = interests[key1].intersection(interests[key2]) #Pode se usar '&' no lugar de intersection
                if common:
                    # Ordenar as chaves para evitar duplicação de pares (key1, key2) e (key2, key1)
                    pair = tuple(sorted((key1, key2)))
                    if pair in commoninterests:
                        commoninterests[pair].update(common)
                    else:
                        commoninterests[pair] = common
                
    for line in commoninterests:
        print(line, commoninterests[line])

    print("b) Maximum number of common interests:")

    max_pair = max(commoninterests.items(), key=lambda item: len(item[1]))
    print(f"\nPar com o maior número de interesses em comum: {max_pair[0]} com {len(max_pair[1])} interesses comuns: {max_pair[1]}")


    interest_count = {}
    for person, inter in interests.items():
        for interest in inter:
            if interest in interest_count:
                interest_count[interest] += 1
            else:
                interest_count[interest] = 1

    most_common_interest = max(interest_count.items(), key=lambda item: item[1])
    print(f"\nInteresse mais comum: {most_common_interest[0]} com {most_common_interest[1]} ocorrências\n")

    print("c) Pairs with maximum number of matching interests:")
    maxmatches = ...
    print(maxmatches)

    print("d) Pairs with low similarity:")
    lowJaccard = ...
    print(lowJaccard)


# Start program:
main()

