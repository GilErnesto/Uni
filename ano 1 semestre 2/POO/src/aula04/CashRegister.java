package aula04;
import java.util.ArrayList;

class Product {
    private String name;
    private double price;
    private int quantity;

    public Product(String name, double price, int quantity) {
        this.name = name;
        this.price = price;
        this.quantity = quantity;
    }

    public double getTotalValue() {
        return price * quantity;
    }

    public String getName() {
        return name;
    }

    public double getPrice() {
        return price;
    }

    public int getQuantity() {
        return quantity;
    }
}

class CashRegister {
    private ArrayList<Product> listaProdutos = new ArrayList<>();   //Qual é a diferença entre privaet ou não?
    private double totalValue;

    public void addProduct(Product p) {
        listaProdutos.add(p);
        totalValue += p.getTotalValue();
    }

    public String toString() {
        String prints = "";
        for (Product p : listaProdutos){
            prints += String.format("%-16s %-10.2f %-10d %-10.2f\n", p.getName(), p.getPrice(), p.getQuantity(), p.getTotalValue());
        }
        prints += "Total: " + totalValue;
        return prints;
    }

public class CashRegisterDemo {
    public static void main(String[] args) {
        // Cria e adiciona 5 produtos
        CashRegister cr = new CashRegister();
        cr.addProduct(new Product("Book", 9.99, 3));
        cr.addProduct(new Product("Pen", 1.99, 10));
        cr.addProduct(new Product("Headphones", 29.99, 2));
        cr.addProduct(new Product("Notebook", 19.99, 5));
        cr.addProduct(new Product("Phone case", 5.99, 1));
        
        // Listar o conteúdo e valor total
        System.out.printf("%-16s %-10s %-10s %-10s\n", "Product", "Price", "Quantity", "Value");
        System.out.println(cr);
    }
}
}