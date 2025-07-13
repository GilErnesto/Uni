package aula09;

public class CommercialPlane extends Plane {
    private int numPassageiros;

    public CommercialPlane(String identificador, String fabricante, String modelo, int anoProd, int maxPassageiros, int velocidadeMax, int numPassageiros){
        super(identificador, fabricante, modelo, maxPassageiros, velocidadeMax, anoProd);
        this.numPassageiros = numPassageiros;
    }

    public int getNumPassageiros(){return numPassageiros;}
    public int setNumPassageiros(int numPassageiros){return this.numPassageiros = numPassageiros;}

    @Override
    public String getPlaneType(){return "Comercial";}

    @Override
    public String toString() {
        return super.toString() + String.format("Este avião leva %d passgeiros. E é de tipo %s", numPassageiros, getPlaneType());
    }
}