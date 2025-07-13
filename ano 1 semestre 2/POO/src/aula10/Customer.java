package aula10;
import java.util.List;

public class Customer {
    private final int customerId;
    private final List<Double> meterReadings;

    public Customer(int customerId, List<Double> meterReadings) {
        this.customerId = customerId;
        this.meterReadings = meterReadings;
    }

    public int getCustomerId() {
        return customerId;
    }

    public List<Double> getMeterReadings() {
        return meterReadings;
    }
}
