package aula10;
import java.io.File;  // Import the File class
import java.io.FileNotFoundException;  // Import this class to handle errors
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Scanner; // Import the Scanner class to read text files
import java.util.ArrayList;
import java.util.List;


public class EnergyUsageReport {
    ArrayList<Customer> clientes = new ArrayList<>();

    public void load(String file) {
        try {
            File myObj = new File(file);
            Scanner myReader = new Scanner(myObj);
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                String[] parts = data.split("\\|");
                int Id = Integer.parseInt(parts[0].trim());
                List<Double> registo = new ArrayList<>();
                    for (int i = 1; i < parts.length; i++) {
                        registo.add(Double.parseDouble(parts[i].trim()));
                    }
                    clientes.add(new Customer(Id, registo));
            }
            myReader.close();
        } catch (FileNotFoundException e) {
            System.out.println("Ficheiros não encontrado.");
            e.printStackTrace();
        }
    }

    public void addCustomer(Customer c){
        clientes.add(c);
    }

    public void removeCustomer(int Id){
        clientes.removeIf(cl -> cl.getCustomerId() == Id);
    }

    public Customer getCustomer(int Id){
        //eturn clientes.stream().filter(cl -> cl.getCustomerId() == Id).findFirst().orElse(null);
        for (Customer cl : clientes) {
            if (cl.getCustomerId() == Id) {
                return cl;
            }
        }
        return null;
    }

    public double calculateTotalUsage(int Id){
        Customer cl = getCustomer(Id);
        double total = 0;
        for(int i=0; i<cl.getMeterReadings().size(); i++){
            total += cl.getMeterReadings().get(i);
        }
        return total;
    }


    public void generateReport(String file) {
        try {
            Path filePath = Paths.get(file);
            File f = filePath.toFile();
            
            try (java.io.PrintWriter writer = new java.io.PrintWriter(f)) {
                for (Customer Cost : clientes ) {
                    writer.print(Cost.getCustomerId());
                    for (Double contagem : Cost.getMeterReadings()) {
                        writer.print("|" + contagem);
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