package aula02;
import java.util.Scanner;

public class Ex7 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Frase -> ");
        String frase = sc.nextLine().trim();

        String regex = "[,\\.\\s]";    //o que faz isto? 💀 
        String[] myArray = frase.split(regex); //w3schools.com/java/java_regex.asp


        String word = "";

        for(String s : myArray){
            if(s.length() > 3){
                word += s.charAt(0);
            }
        }
        System.out.println(word);
        sc.close();
    }
}
