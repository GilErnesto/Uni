package aula08;

class motociclo extends carVeiculo{
    private String tipo;
    
    public motociclo(String matricula, String marca, String modelo, int potencia, String tipo) {
        super(matricula, marca, modelo, potencia);
        if(tipo == "desportivo" || tipo == "estrada"){this.tipo = tipo;} 
    }
    
    public String getTipo(){
        return tipo;
    }
}

class veiLigeiro extends carVeiculo{
    private int numeroQuadro;
    private int bagageira;

    public veiLigeiro(String matricula, String marca, String modelo, int potencia, int numeroQuadro, int bagageira){
        super(matricula, marca, modelo, potencia);
        this.numeroQuadro = numeroQuadro;
        this.bagageira = bagageira;
    }

    public int getNumeroQuadro(){
        return numeroQuadro;
    }
    public int getBagageira(){
        return bagageira;
    }
}

class taxi extends veiLigeiro{
    private int licenca;

    public taxi(String matricula, String marca, String modelo, int potencia, int numeroQuadro, int bagageira, int licenca){
        super(matricula, marca, modelo, potencia, numeroQuadro, bagageira);
        this.licenca = licenca;
    }

    public int getLicenca(){
        return licenca;
    }
}

class pesadoMercadorias extends carVeiculo{
    private int numeroQuadro;
    private int peso;
    private int cargaMaxima;

    public pesadoMercadorias(String matricula, String marca, String modelo, int potencia,int numeroQuadro, int peso, int cargaMaxima){
        super(matricula, marca, modelo, potencia);
        this.numeroQuadro = numeroQuadro;
        this.peso = peso;
        this.cargaMaxima = cargaMaxima;
    }

    public int getNumeroQuadro(){
        return numeroQuadro;
    }
    public int getPeso(){
        return peso;
    }
    public int getCargaMaxima(){
        return cargaMaxima;
    }
}

class pesadoPassageiros extends carVeiculo{
    private int numeroQuadro;
    private int peso;
    private int maxPassageiros; 

    public pesadoPassageiros(String matricula, String marca, String modelo, int potencia,int numeroQuadro, int peso, int maxPassageiros){
        super(matricula, marca, modelo, potencia);
        this.maxPassageiros = maxPassageiros;
        this.peso = peso;
        this.numeroQuadro = numeroQuadro;
    }
    public int getNumeroQuadro(){
        return numeroQuadro;
    }
    public int getPeso(){
        return peso;
    }
    public int getMaxPassageiros(){
        return maxPassageiros;
    }
}

public class veiculo {

}
