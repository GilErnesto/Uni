package aula05;

import java.util.Scanner;

public class Ex2 {
    static class DateYMD {
        private int day;
        private int month;
        private int year;

        public DateYMD(int day, int month, int year) {
            this.day = day;
            this.month = month;
            this.year = year;
        }

        public int getDay() {
            return day;
        }

        public int getMonth() {
            return month;
        }

        public int getYear() {
            return year;
        }
    }

    static class Calendar {
        private int year;
        private int firstWeekdayOfYear;
        private int[][] events;

        public Calendar(int year, int firstWeekdayOfYear) {
            this.year = year;
            this.firstWeekdayOfYear = firstWeekdayOfYear;
            this.events = new int[12][];
            for (int i = 0; i < 12; i++) {
                this.events[i] = new int[getDaysInMonth(i + 1, year)];
            }
        }

        public int getYear() {
            return year;
        }

        public int getFirstWeekdayOfYear() {
            return firstWeekdayOfYear;
        }

        public int firstWeekdayOfMonth(int month) {
            int days = 0;
            for (int i = 1; i < month; i++) {
                days += getDaysInMonth(i, year);
            }
            return (firstWeekdayOfYear + days % 7) % 7;
        }

        public void addEvent(DateYMD date) {
            events[date.getMonth() - 1][date.getDay() - 1]++;
        }

        public void removeEvent(DateYMD date) {
            if (events[date.getMonth() - 1][date.getDay() - 1] > 0) {
                events[date.getMonth() - 1][date.getDay() - 1]--;
            }
        }

        public void printMonth(int month) {
            System.out.printf("%s %d\n", getMonthName(month), year);
            System.out.println("Dom Seg Ter Qua Qui Sex Sab");

            int startDay = firstWeekdayOfMonth(month);
            int daysInMonth = getDaysInMonth(month, year);

            for (int i = 0; i < startDay; i++) {
                System.out.print("    ");
            }
            for (int i = 1; i <= daysInMonth; i++) {
                if (events[month - 1][i - 1] > 0) {
                    System.out.printf("*%2d ", i);
                } else {
                    System.out.printf("%3d ", i);
                }
                if ((i + startDay) % 7 == 0) {
                    System.out.println();
                }
            }
            System.out.println();
        }

        public void printYear() {
            for (int i = 1; i <= 12; i++) {
                printMonth(i);
                System.out.println();
            }
        }

        private String getMonthName(int month) {
            String[] months = {
                "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
                "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
            };
            return months[month - 1];
        }

        private int getDaysInMonth(int month, int year) {
            if (month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12) {
                return 31;
            } else if (month == 2) {
                if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) {
                    return 29;
                } else {
                    return 28;
                }
            } else {
                return 30;
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Calendar calendar = null;

        while (true) {
            System.out.println("Calendar operations:");
            System.out.println("1 - create new calendar");
            System.out.println("2 - print calendar month");
            System.out.println("3 - print calendar");
            System.out.println("0 - exit");
            System.out.print("Choose an option: ");
            int option = sc.nextInt();

            switch (option) {
                case 1:
                    System.out.print("Enter year: ");
                    int year = sc.nextInt();
                    System.out.print("Enter first weekday of the year (1 = Sunday, 2 = Monday, ..., 7 = Saturday): ");
                    int firstWeekday = sc.nextInt();
                    calendar = new Calendar(year, firstWeekday);
                    break;
                case 2:
                    if (calendar == null) {
                        System.out.println("No calendar created.");
                    } else {
                        System.out.print("Enter month (1-12): ");
                        int month = sc.nextInt();
                        calendar.printMonth(month);
                    }
                    break;
                case 3:
                    if (calendar == null) {
                        System.out.println("No calendar created.");
                    } else {
                        calendar.printYear();
                    }
                    break;
                case 0:
                    sc.close();
                    return;
                default:
                    System.out.println("Invalid option. Try again.");
            }
        }
    }
}