package redis.ex5;

import redis.clients.jedis.Jedis;

public class SistemaAntendimentoB {
    public static void main(String[] args) {
        final String ATENDIMENTO_KEY = "atendimento:"; // + username
        Jedis jedis = new Jedis();
    long start = System.nanoTime();

        // 30 unidades de produtos a cada 60 minutos
        int limit = 30; 
        int timeslot = 3600; 
        
        String[] users = {"GilB", "ValeB"};
        
        String[] produtos = {
            "teclado_mecanico", "rato_gaming", "monitor_24", "monitor_32", "headset_usb",
            "cadeira_gaming", "disco_ssd_1tb", "pendrive_64gb", "router_wifi6", "tapete_rato",
            "produto11", "produto12", "produto13", "produto14", "produto15",
            "produto16", "produto17", "produto18", "produto19", "produto20",
            "produto21", "produto22", "produto23", "produto24", "produto25",
            "produto26", "produto27", "produto28", "produto29", "produto30","produto31"
        };
        int[] quantidades = {2, 3, 1, 1, 5, 1, 2, 10, 1, 4, 2, 3, 1, 5, 2, 3, 1, 4, 2, 1, 5, 3, 2, 1, 4, 2, 3, 1, 2, 5, 7};

        for (String user : users) {
            String key = ATENDIMENTO_KEY + user;
            System.out.println("\n--- Processar user: " + user + " ---");

            for (int i = 0; i < produtos.length; i++) {
                /* para testar o expire
                try {
                    Thread.sleep(2000);  // 2 segundo de pausa
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
                */

                int contagem;
                if (jedis.hget(key, "contagem") != null) {
                    contagem = Integer.parseInt(jedis.hget(key, "contagem"));
                } else {
                    contagem = 0;
                }

                if (contagem + quantidades[i] <= limit) {
                    jedis.hset(key, produtos[i], String.valueOf(quantidades[i]));
                    jedis.expire(key, timeslot);
                    jedis.hincrBy(key, "contagem", quantidades[i]);
                    System.out.println("[" + user + "] Produto adicionado: " + produtos[i] + " (quantidade: " + quantidades[i] + ", total: " + (contagem + quantidades[i]) + "/" + limit + ")");

                } else {
                    System.out.println("[" + user + "] Número máximo atingido! Produto recusado: " + produtos[i] + " (quantidade: " + quantidades[i] + ", total atual: " + contagem + "/" + limit + ")");
                }
            }
        }
        jedis.close();
        long end = System.nanoTime();
        System.out.printf("Redis: %.3f ms\n", (end - start) / 1e6);
    }
}
