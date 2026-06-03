package redis.ex3;
import redis.clients.jedis.Jedis;

public class Forum {
    public static void main(String[] args) {
        // Ensure you have redis-server running
        Jedis jedis = new Jedis();
        System.out.println(jedis.ping());
        
        jedis.set("user:1:name", "Gil");
        jedis.set("user:1:Lname", "Guedes");

        System.out.println(jedis.get("user:1:name"));
        

        jedis.close();
    }
}