public class StandardConcertProfitCalculator implements IConcertProfitCalculator{
    double lucro = 0.0;

    @Override
    public double  calculateConcertProfit(Concert t) {
        //1500 por hora, 1500 /60 = ? OU minutos -> horas * 1500
        double tempo = t.getDuracao() / 60;
        double lucro = tempo * 1500;
        String local = t.getLocalConcerto();
        
        if(!local.contains("Portugal")){
            lucro = lucro *2;
        }

        if(!local.contains("Portugal") || !local.contains("Espanha")){
            lucro += 800;
        }

        return lucro;
    }
}
