package aula09;

import java.util.Set;
import java.util.TreeSet;
import java.time.LocalDate;

public class TreeSetDemo {
    public static void main(String[] args) {
        Set<LocalDate> c4 = new TreeSet<>();

        c4.add(LocalDate.of(2024, 12, 25)); 
        c4.add(LocalDate.of(2024, 1, 1));  
        c4.add(LocalDate.of(2024, 6, 15));   
        c4.add(LocalDate.of(2024, 3, 21));   
        c4.add(LocalDate.of(2024, 10, 31));  

        System.out.println("Dates in TreeSet (automatically sorted):");
        for (LocalDate date : c4) {
            System.out.println(date);
        }
    }
}