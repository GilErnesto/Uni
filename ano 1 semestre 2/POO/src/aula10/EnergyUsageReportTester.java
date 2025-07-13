package aula10;
import java.util.Arrays;

public class EnergyUsageReportTester {
    public static void main(String[] args) {
            // Create an instance of the EnergyUsageReport class
            EnergyUsageReport energyReport = new EnergyUsageReport();
            
            // Load the customer data from a text file using the load() method
            energyReport.load("C:\\--PASTA DAS PASTAS--\\Programação\\Poo2425\\src\\aula10\\clients.txt");
            
            // Add one or more customers to the collection using the addCustomer() method
            Customer newCustomer = new Customer(999, Arrays.asList(1500.0, 2000.0, 2500.0, 3000.0));
            energyReport.addCustomer(newCustomer);
            System.out.println("Utilizador adicionado");
            
            // Remove one or more customers from the collection using the removeCustomer() method
            energyReport.removeCustomer(1015);
            System.out.println("Utilizador removido");
            
            // Retrieve a customer from the collection using the getCustomer() method
            Customer retrievedCustomer = energyReport.getCustomer(1025);
            System.out.println(retrievedCustomer);
            
            // Calculate the total energy usage for a specific customer using the calculateTotalUsage() method
            double totalEnergyUsage = energyReport.calculateTotalUsage(1003);
            System.out.println("Total energy usage for customer 1003: " + totalEnergyUsage);
        
            // Generate a report of all customers and their total energy usage using the generateReport() method
            energyReport.generateReport("energy_report.txt");
            System.out.println("Ficheiro Salvo");
    }
}
