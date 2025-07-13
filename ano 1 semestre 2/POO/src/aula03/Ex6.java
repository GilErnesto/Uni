package aula03;
import java.util.Scanner;
import java.util.Calendar;

public class Ex6 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int[] date = readDate(sc);
        int mes = date[0];
        int ano = date[1];
        int dia = readDay(sc, mes, ano);
        printMes(dia, mes, ano);
        sc.close();
    }

    public static int[] readDate(Scanner sc) {
        int mes = 0, ano = 0;
        while (true) {
            System.out.print("Data (mm/yyyy) -> ");
            String s = sc.nextLine();
            String[] parts = s.split("/");
            try {
                mes = Integer.parseInt(parts[0]);
                ano = Integer.parseInt(parts[1]);
                if (mes >= 1 && mes <= 12 && ano > 0) {
                    break;
                } else {
                    System.out.println("Data inválida. Tente novamente.");
                }
            } catch (Exception e) {
                System.out.println("Data inválida. Tente novamente.");
            }
        }
        return new int[]{mes, ano};
    }

    public static int readDay(Scanner sc, int mes, int ano) {
        System.out.print("Quando começa o mês? (1 = Segunda, 2 = Terça, ..., 7 = Domingo, -1 = Hoje) ");
        int dia = sc.nextInt();
        if (dia == -1) {
            Calendar cal = Calendar.getInstance();
            cal.set(Calendar.MONTH, mes - 1);
            cal.set(Calendar.YEAR, ano);
            cal.set(Calendar.DAY_OF_MONTH, 1);
            dia = cal.get(Calendar.DAY_OF_WEEK);
            dia = (dia == 1) ? 7 : dia - 1; // Convert to 1 = Monday, ..., 7 = Sunday
        }
        return dia;
    }

    public static void printMes(int dia, int mes, int ano){
        System.out.printf("%-11s1/%d\n", "", mes, ano);
        System.out.println("Dom Seg Ter Qua Qui Sex Sab");

        int diasTotal = getDaysInMonth(mes, ano);
        
        int startDay = dia % 7;
        for (int i = 0; i < startDay; i++) {
            System.out.print("    ");
        }
        for (int i = 1; i <= diasTotal; i++) {
            System.out.printf("%3d ", i);
            if ((i + startDay) % 7 == 0) {
                System.out.println();
            }
        }
        System.out.println();
    }

    public static int getDaysInMonth(int mes, int ano) {
        if (mes == 1 || mes == 3 || mes == 5 || mes == 7 || mes == 8 || mes == 10 || mes == 12) {
            return 31;
        } else if (mes == 2) {
            if ((ano % 4 == 0 && ano % 100 != 0) || (ano % 400 == 0)) {
                return 29;
            } else {
                return 28;
            }
        } else {
            return 30;
        }
    }
}

