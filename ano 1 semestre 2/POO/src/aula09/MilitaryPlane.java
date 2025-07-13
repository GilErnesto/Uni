package aula09;

public class MilitaryPlane extends Plane{
    private int numMunicao;

    public MilitaryPlane(String identificador, String fabricante, String modelo, int anoProd, int maxPassageiros, int velocidadeMax, int numMunicao){
        super(identificador, fabricante, modelo, maxPassageiros, velocidadeMax, anoProd);
        this.numMunicao = numMunicao;
    }

    public int getNumMunicao(){return numMunicao;}
    public void setNumMunicoes(int numMunicao) {this.numMunicao = numMunicao;}

    @Override
    public String getPlaneType(){return "Militar";}

    @Override
    public String toString() {
        return super.toString() + String.format(" Este avião leva %d balas. E é de tipo %s", numMunicao, getPlaneType());
    }
}