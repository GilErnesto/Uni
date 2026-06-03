package redis.ex4;

import redis.clients.jedis.Jedis;
import redis.clients.jedis.resps.Tuple;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class AutocompleteCSV {
    public static void main(String[] args) {
        final String AUTOCOMPLETE_KEY_CSV = "autocomplete:names:popularity";
        Jedis jedis = new Jedis();

        try (BufferedReader br = new BufferedReader(new FileReader("src/main/java/redis/ex3/nomes-pt-2021.csv"))) {
            
            String line;
            int count = 0;
            
            System.out.println("A carregar nomes para o Redis...");
            
            while ((line = br.readLine()) != null) {
                String[] parts = line.split(";");
                if (parts.length == 2) {
                    String name = parts[0].trim().toLowerCase();
                    try {
                        int popularity = Integer.parseInt(parts[1].trim());
                        jedis.zadd(AUTOCOMPLETE_KEY_CSV, popularity, name);
                        count++;
                    } catch (NumberFormatException e) {
                        System.err.println("Erro ao processar linha: " + line);
                    }
                }
            }
            
            System.out.println(count + " nomes carregados com sucesso!");
            
        } catch (IOException e) {
            System.err.println("Erro ao ler o ficheiro: " + e.getMessage());
        }

        // pesquisa com ordenação por popularidade
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println("\nSearch for ('Enter' for quit)\n");
            String input = scanner.nextLine().trim();
            
            if (input.isEmpty()) {
                break;
            }
            
            String prefix = input.toLowerCase();
            
            // nomes ordenados por popularidade
            List<Tuple> allNames = jedis.zrevrangeWithScores(AUTOCOMPLETE_KEY_CSV, 0, -1);
            
            // filtro pelo prefixo
            List<Tuple> results = new ArrayList<>();
            for (Tuple tuple : allNames) {
                if (tuple.getElement().startsWith(prefix)) {
                    results.add(tuple);
                    if (results.size() >= 1000) {
                        break;
                    }
                }
            }
            
            if (results.isEmpty()) {
                System.out.println("  Nenhum resultado encontrado.\n");
            } else {
                System.out.println("  Resultados (ordenados por popularidade):");
                for (Tuple tuple : results) {
                    System.out.println("    - " + tuple.getElement() + " (" + (int)tuple.getScore() + " registos)");
                }
                System.out.println();
            }
        }
        
        System.out.println("Hasta la vista, baby!");
        scanner.close();
        jedis.close();
    }
}
