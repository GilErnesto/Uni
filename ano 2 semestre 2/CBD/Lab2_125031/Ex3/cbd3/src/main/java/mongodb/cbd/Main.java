package mongodb.cbd;

import com.mongodb.client.*;
import com.mongodb.client.model.Filters;
import com.mongodb.client.model.Updates;

import static com.mongodb.client.model.Filters.and;
import static com.mongodb.client.model.Filters.eq;
import static com.mongodb.client.model.Filters.gt;
import static com.mongodb.client.model.Filters.in;
import static com.mongodb.client.model.Filters.or;
import static com.mongodb.client.model.Filters.regex;
import static com.mongodb.client.model.Filters.text;

import com.mongodb.client.result.InsertManyResult;
import com.mongodb.client.result.UpdateResult;
import org.bson.Document;
import org.bson.conversions.Bson;
import com.mongodb.client.model.Indexes;
import com.mongodb.client.model.Sorts;
import java.util.*;

/* 
Link do curso de mongodb e java
https://learn.mongodb.com/courses/mongodb-crud-operations-in-java
 */

public class Main {

    static MongoCollection<Document> collection;

    public static void main(String[] args) {
        MongoClient client = MongoClients.create("mongodb://localhost:27017");
        MongoDatabase db = client.getDatabase("cbd"); 
        collection = db.getCollection("restaurants");

        criarIndices(); 
        // TESTES

        //inserir(); // insiro 2 restaurants
        System.out.println("\n\n\n");

        editar("40356018", "gastronomia", "Italian"); // restaurant_id é mais único
        System.out.println("\n\n\n");

        /*pesquisa limitada a valores exatos
        caso queira "scores > 80"; não dá */
        pesquisar("address.zipcode", "11224"); 
        System.out.println("\n\n\n");
        pesquisar("gastronomia", "Portuguese");
        System.out.println("\n\n\n");
        pesquisar("localidade", "Vila Pouca de Aguiar");
        System.out.println("\n\n\n");

        pesquisaIndice(); // vai testar a pesquisa com os indices criados

        /*
        queries da 2.2 
        cada query tem o numero da alinea
        */
       System.out.println("Queries da 2.2");
        query4();
        System.out.println("\n\n\n");
        query5();
        System.out.println("\n\n\n");
        query6();
        System.out.println("\n\n\n");
        query11();
        System.out.println("\n\n\n");
        query12();
        System.out.println("\n\n\n");

        // alinea D
        System.out.println("Numero de localidades distintas: " + countLocalidades() + "\n\n\n"); // 5+1, adicionei Vila Pouca
        
        System.out.println("Numero de restaurantes por localidade:");
        countRestByLocalidade().forEach((localidade, total)->System.out.println("-> " + localidade + " - " + total + "\n\n\n"));

        String name= "Park"; // <- mudar o nome para resultados diferentes
        System.out.println("Nome de restaurantes contendo '"+name+"' no nome:");
        getRestWithNameCloserTo(name).forEach(nome->System.out.println("-> " + nome));

        client.close();
    }

    static void inserir() {
        System.out.println("A inserir restaurantes");

        Document doc1 = new Document()
                .append("nome", "Casa Mia")
                .append("gastronomia", "Portuguese")
                .append("localidade", "Vila Pouca de Aguiar")
                .append("restaurant_id", "40356018")
                .append("address", new Document()
                        .append("building", "3")
                        .append("coord", Arrays.asList(41.499454, -7.647024))
                        .append("rua", "Avenida da Noruega")
                        .append("zipcode", "5450"))
                .append("grades", Arrays.asList(
                        new Document()
                            .append("grade", "A")
                            .append("score", 90)
                            .append("date", new Date()),
                        new Document()
                            .append("grade", "B")
                            .append("score", 75)
                            .append("date", new Date())));


        Document doc2 = new Document()
                .append("nome", "Balas - Hamburgueria Artesanal")
                .append("gastronomia", "American")
                .append("localidade", "Vila Pouca de Aguiar")
                .append("restaurant_id", "40356019")
                .append("address", new Document()
                        .append("building", "37")
                        .append("coord", Arrays.asList(41.499638, -7.644525))
                        .append("rua", "Rua Doutor António Gil")
                        .append("zipcode", "5450"))
                .append("grades", Arrays.asList(
                        new Document()
                            .append("grade", "C")
                            .append("score", 50)
                            .append("date", new Date()),
                        new Document()
                            .append("grade", "B")
                            .append("score", 60)
                            .append("date", new Date())));

        List<Document> restaurants = Arrays.asList(doc1, doc2);
        InsertManyResult result = collection.insertMany(restaurants);

        result.getInsertedIds().forEach((index, id)-> System.out.println("Restaurant adicionado: "+restaurants.get(index).getString("nome")+", com ID: "+id.asObjectId().getValue()));
    }

    
    static void pesquisar(String campo, String valor){
        System.out.println("A pesquisar restaurantes, Campo: "+campo+", Valor: "+valor);

        Object novoValor;
        try {
            novoValor = Integer.parseInt(valor); // tenta converter para int
        } catch (NumberFormatException e) {
            novoValor = valor; // se falhar, fica como String
        }

        try(MongoCursor<Document> cursor = collection.find(eq(campo, novoValor)).iterator()){
            while(cursor.hasNext()) {
                System.out.println(cursor.next().toJson());
            }
        }
    }


