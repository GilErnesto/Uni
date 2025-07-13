package aula10;

public class Voo {
    private String hora;
    private String atraso;
    private String origem;
    private String nVoo;
    private Companhia companhia;

    public Voo(String hora, String nVoo, String origem, String atraso, Companhia companhia) {
        this.hora = hora;
        this.nVoo = nVoo;
        this.origem = origem;
        this.atraso = atraso;
        this.companhia = companhia;
    }

    public String getHora() { return hora; }
    public String getOrigem() { return origem; }
    public String getAtraso() { return atraso; }
    public String getNVoo() { return nVoo; }
    public Companhia getCompanhia() { return companhia; }
}
