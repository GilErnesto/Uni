import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class Concert {
    private int id;
    private static int nextId = 1;
    private double duracao; //minutos
    private String LocalConcerto; //cidade,país
    private LocalDateTime DataEHoraInicio;

    public Concert(double duracao, String LocalConcerto, String DataEHoraInicio ) {
        this.id = nextId++;
        this.duracao = duracao;
        this.LocalConcerto = LocalConcerto;
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm");
        this.DataEHoraInicio = LocalDateTime.parse(DataEHoraInicio, formatter);
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
    this.id = id;
    }

    public double getDuracao() {
        return duracao;
    }

    public String getLocalConcerto() {
        return LocalConcerto;
    }

    public LocalDateTime getDataEHoraInicio() {
        return DataEHoraInicio;
    }

    public String getMes() {
        return DataEHoraInicio.getMonth().toString();
    }

    public String getDataEHoraInicioFormatada() {
    DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm");
    return DataEHoraInicio.format(formatter);
    }

    @Override
public String toString() {
    return "Concerto [id= " + id + ", duracao = " + duracao + " minutos, LocalConcerto= " + LocalConcerto + ", DataEHoraInicio= " + getDataEHoraInicioFormatada() + "]";
}

}
