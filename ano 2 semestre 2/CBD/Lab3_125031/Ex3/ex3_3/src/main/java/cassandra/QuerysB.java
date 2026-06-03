package cassandra;

import com.datastax.oss.driver.api.core.CqlSession;
import com.datastax.oss.driver.api.core.cql.BoundStatement;
import com.datastax.oss.driver.api.core.cql.PreparedStatement;
import com.datastax.oss.driver.api.core.cql.ResultSet;
import com.datastax.oss.driver.api.core.cql.Row;

public class QuerysB {
    private static final String DEFAULT_KEYSPACE = "ex3_3";
    
    class CreateTable {
        public static void createTable(){
            System.out.println("===#===#===#===#===#===#===#===#===#===#===#===#===#===#===#===");
            System.out.println("A criar as tabelas para a alínea B");
            try (CqlSession session = CqlSession.builder().withKeyspace(DEFAULT_KEYSPACE).build()) {

                // para o Ex 4
                String createQuery1 = "CREATE TABLE IF NOT EXISTS eventos (username TEXT, videoID UUID, timeEvento TIMESTAMP, tipoEvento TEXT, videoTime INT, PRIMARY KEY (username, videoID, timeEvento)) WITH CLUSTERING ORDER BY (videoID ASC, timeEvento DESC);";
                String createIndex1 = "CREATE INDEX IF NOT EXISTS idx_eventos_tipo ON eventos(tipoEvento);";

                session.execute(createQuery1);
                session.execute(createIndex1);

                System.out.println("Tables created successfully \n");
                } catch (Exception e) {
                    e.printStackTrace();
            }
        }
    }

    class InsertData {
        public static void insertData(){
            System.out.println("===#===#===#===#===#===#===#===#===#===#===#===#===#===#===#===");
            System.out.println("A inserir dados para a alínea B");
        
            try (CqlSession session = CqlSession.builder().withKeyspace(DEFAULT_KEYSPACE).build()) {
        
                // Ex 4 - a 
                String insert1 = "INSERT INTO eventos (username, videoID, tipoEvento, timeEvento, videoTime) VALUES ('hugo',  22222222-2222-2222-2222-222222222222, 'play',  '2024-01-16 09:00:00+0000',  0);";
                String insert2 = "INSERT INTO eventos (username, videoID, tipoEvento, timeEvento, videoTime) VALUES ('hugo',  22222222-2222-2222-2222-222222222222, 'pause', '2024-01-16 09:10:00+0000',  600);";

                session.execute(insert1);
                session.execute(insert2);

                System.out.println("Data inserted successfully \n");
            } catch (Exception e) {
                    e.printStackTrace();
            }
        }
    }

    class SelectQuery {
        public static void selectQuery(){
            System.out.println("===#===#===#===#===#===#===#===#===#===#===#===#===#===#===#===");
            System.out.println("Querys de Select");
        
            try (CqlSession session = CqlSession.builder().withKeyspace(DEFAULT_KEYSPACE).build()) {
                
                // Ex 4 - a
                String select1 = "SELECT * FROM eventos WHERE username = 'hugo' AND videoID = 22222222-2222-2222-2222-222222222222 LIMIT 5;";

                ResultSet resultSet = session.execute(select1);
                boolean foundRows = false;

                for (Row row : resultSet) {
                    foundRows = true;
                    System.out.printf(
                        "username=%s | videoID=%s | tipoEvento=%s | timeEvento=%s | videoTime=%d%n",
                        row.getString("username"),
                        row.getUuid("videoid"),
                        row.getString("tipoevento"),
                        row.getInstant("timeevento"),
                        row.getInt("videotime")
                    );
                }

                if (!foundRows) {
                    System.out.println("Sem resultados para o SELECT da alínea B.");
                }

                System.out.println("\nSelects successfully \n");
            } catch (Exception e) {
                    e.printStackTrace();
            }

        }
    }
}
