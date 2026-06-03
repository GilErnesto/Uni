package cassandra;

import java.util.Scanner;

import com.datastax.oss.driver.api.core.CqlSession;
import com.datastax.oss.driver.api.core.cql.BoundStatement;
import com.datastax.oss.driver.api.core.cql.PreparedStatement;
import com.datastax.oss.protocol.internal.request.Query;


public class Main {
    private static final String DEFAULT_KEYSPACE = "ex3_3";

    public static void main(String[] args) {
        try (CqlSession session = CqlSession.builder().withKeyspace(DEFAULT_KEYSPACE).build()) {
            System.out.println("Connected to the cluster");
        } catch (Exception e) {
            e.printStackTrace();
        }

        CreateTable.createTable();

        System.out.println("Todos as querys serão na tabela users");
        System.out.println("Formato: id INT, name TEXT, email TEXT");
        try (Scanner sc = new Scanner(System.in)) {
            while (true) {
                System.out.println("===#===#===#===");
                System.out.println("1 -> Inserir");
                System.out.println("2 -> Editar");
                System.out.println("3 -> Pesquisar");
                System.out.println("4 -> Querys da alínea B");
                System.out.println("===#===#===#===");

                System.out.print("Escolha um número -> ");
                String escolhaInput = sc.nextLine().trim();
                if (escolhaInput.isEmpty()) {
                    System.out.println("\nEscolha uma opção válida");
                    continue;
                }

                int escolha;
                try {
                    escolha = Integer.parseInt(escolhaInput);
                } catch (NumberFormatException e) {
                    System.out.println("\nEscolha uma opção válida");
                    continue;
                }

                switch (escolha) {
                    case 1:
                        System.out.print("\nId -> ");
                        String id1Input = sc.nextLine().trim();
                        int id_1;
                        try {
                            id_1 = Integer.parseInt(id1Input);
                        } catch (NumberFormatException e) {
                            System.out.println("\nId inválido");
                            break;
                        }

                        System.out.print("Name -> ");
                        String name_1 = sc.nextLine();
                        System.out.print("Email -> ");
                        String email_1 = sc.nextLine();

                        InsertTable.insertTable(id_1, name_1, email_1);
                        break;

                    case 2:
                        System.out.print("\nQue id quer editar? -> ");
                        String id2Input = sc.nextLine().trim();
                        int id_2;
                        try {
                            id_2 = Integer.parseInt(id2Input);
                        } catch (NumberFormatException e) {
                            System.out.println("\nId inválido");
                            break;
                        }

                        System.out.print("Novo nome -> ");
                        String name_2 = sc.nextLine();

                        UpdateTable.updateTable(id_2, name_2);
                        break;

                    case 3:
                        System.out.print("\nSe quiser mostrar todos os dados use '*'\n");
                        System.out.print("Que id quer pesquisar? -> ");
                        String id_3 = sc.nextLine().trim();
                        if (id_3.isEmpty()) {
                            System.out.println("\nId inválido");
                            break;
                        }

                        SelectTable.selectTable(id_3);
                        break;

                    case 4:
                        QuerysB.CreateTable.createTable();
                        QuerysB.InsertData.insertData();
                        QuerysB.SelectQuery.selectQuery();
                        break;

                    default:
                        System.out.println("\nEscolha uma opcão válida");
                        break;
                }
            }
        }
    }

    class CreateTable {
        public static void createTable(){
            try (CqlSession session = CqlSession.builder().withKeyspace(DEFAULT_KEYSPACE).build()) {
                String createQuery = "CREATE TABLE IF NOT EXISTS users(id INT, name TEXT, email TEXT, PRIMARY KEY(id));";

                session.execute(createQuery);
                System.out.println("Table created successfully \n");
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        }

    class InsertTable { 
        public static void insertTable(int id, String name, String email) {
            try (CqlSession session = CqlSession.builder().withKeyspace(DEFAULT_KEYSPACE).build()) {
                String insertQuery = "INSERT INTO users(id, name, email) VALUES (?, ?, ?);";

                PreparedStatement preparedStatement = session.prepare(insertQuery);
                BoundStatement boundStatement = preparedStatement.bind(id, name, email);

                session.execute(boundStatement);
                System.out.println("Data inserted successfully \n");
                } catch (Exception e) {
                    e.printStackTrace();
            }
        }
    }

    class UpdateTable {
        public static void updateTable (int id, String name){
            try (CqlSession session = CqlSession.builder().withKeyspace(DEFAULT_KEYSPACE).build()) {
                String updateQuery = "UPDATE users SET name = ? WHERE id = ?;";

                PreparedStatement preparedStatement = session.prepare(updateQuery);
                BoundStatement boundStatement = preparedStatement.bind(name, id);

                session.execute(boundStatement);
                System.out.println("Table updated successfully \n");
                } catch (Exception e) {
                    e.printStackTrace();
            }
        }
    }

    class SelectTable {
        public static void selectTable (String id_Select){
            try (CqlSession session = CqlSession.builder().withKeyspace(DEFAULT_KEYSPACE).build()) {
                if ("*".equals(id_Select)) {
                    String selectQuery = "SELECT * FROM users";
                    session.execute(selectQuery);
                } else {
                    int id = Integer.parseInt(id_Select);
                    String selectQuery = "SELECT * FROM users WHERE id = ?;";

                    PreparedStatement preparedStatement = session.prepare(selectQuery);
                    BoundStatement boundStatement = preparedStatement.bind(id);

                    session.execute(boundStatement);
                }
                System.out.println("Table select successfully \n");
                } catch (Exception e) {
                    e.printStackTrace();
            }

        }
    }
}

