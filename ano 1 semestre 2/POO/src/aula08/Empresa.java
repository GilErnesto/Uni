package aula08;
import java.util.ArrayList;

public class Empresa {
    private String nome;
    private String codigoPostal;
    private String email;
    private ArrayList<veiculo> conjVeiculos = new ArrayList<>();

    public Empresa(String nome, String codigoPostal, String email){
        this.nome = nome;
        this.codigoPostal = codigoPostal;
        this.email = email;
    }
    public void addVeiculo(veiculo Veiculo){
        conjVeiculos.add(Veiculo);
    }

    public String getNome(){
        return nome;
    }
    public String getCodigoPostal(){
        return codigoPostal;
    }
    public String getEmail(){
        return email;
    }
}
