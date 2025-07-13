package aula08;

public class carVeiculo implements IKmPercorridos{
    private String matricula;
    private String marca;
    private String modelo;
    private int potencia; //cv
    private int ultimoTrajeto;
    private int distanciaTotal;

    public carVeiculo(String matricula, String marca, String modelo, int potencia){
        this.matricula = matricula;
        this.marca = marca;
        this.modelo = modelo;
        this.potencia = potencia;
    }

    public String getMatricula() {
        return matricula;
    }
    public String getMarca() {
        return marca;
    }
    public String getmodelo() {
        return modelo;
    }
    public int getPotencia(){
        return potencia;
    }

    @Override
    public void trajeto(int quilometros){
        System.out.println(quilometros);
    }
    public int ultimoTrajeto(){
        return ultimoTrajeto;
    }
    public int distanciaTotal(){
        return distanciaTotal;
    }
}

