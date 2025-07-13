package aula03;

import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.Scanner;

public class Ex7 {
    public static void main(String[] args) throws IOException {
        Scanner input = new Scanner(new FileReader("words.txt"));
        List<String> words = new ArrayList<>();

        // Part a) Read and list all words from the file
        while (input.hasNext()) {
            String word = input.next();
            System.out.println(word);

            // Part b) Store words longer than 2 characters
            if (word.length() > 2) {
                words.add(word);
            }
        }
        input.close();

        // Part c) List all words ending in 's'
        System.out.println("\nWords ending in 's':");
        for (String word : words) {
            if (word.endsWith("s")) {
                System.out.println(word);
            }
        }

        // Part d) Remove words containing characters other than letters
        Iterator<String> iterator = words.iterator();
        while (iterator.hasNext()) {
            String word = iterator.next();
            if (!word.matches("[a-zA-Z]+")) {
                iterator.remove();
            }
        }

        // Print the remaining words
        System.out.println("\nRemaining words:");
        for (String word : words) {
            System.out.println(word);
        }
    }
}