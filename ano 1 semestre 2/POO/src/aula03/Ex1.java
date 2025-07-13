package aula03;
import java.util.Scanner;

public class Ex1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while(true){
        System.out.println("Insira '.' para acabar o programa");
        System.out.print("Insira um número: ");
        int num = sc.nextInt();
        if(num == '.'){
            break; 
        } else if(isPrime(num)){
            System.out.println(num + " é um número primo.");
        } else {
            System.out.println(num + " não é um número primo.");
        } 
    }
    sc.close();
    }
    
    public static boolean isPrime(int n) {
        if (n < 2) return false; // Números menores que 2 não são primos
        for (int i = 2; i <= Math.sqrt(n); i++) { // Verifica divisibilidade até a raiz quadrada
            if (n % i == 0) return false;
        }
        return true; // Se não encontrou divisores, é primo
    }
}
