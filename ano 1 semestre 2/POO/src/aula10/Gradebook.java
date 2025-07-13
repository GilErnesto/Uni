package aula10;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class Gradebook {
    private List<Student> students = new ArrayList<>();
    public List<Student> load(String filename) {
        try {
            Path filePath = Paths.get(filename);
            File file = filePath.toFile();
            
            try (Scanner reader = new Scanner(file)) {
                while (reader.hasNextLine()) {
                    String line = reader.nextLine();
                    if (!line.isEmpty()) {
                        String[] parts = line.split("\\|");
                        String name = parts[0].trim();
                        List<Double> grades = new ArrayList<>();
                        for (int i = 1; i < parts.length; i++) {
                            grades.add(Double.parseDouble(parts[i].trim()));
                        }
                        students.add(new Student(name, grades));
                    }
                }
            }
        } catch (FileNotFoundException e) {
            System.err.println("Error: Could not find file '" + filename + "'");
        } catch (Exception e) {
            System.err.println("An unexpected error occurred while reading the file");
            e.printStackTrace();
        }
        return students;
    }
    public boolean addStudent(Student s) {
        if (s == null || s.getName().trim().isEmpty()) {
            return false;
        }

        // Verifica se já existe um aluno com o mesmo nome
        for (Student student : students) {
            if (student.getName().equalsIgnoreCase(s.getName())) {
                return false;
            }
        }

        students.add(s);
        return true;
}

    public boolean removeStudent(String name) {
        if (name == null || name.trim().isEmpty()) {
            return false;
        }
        
        return students.removeIf(student -> student.getName().equals(name));
    }
    public String getStudent(String name){
        if(name == null || name.trim().isEmpty()) {
            return null;
        } else {
            for (Student student : students) {
                if (student.getName().equalsIgnoreCase(name)) {
                    return "Student: " + student.getName() + ", Grades: " + student.getGrades();
                }
            }
        }
        return null;
    }
    public double calculateAverageGrade(String name) {
        if(name == null || name.trim().isEmpty()) {
            return 0.0;
        } else {
            for (Student student : students) {
                if (student.getName().equalsIgnoreCase(name)) {
                    List<Double> notas = student.getGrades();
                    double soma = notas.get(0) + notas.get(1) + notas.get(2);
                    double media = soma / 3;
                    return media;
                }
            }
        }
        return 0.0;
    }
    public void printAllStudents() {
        for (Student student : students) {
            System.out.println("Student: " + student.getName() + ", Grades: " + student.getGrades());
        }
    }

    public void save(String filename) {
        try {
            Path filePath = Paths.get(filename);
            File file = filePath.toFile();
            
            try (java.io.PrintWriter writer = new java.io.PrintWriter(file)) {
                for (Student student : students) {
                    writer.print(student.getName());
                    for (Double grade : student.getGrades()) {
                        writer.print("|" + grade);
                    }
                    writer.println();
                }
            }
        } catch (Exception e) {
            System.err.println("An unexpected error occurred while writing to the file");
            e.printStackTrace();
}
    }
}