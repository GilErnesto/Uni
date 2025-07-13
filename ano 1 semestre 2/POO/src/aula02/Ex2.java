package aula02;
import java.util.Scanner;

public class Ex2 {
    public static void main(String[] args) 
    {
        int x1, x2, y1, y2;
        Scanner sc = new Scanner(System.in);
        System.out.print("Primeiro coordenada x? ");
        x1 = sc.nextInt();
        System.out.print("Primeiro coordenada y? ");
        y1 = sc.nextInt();
        System.out.print("Segundo coordenada x? ");
        x2 = sc.nextInt();
        System.out.print("Segundo coordenada y? ");
        y2 = sc.nextInt();
        double dist = Math.sqrt((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1));
        System.out.println("A distância é: " + dist);
        sc.close();
    }

}
