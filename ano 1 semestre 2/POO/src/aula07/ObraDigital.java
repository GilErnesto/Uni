package aula07;

public class ObraDigital extends Obra{
    //informações adicionais sobre a blockchain onde a obra existe (exemplo: Ethereum, Polygon, Solana, etc.) e o endereço do contrato desse NFT em hexadecimal (exemplo: 0x1234AF

    private String blockchain;
    private String NFT;

    public ObraDigital(String nome, String autor, double preçoBase, String blockchain, String NFT){
        super(nome, autor, preçoBase);
        if(blockchainValido(blockchain) && isNFT(NFT)){
            this.blockchain = blockchain;
            this.NFT = NFT;
        }
    }

    protected boolean blockchainValido(String blockchain){
        if(blockchain.equalsIgnoreCase("Ethereum") || blockchain.equalsIgnoreCase("Polygon") || blockchain.equalsIgnoreCase("Solana")){
            return true;
        } else{throw new IllegalArgumentException("Illegal blockchain " + blockchain);}
    }

    protected boolean isNFT(String nft){
        int length = nft.length(); // 8
        char char1 = nft.charAt(0); // 0
        char char2 = nft.charAt(1); // x
        String resto = nft.substring(2);
        if(length == 8 && char1 == '0' && char2 == 'x' ){
            for(int i = 0; i < resto.length(); i++){
                char c = resto.charAt(i);
                if((c >= '1' && c <= '9') || (c >= 'A' && c <= 'F')){
                    continue;
                } else{throw new IllegalArgumentException("Illegal NFT " + nft);}
            }
            return true;
        } else{ throw new IllegalArgumentException("Illegal NFT " + nft);}
    }

}
