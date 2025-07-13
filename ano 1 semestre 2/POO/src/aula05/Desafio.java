package aula05;

import java.time.DayOfWeek;
import java.util.Scanner;

public class Desafio {

    public static void printCalendar(int year, DayOfWeek firstDay) {
        String[] months = {
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        };
        int[] daysInMonth = {
            31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
        };

        if (isLeapYear(year)) {
            daysInMonth[1] = 29; // Fevereiro tem 29 dias em anos bissextos
        }

        int dayOfWeek = firstDay.getValue(); // De 1 (Segunda) a 7 (Domingo)

        for (int month = 0; month < 12; month++) {
            System.out.printf("\n%s %d\n", months[month], year);
            System.out.println("Mo Tu We Th Fr Sa Su");

            for (int i = 1; i < dayOfWeek; i++) {
                System.out.print("   "); // Espaço antes do primeiro dia do mês
            }

            for (int day = 1; day <= daysInMonth[month]; day++) {
                System.out.printf("%2d ", day);
                if ((day + dayOfWeek - 1) % 7 == 0) { // Quebra de linha no domingo
                    System.out.println();
                }
            }

            System.out.println();
            dayOfWeek = (dayOfWeek + daysInMonth[month]) % 7;
            if (dayOfWeek == 0) {
                dayOfWeek = 7; // Ajuste para domingo como último dia
            }
        }
    }

    public static boolean isLeapYear(int year) {
        return (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the year: ");
        int year = sc.nextInt();

        System.out.print("Enter the first day of the week (1 = Monday, ..., 7 = Sunday): ");
        int firstDay = sc.nextInt();

        if (firstDay < 1 || firstDay > 7) {
            System.out.println("Invalid input. First day must be between 1 (Monday) and 7 (Sunday).");
        } else {
            printCalendar(year, DayOfWeek.of(firstDay));
        }

        sc.close();
    }
}
