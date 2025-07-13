package aula02;
import java.util.Scanner;
public class Ex5 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Frase: ");
        String s = sc.nextLine();
        String frase = s.trim(); //remove espaços em branco no início e no fim
        System.out.println(frase.toLowerCase()); //minuscúlas
        System.out.println(frase.substring(frase.length() - 1)); //último caractere
        System.out.println(frase.substring(frase.length()-3, frase.length())); //últimos 3 caracteres
        //outros métodos
        System.out.println(frase.charAt(frase.length()-1)); //último caractere forma diferente
        System.out.println(frase.toUpperCase()); //maiuscúlas
        String frase2 = frase.replace('a', 'e'); //substitui a por e
        System.out.println(frase2);
        System.out.println(frase.endsWith("a")); //verifica se termina com a
        System.out.println(frase.startsWith("a")); //verifica se começa com a
        System.out.println(frase.contains("a")); //verifica se contém a
        System.out.println(frase.indexOf("a")); //retorna a posição da primeira ocorrência de a
        System.out.println(frase.lastIndexOf("a")); //retorna a posição da última ocorrência de a



        sc.close();
    }
}
