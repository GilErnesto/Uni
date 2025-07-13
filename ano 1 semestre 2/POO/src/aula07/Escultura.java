package aula07;

public class Escultura extends Obra{
    //informações adicionais sobre o seu material (madeira, cerâmica ou metal), e se é uma peça única ou quantos exemplares foram produzidos dessa peça
    private String material;
    private boolean pecaUnica;

    public Escultura(String nome, String autor, double preçoBase, String material, boolean pecaUnica, String unica){
        super(nome, autor, preçoBase);
        if(materialValid(material)){
            this.material = material;
            this.pecaUnica = IsPecaUnica(unica);
        } else{
            System.out.print("Invalid Escultura");
        }
    }

    protected boolean materialValid(String material){
        if(material.equalsIgnoreCase("madeira") || material.equalsIgnoreCase("cerâmica") || material.equalsIgnoreCase("metal")){return true;} else{throw new IllegalArgumentException("Illegal material: " + material);} 
    }

    protected boolean IsPecaUnica(String unica){
        switch (unica) {
            case "s": return true;
            case "n": return false;
            default: throw new IllegalArgumentException("s/n");
        }

    }
}
