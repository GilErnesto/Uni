package aula02;
import java.util.Scanner;

public class Ex1 
{
    public static void main(String[] args)
    {
        int seg, min, h;
        Scanner sc = new Scanner(System.in);
        System.out.print("Segundos? ");
        seg = sc.nextInt();
        h = seg / 3600;
        min = (seg % 3600) / 60;
        seg = seg % 60;
        System.out.println( h + ":" + min + ":" + seg );
        
        sc.close();
    }

}
