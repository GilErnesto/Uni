package redis.ex3;
import java.util.List;
import redis.clients.jedis.Jedis;

public class SimplePostList {
    public static String USERS_KEY = "users:list";
    public static void main(String[] args) {
        Jedis jedis = new Jedis();

        // some users
        String[] users = { "Ana", "Pedro", "Maria", "Luis" };
        
        for (String user : users) {
            jedis.rpush(USERS_KEY, user);
        }

        System.out.println("Users list:");
        List<String> lista = jedis.lrange(USERS_KEY, 0, -1);

        for (String user : lista) {
            System.out.println(user);
        }

        jedis.close();
    }
}
