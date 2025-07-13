package aula10;

import java.io.*;
import java.util.*;

public class VooManager {
    private List<Companhia> companhias = new ArrayList<>();
    private List<Voo> voos = new ArrayList<>();

    public void loadCompanhias(String path) throws FileNotFoundException {
        Scanner sc = new Scanner(new File(path));
        if (sc.hasNextLine()) {
        sc.nextLine(); // ignora "Sigla\tCompanhia"
    }
        while (sc.hasNextLine()) {
        String linha = sc.nextLine().trim();

        if (linha.isEmpty()) continue; // Ignora linhas vazias

        String[] parts = linha.split("\\t");

        if (parts.length < 2) {
            System.out.println("⚠️ Linha inválida (faltam campos): " + linha);
            continue;
        }

        String sigla = parts[0].trim();
        String nome = parts[1].trim();
        companhias.add(new Companhia(sigla, nome));
    }

    sc.close();
}

    public void loadVoos(String path) throws FileNotFoundException {
        Scanner sc = new Scanner(new File(path));
        if (sc.hasNextLine()) {
        sc.nextLine(); // ignora "Hora	Voo	Origem	Atraso"
    }
        while (sc.hasNextLine()) {
            String[] parts = sc.nextLine().split("\\t");
            String hora = parts[0].trim();
            String nVoo = parts[1].trim();
            String origem = parts[2].trim();
            String atraso = parts.length > 3 ? parts[3].trim() : "-";

            String sigla = nVoo.replaceAll("^([A-Z]{2}).*", "$1");
            Companhia comp = companhias.stream()
                .filter(c -> c.getSigla().equals(sigla))
                .findFirst()
                .orElse(new Companhia(sigla, "Desconhecida"));

            voos.add(new Voo(hora, nVoo, origem, atraso, comp));
        }
        sc.close();
    }

    public void printALL() {
        System.out.printf("Hora\tVoo\tCompanhia\t\tOrigem\t\tAtraso\tObs\n");
        for (Voo v : voos) {
            System.out.printf("%s\t%s\t%-20s\t%-15s\t%s\t%s\n",
                v.getHora(), v.getNVoo(), v.getCompanhia().getNome(), v.getOrigem(),
                v.getAtraso(), calcularObs(v.getHora(), v.getAtraso()));
        }
    }

    private String calcularObs(String hora, String atraso) {
        if (atraso.equals("-")) return "-";

        try {
            String[] h = hora.split(":");
            String[] a = atraso.split(":");

            int h1 = Integer.parseInt(h[0]);
            int m1 = Integer.parseInt(h[1]);
            int h2 = Integer.parseInt(a[0]);
            int m2 = Integer.parseInt(a[1]);

            int totalMin = (h1 * 60 + m1) + (h2 * 60 + m2);
            int newH = totalMin / 60;
            int newM = totalMin % 60;

            return String.format("%02d:%02d", newH, newM);
        } catch (Exception e) {
            return "?";
        }
    }

    public void createInfopublico(String file) {
        try (PrintWriter writer = new PrintWriter(file)) {
            // Redirect System.out to capture the printALL output
            ByteArrayOutputStream baos = new ByteArrayOutputStream();
            PrintStream ps = new PrintStream(baos);
            PrintStream old = System.out;
            System.setOut(ps);
            
            // Call printALL() which will now write to our stream
            printALL();
            
            // Restore the original System.out
            System.setOut(old);
            
            // Write the captured output to file
            writer.print(baos.toString());
            
        } catch (IOException e) {
            System.err.println("An error occurred while writing to the file");
            e.printStackTrace();
        }
    }

    public static void main(String[] args) throws FileNotFoundException {
        VooManager vm = new VooManager();
        vm.loadCompanhias("src/aula10/companhias.txt");
        vm.loadVoos("src/aula10/voos.txt");
        vm.printALL();
        vm.createInfopublico("src/aula10/Infopublico.txt");
    }
}
