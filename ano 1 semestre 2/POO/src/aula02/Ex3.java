package aula02;
import java.util.Scanner;
public class Ex3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Valor do lado a: ");
        double a = sc.nextDouble();
        System.out.print("Valor do lado b: ");
        double b = sc.nextDouble();
        Hipotenusa(a, b);
        sc.close();        
    }

    public static double Hipotenusa(double a, double b){
        double c = Math.sqrt(a*a + b*b);
        //double c = Math.hypot(a, b); //Hipotenusa
        System.out.printf("Hipotenusa: %.2f%n", c);    
        // Angulos                                                
        double angac = Math.toDegrees(Math.cos(a/c));
        double angbc = Math.toDegrees(Math.sin(b/c));
        System.out.printf("O angulo entre a e c é: %.2f%n", angac);
        System.out.printf("O angulo entre b e c é: %.2f%n", angbc);
        return 0000;
    }
}
