package aula12;
import java.time.LocalDate;

public class ContactsTester {
    public static void main(String[] args) {
        ContactManager cm = new ContactManager();

        Contact c1 = new Contact(1, "Maria Joaquina", 911234567, "joaquina@ua.pt", LocalDate.parse("1985-01-01"));      
        Contact c2 = new Contact(2, "João Miguel", 911234568, "joao@ua.pt", LocalDate.parse("1988-01-01"));
        cm.addContact(c1);
        cm.addContact(c2);
        cm.printAllContacts();

        System.out.println("\n--- Testes Individuais ---");
        System.out.println(cm.getContact(1));
        System.out.println(cm.getContact(2));
        System.out.println(cm.getContact(5));           // não existe
        System.out.println(cm.calculateCost(5));        // não existe

        System.out.println("\n--- Ações ---");
        c1.call(3.5);
        c2.email();
        cm.printAllContacts();

        System.out.println("\n--- Leitura de Ficheiro ---");
        cm.readFile("src/aula12/contatos.txt");
        cm.printAllContacts();

        System.out.println("\n--- Escrita de Ficheiro ---");
        cm.writeFile("src/aula12/out.txt");
    }
}
