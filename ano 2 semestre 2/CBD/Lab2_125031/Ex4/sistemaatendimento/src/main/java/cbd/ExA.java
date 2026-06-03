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

public class ExA {
    static MongoCollection<Document> collection;
    private static final String[] USERNAMES = {"GilA", "ValeA"};
    private static final String[] PRODUCTS = {
        "teclado_mecanico", "rato_gaming", "monitor_24", "monitor_32", "headset_usb",
        "cadeira_gaming", "disco_ssd_1tb", "pendrive_64gb", "router_wifi6", "tapete_rato",
        "produto11", "produto12", "produto13", "produto14", "produto15", "produto16", "produto17",
        "produto18", "produto19", "produto20", "produto21", "produto22", "produto23",
        "produto24", "produto25", "produto26", "produto27", "produto28", "produto29", "produto30", "produto31"
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
                for (String product : PRODUCTS) {
                    if (collection.countDocuments(new Document("username", username)) < limit) {
                        inserir(username, product);
                    } else {
                        System.out.println("\n== Limite atingido para o utilizador: " + username + " ==");
                    }
                }
            }
        }
long end = System.nanoTime();
System.out.printf("Mongo: %.3f ms\n", (end-start)/1e6);
}

    static void inserir(String username, String product) {
        Document aten= new Document("_id", new ObjectId())
                        .append("username", username)
                        .append("product", product)
                        .append("time_limit", new Date());

        InsertOneResult result= collection.insertOne(aten);
        BsonValue id= result.getInsertedId();
        System.out.println("Transação adicionada"+id);
    }
}
