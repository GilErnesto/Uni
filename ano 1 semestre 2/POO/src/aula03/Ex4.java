package aula03;
import java.util.Scanner;
import java.util.ArrayList;
import java.io.File;
import java.io.FileNotFoundException;

public class Ex4 {
    public static void main(String[] args) {
        ArrayList<float[]> grades = new ArrayList<>();
        try {
            Scanner fileScanner = new Scanner(new File(".txt")); //Falta o documento
            while (fileScanner.hasNextLine()) {
                String line = fileScanner.nextLine();
                String[] parts = line.split("\t");
                float gradeT = Float.parseFloat(parts[0]);
                float gradeP = Float.parseFloat(parts[1]);
                grades.add(new float[]{gradeT, gradeP});
            }
            fileScanner.close();
        } catch (FileNotFoundException e) {
            System.out.println("File not found.");
            return;
        }

        System.out.printf("%-10s %-15s %-15s%n", "gradeT", "gradeP", "finalGrade");
        for (float[] grade : grades) {
            float gradeT = grade[0];
            float gradeP = grade[1];
            float finalGrade = calculateFinalGrade(gradeT, gradeP);
            System.out.printf("%-10.1f %-15.1f %-15.1f%n", gradeT, gradeP, finalGrade);
        }

        System.out.println("\nStudents who passed:");
        for (float[] grade : grades) {
            float gradeT = grade[0];
            float gradeP = grade[1];
            float finalGrade = calculateFinalGrade(gradeT, gradeP);
            if (finalGrade != 66) {
                System.out.printf("gradeT: %-10.1f gradeP: %-10.1f finalGrade: %-10.1f%n", gradeT, gradeP, finalGrade);
            }
        }
    }

    public static float calculateFinalGrade(float gradeT, float gradeP) {
        if (gradeT < 7.0 || gradeP < 7.0) {
            return 66;
        }
        return Math.round(0.4 * gradeT + 0.6 * gradeP);
    }
}