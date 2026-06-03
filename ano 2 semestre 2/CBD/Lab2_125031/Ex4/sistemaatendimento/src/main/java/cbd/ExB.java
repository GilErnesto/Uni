package cbd;

import java.util.Date;
import java.util.concurrent.TimeUnit;

import org.bson.BsonValue;
import org.bson.Document;
import org.bson.types.ObjectId;
import com.mongodb.client.MongoClient;
import com.mongodb.client.MongoClients;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;
import com.mongodb.client.model.IndexOptions;
import com.mongodb.client.model.Indexes;
import com.mongodb.client.result.InsertOneResult;

public class ExB {
    static MongoCollection<Document> collection;
    private static final String[] USERNAMES = {"GilB", "ValeB"};
    private static final String[] PRODUCTS = {
        "teclado_mecanico", "rato_gaming", "monitor_24", "monitor_32", "headset_usb",
        "cadeira_gaming", "disco_ssd_1tb", "pendrive_64gb", "router_wifi6", "tapete_rato",
        "produto11", "produto12", "produto13", "produto14", "produto15", "produto16", "produto17",
        "produto18", "produto19", "produto20", "produto21", "produto22", "produto23",
        "produto24", "produto25", "produto26", "produto27", "produto28", "produto29", "produto30", "produto31"
    };
    public static final int[] QUANTITY = {
        2, 3, 1, 1, 5, 1, 2, 10, 1, 4, 2, 3, 1, 5, 2, 3, 1, 4, 2, 1, 5, 3, 2, 1, 4, 2, 3, 1, 2, 5, 7
    };
    
    public static void main(String[] args) {
long start = System.nanoTime();
        try (MongoClient client = MongoClients.create("mongodb://localhost:27017")) {
            MongoDatabase db = client.getDatabase("cbd");
            collection = db.getCollection("atendimento");

            long timeslot = 3600;
            int limit = 30;
            IndexOptions options = new IndexOptions().expireAfter(timeslot, TimeUnit.SECONDS);
            collection.createIndex(Indexes.ascending("time_limit"), options);

            for (String username : USERNAMES) {
                for (int i = 0; i < PRODUCTS.length; i++) {
                    int quantityInWindow = getQuantityForUser(username);
                    if (quantityInWindow + QUANTITY[i] <= limit) {
                        inserir(username, PRODUCTS[i], QUANTITY[i]);
                    } else {
                        System.out.println("\n== Limite atingido para o utilizador: " + username + " ==\n");
                    }
                }
            }
        }
long end = System.nanoTime();
System.out.printf("Mongo: %.3f ms\n", (end-start)/1e6);
}

    static void inserir(String username, String product, int quantity) {
        Document aten = new Document("_id", new ObjectId())
                        .append("username", username)
                        .append("product", product)
                        .append("quantity", quantity)
                        .append("time_limit", new Date());

        InsertOneResult result = collection.insertOne(aten);
        BsonValue id = result.getInsertedId();
        System.out.println("Transação adicionada " + id);
    }

    static int getQuantityForUser(String username) {
        Document match = new Document("$match", new Document("username", username)); // garante os limite para cada user

        Document group = new Document("$group", new Document("_id", null)
                        .append("totalQuantity", new Document("$sum", new Document("$ifNull", java.util.Arrays.asList("$quantity", 1)))));

        Document result = collection.aggregate(java.util.Arrays.asList(match, group)).first();
        if (result == null) {
            return 0;
        }

        Object total = result.get("totalQuantity");
        if (total instanceof Number) {
            return ((Number) total).intValue();
        }

        return 0;
    }
}
