package redis.ex3;

import redis.clients.jedis.Jedis;
public class SimplePost {
    public static String USERS_KEY = "users"; // Key set for users' name
        public static void main(String[] args) {
        Jedis jedis = new Jedis();

        // some users
        String[] users = { "Ana", "Pedro", "Maria", "Luis" };

        for (String user : users){
            jedis.sadd(USERS_KEY, user);
            jedis.smembers(USERS_KEY).forEach(System.out::println);
        }
        jedis.close();
    }
}