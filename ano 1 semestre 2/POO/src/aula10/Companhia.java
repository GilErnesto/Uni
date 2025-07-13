package aula10;

public class Companhia {
    private String sigla;
    private String nome;

    public Companhia(String sigla, String nome) {
        this.sigla = sigla;
        this.nome = nome;
    }

    public String getSigla() { return sigla; }
    public String getNome() { return nome; }
}
