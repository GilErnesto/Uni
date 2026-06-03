package redis.ex5;

import redis.clients.jedis.Jedis;

public class SistemaAntendimento {
    public static void main(String[] args) {
        final String ATENDIMENTO_KEY = "atendimento:"; // + username
        Jedis jedis = new Jedis();
    long start = System.nanoTime();

        // 30 unidades de produtos a cada 60 minutos
        int limit = 30; 
        int timeslot = 3600; 
        
        String[] users = {"GilA", "ValeA"};
        String[] pedidos_user = {
            "teclado_mecanico","rato_gaming","monitor_24","monitor_32","headset_usb",
            "cadeira_gaming","disco_ssd_1tb","pendrive_64gb","router_wifi6","tapete_rato",
            "produto11","produto12","produto13","produto14","produto15","produto16","produto17",
            "produto18","produto19","produto20","produto21","produto22","produto23",
            "produto24","produto25","produto26","produto27","produto28","produto29","produto30","produto31"
        };

        for (String user : users) {
            String key = ATENDIMENTO_KEY + user;
            System.out.println("\n--- Processar user: " + user + " ---");

            for (String pedido : pedidos_user) {
                /* para testar o expire
                try {
                    Thread.sleep(1000);  // 1 segundos de pausa
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
                */
                if (jedis.scard(key) < limit) {
                    jedis.sadd(key, pedido);
                    jedis.expire(key, timeslot);
                    System.out.println("[" + user + "] Produto adicionado, " + pedido);

                } else {
                    System.out.println("[" + user + "] Número máximo atingido! Produto recusado, " + pedido);
                }
            }
        }
        jedis.close();
    
        long end = System.nanoTime();
        System.out.printf("Redis: %.3f ms\n", (end - start) / 1e6);

    }
}
