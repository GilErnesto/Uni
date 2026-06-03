package redis.ex4;

import redis.clients.jedis.Jedis;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.List;
import java.util.Scanner;

public class Autocomplete {
    
    public static void main(String[] args) {
        final String AUTOCOMPLETE_KEY = "autocomplete:names";
        Jedis jedis = new Jedis();
        
        // mete os nomes do ficheiro no Redis
        try (BufferedReader br = new BufferedReader(new FileReader("src/main/java/redis/ex3/names.txt"))) {
            String name;
            int count = 0;
            
            System.out.println("A carregar nomes para o Redis...");
            
            while ((name = br.readLine()) != null) {
                name = name.trim().toLowerCase();
                if (!name.isEmpty()) {
                    jedis.zadd(AUTOCOMPLETE_KEY, 0, name); // cada nome tem um número
                    count++;
                }
            }
            
            System.out.println(count + " nomes carregados com sucesso!");
            
        } catch (IOException e) {
            System.err.println("Erro ao ler o ficheiro: " + e.getMessage());
        }

        // pesquisa
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println("\nSearch for ('Enter' for quit)\n");
            String input = scanner.nextLine().trim();
            
            if (input.isEmpty()) {
                break;
            }
            
            // nomes com acentos não funcionam
            String prefix = input.toLowerCase();
            String start = "[" + prefix;            // todos os nomes >= ('[') do prefixo 
            String end = "[" + prefix + (char)255;  // 255 = byte máximo
            
            List<String> results = jedis.zrangeByLex(AUTOCOMPLETE_KEY, start, end, 0, 1000); // 1000 de limite de deve ser o suficiente 🙏
            
            if (results.isEmpty()) {
                System.out.println("Nenhum resultado encontrado.\n");
            } else {
                System.out.println("Resultados:");
                for (String name : results) {
                    System.out.println("- " + name);
                }
                System.out.println();
            }
        }
        
        System.out.println("Hasta la vista, baby!");
        scanner.close();
        jedis.close();
    }
}
