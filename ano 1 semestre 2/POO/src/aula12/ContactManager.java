package aula12;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.time.LocalDate;
import java.util.List;
import java.util.Scanner;
import java.util.ArrayList;
import aula12.IContactCostCalculator.ContactType;

public class ContactManager {
    private List<Contact> contacts;

    public ContactManager() {
        this.contacts = new ArrayList<>();
    }

    public boolean addContact(Contact c) {
        if (c == null) return false;

        for (Contact existingContact : contacts) {
            if (existingContact.getNome().equals(c.getNome()) &&
                existingContact.getnTel() == c.getnTel() &&
                existingContact.getEmail().equals(c.getEmail())) {
                return false;
            }
        }

        return contacts.add(c);
    }

    public boolean removeContact(int id) {
        return contacts.removeIf(c -> c.getIdUnico() == id);
    }

    public Contact getContact(int id) {
        for (Contact c : contacts) {
            if (c.getIdUnico() == id) return c;
        }
        return null;
    }

    public double calculateCost(int id) {
        Contact contact = getContact(id);
        if (contact == null) {
            System.out.println("Contact not found.");
            return 0;
        }

        StandardCostCalculator calc = new StandardCostCalculator();
        return calc.calculateCost(contact.getPhoneCounter(), ContactType.CELLNUMBER)
             + calc.calculateCost(contact.getEmailCounter(), ContactType.EMAIL);
    }

    public void printAllContacts() {
        int i = 1;
        for (Contact c : contacts) {
            System.out.println(i + ": " + c);
            i++;
        }
    }

    public void readFile(String file) {
        try (Scanner leitor = new Scanner(new File(file))) {
            int id = 10000;

            while (leitor.hasNextLine()) {
                String linha = leitor.nextLine();
                String[] dados = linha.split("\t");

                if (dados.length == 4) {
                    String nome = dados[0];
                    int nTel = Integer.parseInt(dados[1]);
                    String email = dados[2];
                    LocalDate data = LocalDate.parse(dados[3]);

                    Contact novoContact = new Contact(id++, nome, nTel, email, data);
                    addContact(novoContact);
                }
            }

        } catch (FileNotFoundException e) {
            System.out.println("Ficheiro não encontrado!");
        }
    }

    public void writeFile(String file) {
        try (FileWriter writer = new FileWriter(file)) {
            for (Contact contact : contacts) {
                writer.write(String.format("%s;%d;%s;%s;%d%n",
                    contact.getNome(),
                    contact.getnTel(),
                    contact.getEmail(),
                    contact.getDataDeNascimento(),
                    contact.getIdUnico()));
            }
        } catch (IOException e) {
            System.out.println("Erro ao escrever no ficheiro: " + e.getMessage());
        }
    }

    public List<Contact> searchOlderThan(LocalDate date) {
        List<Contact> result = new ArrayList<>();
        for (Contact c : contacts) {
            if (c.getDataDeNascimento().isBefore(date)) {
                result.add(c);
            }
        }
        return result;
    }
}
