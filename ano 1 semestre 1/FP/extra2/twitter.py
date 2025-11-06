import json
from collections import Counter

def main():
    # Abre o ficheiro e descodifica-o criando o objeto twits.
    with open("twitter.json", encoding="utf8") as f:
        twits = json.load(f)

    # Cria uma lista de todas as palavras mencionadas nos tweets.
    all_words = []
    for twit in twits:
        all_words.extend(twit["text"].split())

    # Conta a frequência de cada palavra.
    word_counts = Counter(all_words)

    # Ordena a lista por ordem crescente de número de vezes que a palavra é dita.
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    # Cria uma nova lista ordenada apenas com as hashtags.
    hashtags = [word for word in all_words if word.startswith("#")]
    hashtag_counts = Counter(hashtags)
    sorted_hashtags = sorted(hashtag_counts.items(), key=lambda x: x[1], reverse=True)

    # Cria um histograma normalizado a 18 colunas das hashtags mais populares.
    max_count = sorted_hashtags[0][1] if sorted_hashtags else 1
    for hashtag, count in sorted_hashtags[:10]:
        bar_length = int((count / max_count) * 18)
        print(f"{hashtag:<6} ({count:3}) {'+' * bar_length}")

if __name__ == "__main__":
    main()

