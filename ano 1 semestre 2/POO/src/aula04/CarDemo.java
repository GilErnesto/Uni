
package aula04;
import java.util.Scanner;
import java.util.regex.Pattern;

public class CarDemo {

    static Scanner sc = new Scanner(System.in);

    static boolean isValidCarData(String[] data) {
        if (data.length < 4) return false;
        if (!Pattern.matches("\\d{4}", data[2])) return false;
        if (!Pattern.matches("\\d+", data[3])) return false;
        return true;
    }

    static boolean isValidTripData(String[] data) {
        if (data.length != 2) return false;
        if (!Pattern.matches("\\d+", data[0])) return false;
        if (!Pattern.matches("\\d+", data[1])) return false;
        return true;
    }

    static int registerCars(Car[] cars) {
        int numCars = 0;
        while (true) {
            System.out.print("Insira dados do carro (marca modelo ano quilómetros): ");
            String input = sc.nextLine();
            if (input.isEmpty()) {
                break;
            }
            String[] data = input.split(" ");
            if (isValidCarData(data)) {
                String make = data[0];
                String model = String.join(" ", java.util.Arrays.copyOfRange(data, 1, data.length - 2));
                int year = Integer.parseInt(data[data.length - 2]);
                int kms = Integer.parseInt(data[data.length - 1]);
                cars[numCars++] = new Car(make, model, year, kms);
            } else {
                System.out.println("Dados mal formatados. Tente novamente.");
            }
        }
        return numCars;
    }

    static void registerTrips(Car[] cars, int numCars) {
        while (true) {
            System.out.print("Registe uma viagem no formato \"Número do carro (ordem):distância\": ");
            String input = sc.nextLine();
            if (input.isEmpty()) {
                break;
            }
            String[] data = input.split(":");
            if (isValidTripData(data)) {
                int carIndex = Integer.parseInt(data[0]);
                int distance = Integer.parseInt(data[1]);
                if (carIndex >= 0 && carIndex < numCars) {
                    cars[carIndex].drive(distance);
                    System.out.println("Carro " + carIndex + " viajou " + distance + " quilómetros.");
                } else {
                    System.out.println("Índice de carro inválido. Tente novamente.");
                }
            } else {
                System.out.println("Dados mal formatados. Tente novamente.");
            }
        }
    }

    static void listCars(Car[] cars) {
        System.out.println("\nCarros registados: ");
        for (Car car : cars) {
            if (car != null) {
                System.out.println(car);
            }
        }
        System.out.println("\n");
    }

    public static void main(String[] args) {

        Car[] cars = new Car[10];

        int numCars = registerCars(cars);

        if (numCars > 0) {
            listCars(cars);
            registerTrips(cars, numCars);
            listCars(cars);
        }

        sc.close();
    }
}