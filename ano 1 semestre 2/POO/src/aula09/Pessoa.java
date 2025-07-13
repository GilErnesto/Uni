package aula09;

public class Pessoa {
    private String nome;
    private int idade;

    public Pessoa(String nome, int idade) {
        this.nome = nome;
        this.idade = idade;
    }

    @Override
    public String toString() {
        // Fix: Add the idade parameter to String.format()
        return String.format("Nome: %s, Idade: %d", nome, idade);
    }

    // Make sure to implement equals and hashCode methods for proper HashSet behavior
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Pessoa)) return false;
        Pessoa pessoa = (Pessoa) o;
        return idade == pessoa.idade && 
               (nome != null ? nome.equals(pessoa.nome) : pessoa.nome == null);
    }

    @Override
    public int hashCode() {
        int result = nome != null ? nome.hashCode() : 0;
        result = 31 * result + idade;
        return result;
    }
}