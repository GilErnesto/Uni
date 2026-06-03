package cbd;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            while (true) {
                System.out.print("Escolha a alinea (A/B) ou 'stop' para sair -> ");
                String opcao = sc.nextLine().trim();

                if ("stop".equalsIgnoreCase(opcao)) {
                    System.out.println("Programa terminado.");
                    break;
                }

                if ("A".equalsIgnoreCase(opcao)) {
                    ExA.main(args);
                } else if ("B".equalsIgnoreCase(opcao)) {
                    ExB.main(args);
                } else {
                    System.out.println("Opcao invalida. Use apenas A, B ou stop.");
                }
            }
        }
    }
}