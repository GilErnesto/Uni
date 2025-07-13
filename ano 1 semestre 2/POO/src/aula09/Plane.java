package aula09;

public class Plane {
    private String identificador;
    private String fabricante;
    private String modelo;
    private int anoProd;
    private int maxPassageiros;
    private int velocidadeMax;

    public Plane(String identificador, String fabricante, String modelo, int anoProd, int maxPassageiros, int velocidadeMax){
        this.identificador = identificador;
        this.fabricante = fabricante;
        this.modelo = modelo;
        this.anoProd = anoProd;
        this.maxPassageiros = maxPassageiros;
        this.velocidadeMax = velocidadeMax;
    }

    // Getters
    public String getIdentificador() { return identificador; }
    public String getFabricante() { return fabricante; }
    public String getModelo() { return modelo; }
    public int getAnoProd() { return anoProd; }
    public int getMaxPassageiros() { return maxPassageiros; }
    public int getVelocidadeMax() { return velocidadeMax; }
    public String getPlaneType(){return "Normal";}

    // Setters
    public void setFabricante(String fabricante) { this.fabricante = fabricante; }
    public void setModelo(String modelo) { this.modelo = modelo; }
    public void setAnoProd(int anoProd) { this.anoProd = anoProd; }
    public void setMaxPassageiros(int maxPassageiros) { this.maxPassageiros = maxPassageiros; }
    public void setVelocidadeMax(int velocidadeMax) { this.velocidadeMax = velocidadeMax; }

    @Override
    public String toString() {
        return String.format("Avião %s: %s %s, %d, %d passageiros, %d km/h",
                identificador, fabricante, modelo, anoProd, maxPassageiros, velocidadeMax);
    }
}
