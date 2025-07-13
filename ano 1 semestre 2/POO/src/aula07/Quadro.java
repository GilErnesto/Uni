package aula07;

public class Quadro extends Obra {
    //informações adicionais sobre o tipo de tinta usado (óleo, guache, aguarela), se está emoldurada (sim/não), e o tamanho da tela (S, M, L, ou XL)
    private String tintaUsada;
    private boolean emoldurada;
    private String tamanho;

    public Quadro(String nome, String autor, double preçoBase, String tintaUsada, String tamanho, boolean emoldurado, String frame){
        super(nome, autor, preçoBase);
        if(sizeIsValido(tamanho) && tintaIsValido(tintaUsada)){
            this.tintaUsada = tintaUsada;
            this.emoldurada = emolduradoValido(frame);
            this.tamanho = tamanho;
        }
    }

    protected boolean tintaIsValido(String tinta) {
        if (tinta.equalsIgnoreCase("óleo") || tinta.equalsIgnoreCase("guache") || tinta.equalsIgnoreCase("aguarela")) {
            return true;
        } else {
            throw new IllegalArgumentException("Tipo de tinta inválido: " + tinta);
        }
    }

    protected boolean sizeIsValido(String size) {
        if (size.equalsIgnoreCase("S") || size.equalsIgnoreCase("M") || size.equalsIgnoreCase("L") || size.equalsIgnoreCase("XL")) {
            return true;
        } else {
            throw new IllegalArgumentException("Tamanho inválido: " + size);
        }
    }

protected boolean emolduradoValido(String framed){
    switch (framed.toLowerCase()) {
        case "s": return true;
        case "n": return false;
        default: throw new IllegalArgumentException("Valor inválido: use 's' ou 'n'");
    }
}


}
