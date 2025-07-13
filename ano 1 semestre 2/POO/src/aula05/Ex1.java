package aula05;
import java.util.Scanner;
import java.time.LocalDate;

public class Ex1 {

    static class DateYMD {
        public boolean validMonth(int month) {
            return month >= 1 && month <= 12;
        }

        public int monthDays(int month, int year) {
            switch (month) {
                case 1, 3, 5, 7, 8, 10, 12:
                    return 31;
                case 4, 6, 9, 11:
                    return 30;
                case 2:
                    return isLeapYear(year) ? 29 : 28;
                default:
                    return -1;
            }
        }

        public boolean isLeapYear(int year) {
            return (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
        }

        public boolean valid(int day, int month, int year) {
            return validMonth(month) && day >= 1 && day <= monthDays(month, year);
        }
    }

    public static String newDate(Scanner sc) {
        System.out.print("Enter the day: ");
        int day = sc.nextInt();
        System.out.print("Enter the month: ");
        int month = sc.nextInt();
        System.out.print("Enter the year: ");
        int year = sc.nextInt();

        DateYMD date = new DateYMD();
        return date.valid(day, month, year) ? year + "/" + month + "/" + day : "Invalid date";
    }

    public static String incrementDate(Scanner sc) {
        System.out.print("Enter the day: ");
        int day = sc.nextInt();
        System.out.print("Enter the month: ");
        int month = sc.nextInt();
        System.out.print("Enter the year: ");
        int year = sc.nextInt();

        DateYMD date = new DateYMD();
        if (date.valid(day, month, year)) {
            if (day == date.monthDays(month, year)) {
                day = 1;
                if (month == 12) {
                    month = 1;
                    year++;
                } else {
                    month++;
                }
            } else {
                day++;
            }
            return year + "/" + month + "/" + day;
        }
        return "Invalid date";
    }

    public static String decrementDate(Scanner sc) {
        System.out.print("Enter the day: ");
        int day = sc.nextInt();
        System.out.print("Enter the month: ");
        int month = sc.nextInt();
        System.out.print("Enter the year: ");
        int year = sc.nextInt();

        DateYMD date = new DateYMD();
        if (date.valid(day, month, year)) {
            if (day == 1) {
                if (month == 1) {
                    month = 12;
                    year--;
                } else {
                    month--;
                }
                day = date.monthDays(month, year);
            } else {
                day--;
            }
            return year + "/" + month + "/" + day;
        }
        return "Invalid date";
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        while (true) {
            System.out.print("\nDate operations:\n 1 - create new date\n 2 - show current date\n 3 - increment date\n 4 - decrement date\n 0 - exit\n> ");
            int option = sc.nextInt();
            
            switch(option) {
                case 1:
                    System.out.println(newDate(sc));
                    break;
                case 2:
                    System.out.println(LocalDate.now());
                    break;
                case 3:
                    System.out.println(incrementDate(sc));
                    break;
                case 4:
                    System.out.println(decrementDate(sc));
                    break;
                case 0:
                    System.out.println("Hasta la vista, BABY!");
                    sc.close();
                    return;
                default:
                    System.out.println("Invalid option. Try again.");
            }
        }
    }
}
