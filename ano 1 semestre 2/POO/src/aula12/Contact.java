package aula12;

import java.time.LocalDate;

public class Contact {
    private String nome;
    private int nTel;
    private String email;
    private LocalDate dataDeNascimento;
    private int idUnico;

    private int phoneCounter = 0;
    private int emailCounter = 0;

    public Contact(int idUnico, String nome, int nTel, String email, LocalDate dataDeNascimento) {
        this.nome = nome;
        this.nTel = nTel;
        this.email = email;
        this.dataDeNascimento = dataDeNascimento;
        this.idUnico = idUnico;
    }

    public int getIdUnico() {
        return idUnico;
    }

    public String getNome() {
        return nome;
    }

    public int getnTel() {
        if (String.valueOf(nTel).length() == 9) {
            return nTel;
        }
        throw new IllegalArgumentException("Número de telefone inválido.");
    }

    public String getEmail() {
        if (email != null && email.matches("^[A-Za-z0-9+_.-]+@(.+)$")) {
            return email;
        }
        throw new IllegalArgumentException("Email inválido.");
    }

    public LocalDate getDataDeNascimento() {
        return dataDeNascimento;
    }

    public void call(double units) {
        phoneCounter += units;
        System.out.println(nome + " fez uma chamada de " + units + " minutos.");
    }

    public void email() {
        emailCounter++;
        System.out.println(nome + " enviou um e-mail.");
    }

    public int getEmailCounter() {
        return emailCounter;
    }

    public double getPhoneCounter() {
        return phoneCounter;
    }

    @Override
    public String toString() {
        return String.format("Nome: %s ;Nº Telemóvel: %d ;Id Único: %d ;Email: %s ;Data de Nascimento: %s",
                nome, nTel, idUnico, email, dataDeNascimento);
    }
}
