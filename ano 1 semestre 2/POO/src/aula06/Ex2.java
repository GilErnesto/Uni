package aula06;

import java.util.*;

public class Ex2 {
    public static void main(String[] args) {
        new ContactManager().run();
    }
}

class Pessoa {
    private String nome;
    
    public Pessoa(String nome) {
        this.nome = nome;
    }
    
    public String getNome() {
        return nome;
    }
}

class Contact {
    private static int nextId = 1;
    private final int id;
    private String telefone;
    private String email;
    private Pessoa pessoa;

    public Contact(Pessoa pessoa, String telefone, String email) {
        if (pessoa == null) {
            throw new IllegalArgumentException("Pessoa não pode ser null");
        }
        if ((telefone == null || telefone.isEmpty()) && (email == null || email.isEmpty())) {
            throw new IllegalArgumentException("Deve fornecer telefone ou email");
        }
        this.id = nextId++;
        this.pessoa = pessoa;
        setTelefone(telefone);
        setEmail(email);
    }

    public boolean isEmailValid(String email) {
        if (email == null || email.isEmpty()) return true;  // email is optional
        return email.matches("^[A-Za-z0-9+_.-]+@[A-Za-z0-9.-]+\\.(com|pt|org|net)$");
    }

    public boolean isTelefoneValid(String telefone) {
        if (telefone == null || telefone.isEmpty()) return true;  // telefone is optional
        return telefone.matches("^9\\d{8}$");
    }

    public void setTelefone(String telefone) {
        if (!isTelefoneValid(telefone)) {
            throw new IllegalArgumentException("Telefone inválido");
        }
        this.telefone = telefone;
    }

    public void setEmail(String email) {
        if (!isEmailValid(email)) {
            throw new IllegalArgumentException("Email inválido");
        }
        this.email = email;
    }

    // Getters
    public int getId() { return id; }
    public String getTelefone() { return telefone; }
    public String getEmail() { return email; }
    public Pessoa getPessoa() { return pessoa; }

    @Override
    public String toString() {
        return String.format("ID: %d, Nome: %s, Telefone: %s, Email: %s", 
            id, pessoa.getNome(), 
            telefone != null ? telefone : "N/A", 
            email != null ? email : "N/A");
    }
}

class ContactManager {
    private List<Contact> contacts = new ArrayList<>();
    private Scanner scanner = new Scanner(System.in);

    public void run() {
        while (true) {
            showMenu();
            int option = scanner.nextInt();
            scanner.nextLine(); // consume newline

            switch (option) {
                case 1: insertContact(); break;
                case 2: updateContact(); break;
                case 3: deleteContact(); break;
                case 4: searchContact(); break;
                case 5: listContacts(); break;
                case 0: return;
                default: System.out.println("Opção inválida!");
            }
        }
    }

    private void showMenu() {
        System.out.println("\n=== Gestão de Contactos ===");
        System.out.println("1. Inserir contacto");
        System.out.println("2. Alterar contacto");
        System.out.println("3. Apagar contacto");
        System.out.println("4. Procurar contacto");
        System.out.println("5. Listar contactos");
        System.out.println("0. Sair");
        System.out.print("Opção: ");
    }

    private void insertContact() {
        System.out.print("Nome: ");
        String nome = scanner.nextLine();
        
        // Check if person already exists
        boolean exists = contacts.stream()
            .anyMatch(c -> c.getPessoa().getNome().equalsIgnoreCase(nome));
        
        if (exists) {
            System.out.print("Pessoa já existe. Continuar? (S/N): ");
            if (!scanner.nextLine().equalsIgnoreCase("S")) {
                return;
            }
        }

        System.out.print("Telefone (ou Enter para saltar): ");
        String telefone = scanner.nextLine();
        System.out.print("Email (ou Enter para saltar): ");
        String email = scanner.nextLine();
        
        try {
            contacts.add(new Contact(new Pessoa(nome), 
                telefone.isEmpty() ? null : telefone, 
                email.isEmpty() ? null : email));
            System.out.println("Contacto adicionado com sucesso!");
        } catch (IllegalArgumentException e) {
            System.out.println("Erro: " + e.getMessage());
        }
    }

    private void updateContact() {
        System.out.print("Pesquisar por (1-ID, 2-Nome): ");
        int searchType = scanner.nextInt();
        scanner.nextLine();
        
        List<Contact> found = new ArrayList<>();
        if (searchType == 1) {
            System.out.print("ID: ");
            int id = scanner.nextInt();
            scanner.nextLine();
            contacts.stream().filter(c -> c.getId() == id).findFirst()
                .ifPresent(found::add);
        } else {
            System.out.print("Nome: ");
            String nome = scanner.nextLine();
            contacts.stream()
                .filter(c -> c.getPessoa().getNome().toLowerCase()
                    .contains(nome.toLowerCase()))
                .forEach(found::add);
        }

        if (found.isEmpty()) {
            System.out.println("Contacto não encontrado!");
            return;
        }

        Contact toUpdate;
        if (found.size() > 1) {
            System.out.println("Vários contactos encontrados:");
            found.forEach(System.out::println);
            System.out.print("ID do contacto a alterar: ");
            int id = scanner.nextInt();
            scanner.nextLine();
            toUpdate = found.stream()
                .filter(c -> c.getId() == id)
                .findFirst()
                .orElse(null);
        } else {
            toUpdate = found.get(0);
        }

        if (toUpdate != null) {
            try {
                System.out.print("Novo telefone (ou Enter para manter): ");
                String telefone = scanner.nextLine();
                if (!telefone.isEmpty()) toUpdate.setTelefone(telefone);
                
                System.out.print("Novo email (ou Enter para manter): ");
                String email = scanner.nextLine();
                if (!email.isEmpty()) toUpdate.setEmail(email);
                
                System.out.println("Contacto atualizado com sucesso!");
            } catch (IllegalArgumentException e) {
                System.out.println("Erro: " + e.getMessage());
            }
        }
    }

    private void deleteContact() {
        System.out.print("ID do contacto a apagar: ");
        int id = scanner.nextInt();
        boolean removed = contacts.removeIf(c -> c.getId() == id);
        if (removed) {
            System.out.println("Contacto removido com sucesso!");
        } else {
            System.out.println("Contacto não encontrado!");
        }
    }

    private void searchContact() {
        System.out.print("Nome a procurar: ");
        String nome = scanner.nextLine();
        boolean found = false;
        for (Contact c : contacts) {
            if (c.getPessoa().getNome().toLowerCase().contains(nome.toLowerCase())) {
                System.out.println(c);
                found = true;
            }
        }
        if (!found) {
            System.out.println("Nenhum contacto encontrado!");
        }
    }

    private void listContacts() {
        if (contacts.isEmpty()) {
            System.out.println("Não existem contactos!");
            return;
        }
        contacts.forEach(System.out::println);
    }
}