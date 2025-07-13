public class ConcertTester {
    public static void main(String[] args) {
        ConcertManager cm = new ConcertManager();

        // ----------------------------------------------------------
        //ordenei o concerto para ficar igual ao meu construtor (double duracao, String LocalConcerto, String DataEHoraInicio)
        Concert c1 = new Concert(25.0, "Madrid, Espanha", "2025-05-27 11:00");
        Concert c2 = new Concert(35.0, "Oslo, Suecia", "2025-05-28 05:00");
        cm.addConcert(c1);
        cm.addConcert(c2);
        // ----------------------------------------------------------

        cm.printAllConcerts();

        // ----------------------------------------------------------
        System.out.println(cm.getConcert(1));
        System.out.println(cm.calculateConcertProfit(1));
        System.out.println(cm.getConcert(2));
        System.out.println(cm.calculateConcertProfit(2));
        System.out.println(cm.getConcert(30));              // não existe!
        System.out.println(cm.calculateConcertProfit(30));    // não existe!
        // ----------------------------------------------------------

        System.out.println("---------------");
        cm.sortConcertsByProfit();
        System.out.println("---------------");

        // ----------------------------------------------------------
        //mudei o path do ficheiro pois não estava a ser encontrado e adicionei uma separação par a destacar melhor este passo
        System.out.println("------####File Reader ON####---------");
        cm.readFile("C:\\--PASTA DAS PASTAS--\\Programação\\Java\\125031\\src\\classicpimba.txt");
        cm.printAllConcerts();
        System.out.println("------####File Reader OFF####---------");

        // ----------------------------------------------------------
        System.out.println(cm.getConcert(1));
        System.out.println(cm.calculateConcertProfit(1));
        System.out.println(cm.getConcert(2));
        System.out.println(cm.calculateConcertProfit(2));
        System.out.println(cm.getConcert(30));
        System.out.println(cm.calculateConcertProfit(30));
        // ----------------------------------------------------------
        //fiz a mesma coisa que no reader, mas em vez de separar só verifiquei dei um output positivito
        cm.writeFile("C:\\--PASTA DAS PASTAS--\\Programação\\Java\\125031\\src\\result.txt");
        System.out.println("------####File Write completo com sucesso####---------");


        // ----------------------------------------------------------

        System.out.println("---------------");
        cm.sortConcertsByProfit();
        System.out.println("---------------");

        // ----------------------------------------------------------

    }
}
