package aula06;

public class Ex1 {
    static class DateYMD {
        private int day;
        private int month;
        private int year;

        public DateYMD(int day, int month, int year) {
            this.day = day;
            this.month = month;
            this.year = year;
            if(verificar(day, month, year)){
                System.out.println("Data válida: " + day + "/" + month + "/" + year);
            } else {
                System.out.println("Data inválida: " + day + "/" + month + "/" + year);
                
            }
        }
        public boolean verificar(int dia, int mes, int ano) {
            if (mes == 2) {
                if (ano % 4 == 0 && (ano % 100 != 0 || ano % 400 == 0)) {
                    return dia <= 29;
                } else {
                    return dia <= 28;
                }
            } else if (mes == 4 || mes == 6 || mes == 9 || mes == 11) {
                return dia <= 30;
            } else if (mes >= 1 && mes <= 12) {
                return dia <= 31;
            }
            return false;
        }
        
        public int getDay() {
            return day;
        }
        
        public int getMonth() {
            return month;
        }
        
        public int getYear() {
            return year;
        }
    }

    public class Pessoa {
        private String nome;
        private int cc;
        private DateYMD dataNasc;
        
        public Pessoa(String nome, int cc, DateYMD dataNasc) {
            if (nome == null || nome.trim().isEmpty()) {
                System.out.println("Nome inválido");
            }
            if (cc <= 0) {
                System.out.println("CC inválido");
            }
            if (dataNasc == null) {
                System.out.println("Data de nascimento inválida");
            }
            
            this.nome = nome;
            this.cc = cc;
            this.dataNasc = dataNasc;
        }
        
        public String getNome() {
            return nome;
        }
        
        @Override
        public String toString() {
            return String.format("Nome: %s, CC: %d, Data de Nascimento: %d/%d/%d",
            nome, cc, dataNasc.getDay(), dataNasc.getMonth(), dataNasc.getYear());
        }
    }

    public class Aluno extends Pessoa {
        private static int ultimoNMec = 99;
        private int nMec;
        private DateYMD dataInsc;
        
        public Aluno(String nome, int cc, DateYMD dataNasc, DateYMD dataInsc) {
            super(nome, cc, dataNasc);
            this.nMec = ++ultimoNMec;
            this.dataInsc = dataInsc;
        }
        
        public Aluno(String nome, int cc, DateYMD dataNasc) {
            super(nome, cc, dataNasc);
            this.nMec = ++ultimoNMec;
            this.dataInsc = new DateYMD(20, 3, 2025);
        }
        
        public int getNMec() {
            return nMec;
        }
        
        @Override
        public String toString() {
            return super.toString() + String.format(", NMec: %d, Data de Inscrição: %d/%d/%d",
            nMec, dataInsc.getDay(), dataInsc.getMonth(), dataInsc.getYear());
        }
    }
    
    public class Professor extends Pessoa {
    private String categoria;
    private static final String[] CATEGORIAS = {"Auxiliar", "Associado", "Catedrático"};
    private String departamento;

    public Professor(String nome, int cc, DateYMD dataNasc, String categoria, String departamento) {
        super(nome, cc, dataNasc);
        if (!isValidCategoria(categoria)) {
            System.out.println("Categoria inválida");
        }
        this.categoria = categoria;
        this.departamento = departamento;
    }

    private boolean isValidCategoria(String categoria) {
        for (String cat : CATEGORIAS) {
            if (cat.equals(categoria)) return true;
        }
        return false;
    }

    @Override 
    public String toString() {
        return super.toString() + String.format(", Categoria: %s, Departamento: %s",
                categoria, departamento);
    }
}
public class Bolseiro extends Aluno {
    private int bolsa;
    private Professor orientador;

    public Bolseiro(String nome, int cc, DateYMD dataNasc, Professor orientador, int bolsa) {
        super(nome, cc, dataNasc);
        this.orientador = orientador;
        setBolsa(bolsa);
    }

    public void setBolsa(int bolsa) {
        if (bolsa < 0) {
            System.out.println("Valor da bolsa inválido");
        }
        this.bolsa = bolsa;
    }

    public int getBolsa() {
        return bolsa;
    }

    public Professor getOrientador() {
        return orientador;
    }

    public void setOrientador(Professor orientador) {
        if (orientador == null) {
            System.out.println("Orientador não pode ser null");
        }
        this.orientador = orientador;
    }
    @Override
    public String toString() {
        return super.toString() + String.format(", Bolsa: %d€, Orientador: %s",
                bolsa, orientador.getNome());
    }
}

public class Test {
    public static void main(String[] args) {
        // Create an Aluno instance
        Ex1.DateYMD dataNascAl = new Ex1.DateYMD(18, 7, 1990);
        Ex1.DateYMD dataInscAl = new Ex1.DateYMD(1, 9, 2018);
        Ex1 ex1 = new Ex1();
        Ex1.Aluno al = ex1.new Aluno("Andreia Melo", 9855678, dataNascAl, dataInscAl);

        // Create a Professor instance
        Ex1.DateYMD dataNascProf = new Ex1.DateYMD(13, 3, 1967);
        Ex1.Professor p1 = ex1.new Professor("Jorge Almeida", 3467225, dataNascProf, "Associado", "Informática");

        // Create a Bolseiro instance
        Ex1.DateYMD dataNascBol = new Ex1.DateYMD(11, 5, 1985);
        Ex1.Bolseiro bls = ex1.new Bolseiro("Igor Santos", 8976543, dataNascBol, p1, 900);
        
        // Update bolsa value
        bls.setBolsa(1050);

        // Print results
        System.out.println("Aluno: " + al.getNome());
        System.out.println(al);
        System.out.println("Bolseiro: " + bls.getNome() + ", NMec: " 
            + bls.getNMec() + ", Bolsa: " + bls.getBolsa() + ", Orientador: " 
            + bls.getOrientador().getNome());
        System.out.println(bls);
        }
    }
}