package MiniTeste_GilGuedes_125031.MiniTeste;

public abstract class Pacote {
    protected String origem;
    protected String destino;
    
    public Pacote(String origem, String destino) {
        this.origem = origem;
        this.destino = destino;
    }

    public String getOrigem(){
        return origem;
    }
    public String getDestino(){
        return destino;
    }
}