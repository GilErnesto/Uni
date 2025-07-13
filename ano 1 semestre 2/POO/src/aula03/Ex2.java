package aula03;
import java.util.Random;
import java.util.Scanner;

public class Ex2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Random rand = new Random();
        int number = rand.nextInt((100 + 1) - 1) + 1;
        int guess = 0;
        int attempts = 0;
        while (true){
            System.out.print("Adivinha o número entre 1 e 100: ");
            guess = sc.nextInt();
            attempts++;
            if(guess == number){
                System.out.println("Parabéns, acertaste em " + attempts + " tentativas!");
                break;
            } else if(guess < number){
                System.out.println("O número é maior!");

            } else {
                System.out.println("O número é menor!");
            }
            //if(attempts % 5 == 0){
            //    System.out.println("Queres desistir? (Y)es");
            //    if(sc.next().charAt(0) == 'Y'){
            //        System.out.println("O número era " + number);
            //        break;
            //    }
            //}
        }

        int attemptsPC = computador(number);
        
        if(attempts < attemptsPC){
            System.out.println("Ganhaste! Contra o PC!");
        } else if(attempts > attemptsPC){
            System.out.println("Perdeste! Contra o PC!");
        } else {
            System.out.println("Empate! Contra o PC!");
        }    
        
        int attemptsPC2 = computador2(number);
        if(attempts < attemptsPC2){
            System.out.println("Ganhaste! Contra o PC2!");
        } else if(attempts > attemptsPC2){
            System.out.println("Perdeste! Contra o PC2!");
        } else {
            System.out.println("Empate! Contra o PC2!");
        }    

        sc.close();
    }

    public static int computador(int number){
        int attempts = 0;
        Random rand = new Random();
        int guess = rand.nextInt((100+1) - 1) + 1;
        while(true){
            attempts++;
            if(guess == number){
                System.out.println("1111 O computador acertou em " + attempts + " tentativas!");
                break;
            } else if(guess < number){
                guess = rand.nextInt((100 + 1) - guess) + guess;
            } else {
                guess = rand.nextInt((guess + 1) - 1) + 1;
            }
        }
        return attempts;
    }

    public static int computador2(int number){
        int attempts = 0;
        int low = 1;
        int high = 100;
        int guess;
        while(true){
            attempts++;
            guess = (low + high) / 2;
            if(guess == number){
                System.out.println("2222 O computador2 acertou em " + attempts + " tentativas!");
                break;
            } else if(guess < number){
                low = guess + 1;
            } else {
                high = guess - 1;
            }
        }
        return attempts;
    }
}