import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class ConcertManager {
    ArrayList<Concert> concerts = new ArrayList<>();   

    public void addConcert( Concert t) {
        concerts.add(t);
    }

    public void removeConcert(int id) {
        Concert toRemove = null;
        for (Concert t : concerts) {
            if (t.getId() == id) {
                toRemove = t;
                break;
            }
        }
        if (toRemove != null) {
            concerts.remove(toRemove);
        }
    }

    public Concert getConcert(int id) {
        for (Concert concert : concerts)
            {
                if(concert.getId() == id){   
                    return concert;
                }
            }
        return null;
    }

    public double calculateConcertProfit(int id){
        for (Concert concert : concerts) {
                if (concert.getId() == id) {
                    return new StandardConcertProfitCalculator().calculateConcertProfit(concert);
                }
            }
            return -1;
    }

    public void printAllConcerts() {
        for (Concert concert : concerts) {
            System.out.println(concert);
        }
    }

//sortConcertsByProfit(): imprime no ecrã todos os concertos separados por mês do ano. Dentro de cada mês, os concertos devem ser impressos por ordem decrescente do seu lucro. [15%]
    public void sortConcertsByProfit(){
        ArrayList<Concert> copia = new ArrayList<>(concerts);

        Map<String, Integer> ordemMes = new HashMap<>();
        ordemMes.put("JANUARY", 1);
        ordemMes.put("FEBRUARY", 2);
        ordemMes.put("MARCH", 3);
        ordemMes.put("APRIL", 4);
        ordemMes.put("MAY", 5);
        ordemMes.put("JUNE", 6);
        ordemMes.put("JULY", 7);
        ordemMes.put("AUGUST", 8);
        ordemMes.put("SEPTEMBER", 9);
        ordemMes.put("OCTOBER", 10);
        ordemMes.put("NOVEMBER", 11);
        ordemMes.put("DEZEMBER", 12);

        copia.sort((t1, t2) -> {
        int mes1 = ordemMes.getOrDefault(t1.getMes(), 1);
        int mes2 = ordemMes.getOrDefault(t2.getMes(), 1);

        if (mes1 != mes2) {
            return Integer.compare(mes1, mes2); 
        } else {
            double custo1 = calculateConcertProfit(t1.getId());
            double custo2 = calculateConcertProfit(t2.getId());
            return Double.compare(custo2, custo1); 
        }
    });

        for (Concert concert : copia) {System.out.println(concert + " | Mês: " + concert.getMes() + " | Lucro: " + calculateConcertProfit(concert.getId()));
    }
    }

    public void readFile(String fich) {
    try (BufferedReader br = new BufferedReader(new FileReader(fich))) {
        String linha = br.readLine(); 

        while ((linha = br.readLine()) != null) {
            if (linha.trim().isEmpty()) continue;

            String[] partes = linha.split(";");
            if (partes.length < 4) continue;  //talves isto possa causar erro

            int id = Integer.parseInt(partes[0].trim());
            double duracao = Double.parseDouble(partes[1].trim());
            String local = partes[2].trim();
            String dataHora = partes[3].trim();
            
            //double duracao, String LocalConcerto, String DataEHoraInicio
            Concert nova = new Concert(duracao, local, dataHora);
            nova.setId(id);  

            Concert existente = getConcert(id);
            if (existente != null) {
                concerts.remove(existente);
            }

            concerts.add(nova);
        }
    } catch (IOException e) {
        System.out.println("Erro ao ler ficheiro: " + e.getMessage());
    } catch (NumberFormatException e) {
        System.out.println("Erro ao converter número: " + e.getMessage());
    }
}

public void writeFile(String fich) {
    try (BufferedWriter bw = new BufferedWriter(new FileWriter(fich))) {
        bw.write("ID; Duracao; Local do Concerto; Data e Hora");
        bw.newLine();

        for (Concert concert : concerts) {
            String linha = String.format("%d; %.1f; %s  ; %s", concert.getId(),concert.getDuracao(),concert.getLocalConcerto(),concert.getDataEHoraInicio());
            bw.write(linha);
            bw.newLine();
        }

    } catch (IOException e) {
        System.out.println("Erro ao gravar ficheiro: " + e.getMessage());
    }
}


}
