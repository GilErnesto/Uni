package aula07;

public class Obra {
    //informações como o nome da obra, o seu autor, preço base e um identificador da peça único, atribuído automaticamente (e sequencialmente a partir de 33)
    private String nome;
    private String autor;
    private double preçoBase;
    private static int identificador = 33;

    public Obra(String nome, String autor, double preçoBase){
        this.nome = nome;
        this.autor = autor;
        this.preçoBase = preçoBase;
    }

    public String getNome(){return nome;}
    public String getAutor(){return autor;}
    public double getPreçoBase(){return preçoBase;}
    public int identificadorObra(){return identificador + 1;}
}
