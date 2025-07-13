package aula07;

import java.util.Scanner;

public class MainGaleria {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        //Galeria galeria = new Galeria(100);
        int opcao = 0;
        do {
            System.out.println("\nMenu:");
            System.out.println("1. Adicionar uma obra");
            System.out.println("2. Listar obras");
            System.out.println("3. Vender uma obra");
            System.out.println("4. Calcular o lucro total");
            System.out.println("5. Sair");
            System.out.print("Opçao: ");
            opcao = sc.nextInt();
            sc.nextLine();
            switch (opcao) {
                case 1:
         //           galeria.addObra();
                    break;
                case 2:
         //           galeria.listObra();
                    break;
                case 3:
          //          galeria.sellFront();
                    break;
                case 4:
          //          System.out.print(Double.toString(galeria.getLucro()));
                    break;
                case 5:
                    System.out.println("5. Sair");
                    break;
            }
        } while (opcao != 5);
        sc.close();
    }
}