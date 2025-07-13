package aula03;  //Professor explicar este exercício

import java.util.ArrayList;
import java.util.Collection;
import java.util.Iterator;

public class Ex3 {
    public static class CollectionTester {
        public static void main(String[] args) {
            int[] dimensions = {1000, 5000, 10000, 50000, 100000};
            Collection<Integer> col = new ArrayList<>();

            System.out.printf("%-10s %-15s %-15s %-15s%n", "DIM", "Add (ms)", "Search (ms)", "Remove (ms)");
            for (int dim : dimensions) {
                checkPerformance(col, dim);
            }
        }

        private static void checkPerformance(Collection<Integer> col, int dim) {
            double start, stop, delta;

            // Add
            start = System.nanoTime(); // clock snapshot before
            for (int i = 0; i < dim; i++) {
                col.add(i);
            }
            stop = System.nanoTime(); // clock snapshot after
            delta = (stop - start) / 1e6; // convert to milliseconds
            double addTime = delta;

            // Search
            start = System.nanoTime(); // clock snapshot before
            for (int i = 0; i < dim; i++) {
                int n = (int) (Math.random() * dim);
                if (!col.contains(n)) {
                    System.out.println("Not found???" + n);
                }
            }
            stop = System.nanoTime(); // clock snapshot after
            delta = (stop - start) / 1e6; // convert nanoseconds to milliseconds
            double searchTime = delta;

            // Remove
            start = System.nanoTime(); // clock snapshot before
            Iterator<Integer> iterator = col.iterator();
            while (iterator.hasNext()) {
                iterator.next();
                iterator.remove();
            }
            stop = System.nanoTime(); // clock snapshot after
            delta = (stop - start) / 1e6; // convert nanoseconds to milliseconds
            double removeTime = delta;

            System.out.printf("%-10d %-15.2f %-15.2f %-15.2f%n", dim, addTime, searchTime, removeTime);
        }
    }
}