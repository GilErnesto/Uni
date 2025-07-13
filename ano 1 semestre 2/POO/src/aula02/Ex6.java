package aula02;
import java.util.Scanner;

public class Ex6 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Frase -> ");
        String s = sc.nextLine();
        String frase = s.trim();
        System.out.println(countDigits(frase));
        System.out.println(countSpaces(frase));
        System.out.println(upCase(frase));
        System.out.println(removeSpace(frase));
        System.out.println(isPalindrome(frase));
        sc.close();
    }
        

        
        public static int countDigits(String frase) {
            int count = 0;
            for (int i = 0; i < frase.length(); i++) {
                if (Character.isDigit(frase.charAt(i))) {
                    count++;
                }
            }
            return count;
        }

        public static int countSpaces(String frase){
            int count = 0;
            for (int i = 0; i < frase.length(); i++) {
                if (Character.isWhitespace(frase.charAt(i))) {
                    count++;
                }
            }
            return count;
        }

        public static boolean upCase(String frase){
            for (int i = 0; i < frase.length(); i++) {
                if (Character.isLowerCase(frase.charAt(i))) {
                    return false;
                }
            }
            return true;
        }

        public static String removeSpace(String frase){
            String newFrase = "";
            boolean lastWasSpace = false;
            
            for (int i = 0; i < frase.length(); i++) {
                char c = frase.charAt(i);
                if (Character.isLetterOrDigit(c)) {
                    newFrase += c;
                    lastWasSpace = false; // O último caractere adicionado não é um espaço
                } else if (Character.isWhitespace(c) && !lastWasSpace) {
                    newFrase += ' '; // Adiciona um único espaço
                    lastWasSpace = true;
                }
            }
            return newFrase;
        }
    
    public static boolean isPalindrome(String frase){
        String newFrase = "";
        for(int i = frase.length() -1; i>=0; i--){
            char c = frase.charAt(i);
            newFrase += c;
        }
        if (frase.equals(newFrase)){
            return true;
        } else {
            return false;
        }

    }
    
    
    }

