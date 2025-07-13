package aula03;
import java.util.Scanner;
import java.util.ArrayList;
import java.io.File;
import java.io.FileNotFoundException;

public class Ex5 {
    public static void main(String[] args) {
        ArrayList<Student> students = new ArrayList<>();
        float totalGradeP = 0;
        float totalGradeT = 0;

        try {
            Scanner fileScanner = new Scanner(new File("src/aula03/grades.txt"));
            while (fileScanner.hasNextLine()) {
                String line = fileScanner.nextLine();
                String[] parts = line.split("\t");
                String name = parts[0];
                float gradeP = Float.parseFloat(parts[1]);
                float gradeT = Float.parseFloat(parts[2]);
                students.add(new Student(name, gradeP, gradeT));
                totalGradeP += gradeP;
                totalGradeT += gradeT;
            }
            fileScanner.close();
        } catch (FileNotFoundException e) {
            System.out.println("File not found.");
            return;
        }

        int numberOfStudents = students.size();
        float averageGradeP = totalGradeP / numberOfStudents;
        float averageGradeT = totalGradeT / numberOfStudents;

        System.out.printf("Average gradeP: %.2f%n", averageGradeP);
        System.out.printf("Average gradeT: %.2f%n", averageGradeT);

        System.out.println("\nStudents with gradeT above the overall average:");
        for (Student student : students) {
            if (student.gradeT() > averageGradeT) {
                System.out.println(student.name());
            }
        }
    }

    record Student(String name, float gradeP, float gradeT) {}
}
