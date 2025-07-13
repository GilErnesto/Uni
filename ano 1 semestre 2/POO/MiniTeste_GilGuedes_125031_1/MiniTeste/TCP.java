package MiniTeste_GilGuedes_125031.MiniTeste;

public class TCP extends Pacote {
    protected String mensagem;

    public TCP(String origem, String destino, String mensagem) {
        super(origem, destino);
        if(mensagem.length() > 1460)
        {System.out.print("Mensagem é muito longa");
        } else{this.mensagem = mensagem;}
    }
    
    public String getMensagem(){
        return mensagem;
    }
}
