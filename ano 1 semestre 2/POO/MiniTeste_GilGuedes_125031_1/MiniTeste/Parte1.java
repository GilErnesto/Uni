package MiniTeste_GilGuedes_125031.MiniTeste;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Parte1 {
    // -----------------------------------------------------
    //          !!! Não alterar este código !!!
    // -----------------------------------------------------
    private static int v1;
    private static List<Integer> v2 = new ArrayList<>();
    private static String v3;
    private static List<String> v4 = new ArrayList<>();
    // -----------------------------------------------------

    // -----------------------------------------------------------
    // >> Pode acrescentar novos métodos aqui (não é obrigatório)
    // -----------------------------------------------------------

    // pex., public static void ler(SOURCE) {}

    // -----------------------------------------------------------

    //public static void lerTeclado(int v1, List<Integer> v2, String v3, List<String> v4) {
        // TODO: implementar a leitura aqui
        // pex., ler(teclado); -ou- o que lhe for mais conveniente

        //Scanner sc = new Scanner(System.in);
        //System.out.print("Primeiro input (v1)-> ");
        //v1 = sc.nextInt();
        //System.out.print("Segundo input (v2)-> ");
        //sc.nextLine();
        //String[] v2_2 = sc.nextLine().split(" ");
        //for (String num : v2_2) {
        //    v2.add(Integer.parseInt(num));
        //}
        //System.out.print("Terceiro input (v3)-> ");
        //v3 = sc.nextLine();
        //System.out.print("Quarto input (v4)-> ");
        //String[] v4_4 = sc.nextLine().split(" ");
        //for (String palavra : v4_4){
        //    v4.add(palavra);
        //}

        //imprimir(v1, v2, v3, v4);
        //sc.close();}

    public static void lerFicheiro() {
        try{
            Scanner scanner = new Scanner(new File("MiniTeste_GilGuedes_125031/MiniTeste/inputs.txt"));
            v1 = scanner.nextInt();
            scanner.nextLine();
            String[] v2_2 = scanner.nextLine().split(" ");
            for (String num : v2_2) {
                v2.add(Integer.parseInt(num));
            }
            v3 = scanner.nextLine();
            String[] v4_4 = scanner.nextLine().split(" ");
            for (String palavra : v4_4) {
                v4.add(palavra);
            }
            scanner.close();
            imprimir(v1, v2, v3, v4);
        } catch(FileNotFoundException e){
            System.out.print("Ficheiro nao encontrado");
        }
    }

    public static void imprimir(int v1, List<Integer> v2, String v3, List<String> v4) {
        // TODO: implementar a impressão aqui
        System.out.println(v1);
        for(Integer num : v2){
            System.out.print(num + " ");
        }
        System.out.println();
        System.out.println(v3);
        for(String palavra : v4){
            System.out.print(palavra + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        // -----------------------------------------------------------------
        // !!! Não imprimir texto a pedir determinado input, ler direto !!!
        // -----------------------------------------------------------------

        // pode editar livremente este código
        //lerTeclado(v1, v2, v3, v4);
        lerFicheiro();
        //imprimir();
    }
} 
