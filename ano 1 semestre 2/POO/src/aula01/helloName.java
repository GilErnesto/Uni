package aula01;
import java.util.Scanner;

public class helloName
{
    public static  void main(String[] args)
    {
        String name;
        Scanner sc = new Scanner(System.in);
        System.out.print("Nome? ");
        name = sc.nextLine();
        System.out.println("Hello, " + name);
        sc.close();
    }
}