    static void editar(String ID, String campo, String novoValor){
        Bson query = Filters.eq("restaurant_id", ID);
        Bson updates = Updates.set(campo, novoValor);
        UpdateResult result = collection.updateOne(query, updates);

        if (result.getMatchedCount() == 0)
            System.out.println("Restaurante_id '" + ID + "' nao encontrado.");
        else
            System.out.println("Restaurante_id '" + ID + "' -> '" + campo + "' atualizado para '" + novoValor + "'");
    }

    static void criarIndices() {
        // indice localidade
        String idx1 = collection.createIndex(Indexes.ascending("localidade"));
        System.out.println("Índice criado: " + idx1);

        // indice gastronomia
        String idx2 = collection.createIndex(Indexes.ascending("gastronomia"));
        System.out.println("Índice criado: " + idx2);

        // indice de texto para nome
        String idx3 = collection.createIndex(Indexes.text("nome"));
        System.out.println("Índice criado: " + idx3);
    }

    static void pesquisaIndice() {
        System.out.println("A pesquisar restaurantes, usando Índice Localidade (Vila Pouca de Aguiar)");
        try (MongoCursor<Document> cursor = collection.find(eq("localidade", "Vila Pouca de Aguiar")).iterator()) {
            while (cursor.hasNext())
                System.out.println(cursor.next().getString("nome"));
        }

        System.out.println("A pesquisar restaurantes, usando Índice Gastronomia (Portuguese)");
        try (MongoCursor<Document> cursor = collection.find(eq("gastronomia", "Portuguese")).iterator()) {
            while (cursor.hasNext())
                System.out.println(cursor.next().getString("nome"));
        }

        System.out.println("A pesquisar restaurantes, usando Índice Texto (Riviera)");
        try (MongoCursor<Document> cursor = collection.find(text("Riviera")).iterator()) {
            while (cursor.hasNext())
                System.out.println(cursor.next().getString("nome"));
        }
    }

    static void query4(){
        System.out.println("Query 4");

        long total = collection.countDocuments(eq("localidade", "Bronx"));
        System.out.println("Total de restaurantes no Bronx: " + total);
    }

    static void query5(){
        System.out.println("Query 5");
        
        try (MongoCursor<Document> cursor = collection
                .find(eq("localidade", "Bronx"))
                .sort(Sorts.ascending("nome"))
                .limit(15)
                .iterator()) {

            while (cursor.hasNext()) {
                System.out.println(cursor.next().toJson());
            }
        }
    }

    static void query6(){
        System.out.println("Query 6");
        
        try (MongoCursor<Document> cursor = collection
                .find(gt("grades.score", 85))
                .iterator()) {

            while (cursor.hasNext()) {
                System.out.println(cursor.next().toJson());
            }
        }
    }

    static void query11(){
        System.out.println("Query 11");

        try (MongoCursor<Document> cursor = collection
            .find(and(eq("localidade", "Bronx"),
                  or(eq("gastronomia", "American"),
                  eq("gastronomia", "Chinese"))))
            .iterator()) {
            
            while (cursor.hasNext()) {
                Document doc = cursor.next();
                System.out.println(doc.getString("nome") + "; " + doc.getString("localidade") + "; " + doc.getString("gastronomia"));
            }
        }
    }

    static void query12(){
        System.out.println("Query 12");

        try (MongoCursor<Document> cursor = collection
            .find(in("localidade", "Staten Island", "Queens", "Brooklyn"))
            .iterator()) {

            while (cursor.hasNext()) {
                Document doc = cursor.next();
                System.out.println(doc.getString("nome") + " | " + doc.getString("localidade"));
            }
        }
    }

    public static int countLocalidades(){
        List<String> localidades = collection
            .distinct("localidade", String.class)
            .into(new ArrayList<>());

        return localidades.size();
    }
    
    public static Map<String, Integer> countRestByLocalidade(){
        Map<String, Integer> resultado = new HashMap<>();

        try (MongoCursor<Document> cursor = collection
            .aggregate(List.of(new Document("$group", new Document("_id", "$localidade")
                .append("total", new Document("$sum", 1)))))
            .iterator()) {

            while (cursor.hasNext()) {
                Document doc = cursor.next();
                resultado.put(doc.getString("_id"), doc.getInteger("total"));
            }
        }
        return resultado;
    }

    public static List<String> getRestWithNameCloserTo(String name){
        List<String> resultado = new ArrayList<>();

        try (MongoCursor<Document> cursor = collection
            .find(regex("nome", name, "i"))
            .iterator()) {

            while (cursor.hasNext()) {
                resultado.add(cursor.next().getString("nome"));
            }
        }
        return resultado;
    }
}