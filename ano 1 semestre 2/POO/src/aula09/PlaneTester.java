package aula09;

import java.util.Scanner;

public class PlaneTester {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        PlaneManager manager = new PlaneManager();
        boolean running = true;

        while (running) {
            System.out.println("\n--- MENU GESTÃO DE FROTA ---");
            System.out.println("1 - Adicionar avião comercial");
            System.out.println("2 - Adicionar avião militar");
            System.out.println("3 - Remover avião");
            System.out.println("4 - Procurar avião por ID");
            System.out.println("5 - Listar todos os aviões");
            System.out.println("6 - Listar aviões comerciais");
            System.out.println("7 - Listar aviões militares");
            System.out.println("8 - Mostrar avião mais rápido");
            System.out.println("0 - Sair");
            System.out.print("Escolha uma opção: ");
            int op = sc.nextInt();
            sc.nextLine(); // consumir \n

            switch (op) {
                case 1 -> {
                    Plane plane = criarComercial(sc);
                    manager.addPlane(plane);
                }
                case 2 -> {
                    Plane plane = criarMilitar(sc);
                    manager.addPlane(plane);
                }
                case 3 -> {
                    System.out.print("ID do avião a remover: ");
                    String id = sc.nextLine();
                    manager.removePlane(id);
                }
                case 4 -> {
                    System.out.print("ID do avião a procurar: ");
                    String id = sc.nextLine();
                    Plane found = manager.searchPlane(id);
                    System.out.println(found != null ? found : "Avião não encontrado.");
                }
                case 5 -> manager.printAllPlanes();
                case 6 -> manager.getCommercialPlanes();
                case 7 -> manager.getMilitaryPlanes();
                case 8 -> {
                    Plane fastest = manager.getFastestPlane();
                    System.out.println(fastest != null ? fastest : "Frota vazia.");
                }
                case 0 -> running = false;
                default -> System.out.println("Opção inválida.");
            }
        }

        sc.close();
    }

    private static CommercialPlane criarComercial(Scanner sc) {
        System.out.println("Adicionar avião comercial:");
        System.out.print("ID: ");
        String id = sc.nextLine();
        System.out.print("Fabricante: ");
        String fab = sc.nextLine();
        System.out.print("Modelo: ");
        String modelo = sc.nextLine();
        System.out.print("Ano de produção: ");
        int ano = sc.nextInt();
        System.out.print("Nº máximo passageiros: ");
        int maxP = sc.nextInt();
        System.out.print("Velocidade máxima: ");
        int vMax = sc.nextInt();        
        System.out.print("Nº passageiros no avião: ");
        int numP = sc.nextInt();
        sc.nextLine(); // consumir \n

        return new CommercialPlane(id, fab, modelo, ano, maxP, vMax, numP);
    }

    private static MilitaryPlane criarMilitar(Scanner sc) {
        System.out.println("Adicionar avião militar:");
        System.out.print("ID: ");
        String id = sc.nextLine();
        System.out.print("Fabricante: ");
        String fab = sc.nextLine();
        System.out.print("Modelo: ");
        String modelo = sc.nextLine();
        System.out.print("Ano de produção: ");
        int ano = sc.nextInt();
        System.out.print("Nº máximo passageiros: ");
        int maxP = sc.nextInt();
        System.out.print("Velocidade máxima: ");
        int vMax = sc.nextInt();
        System.out.print("Quantidade de munição: ");
        int muni = sc.nextInt();
        sc.nextLine(); // consumir \n

        return new MilitaryPlane(id, fab, modelo, ano, maxP, vMax, muni);
    }
}
