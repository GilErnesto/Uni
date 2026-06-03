package redis.ex3;

import redis.clients.jedis.Jedis;
import java.util.Map;

public class SimplePostHashMap {
    public static String USERS_KEY = "users:hash";

    public static void main(String[] args) {
        Jedis jedis = new Jedis();

        String[][] users = { 
            {"Ana", "Marques"}, 
            {"Pedro", "Lourenço"}, 
            {"Gil", "Guedes"}, 
            {"Luis", "Sousa"} 
        };

        for (String[] user : users) {
            jedis.hset(USERS_KEY, user[0], user[1]);
        }

        System.out.println("Users in hashmap:");
        Map<String, String> usersMap = jedis.hgetAll(USERS_KEY);

        usersMap.forEach((name, sobrenome) -> 
            System.out.println(name + ": " + sobrenome)
        );

        jedis.close();
    }
}
