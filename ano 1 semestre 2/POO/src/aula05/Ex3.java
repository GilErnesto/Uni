package aula05;

import java.util.ArrayList;
import java.util.List;

class DateYMD {
    private int day;
    private int month;
    private int year;

    public DateYMD(int day, int month, int year) {
        this.day = day;
        this.month = month;
        this.year = year;
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

    @Override
    public String toString() {
        return String.format("%d-%02d-%02d", year, month, day);
    }
}

class Property {
    private static int nextId = 1000;
    private int id;
    private String location;
    private int rooms;
    private int price;
    private boolean available;
    private DateYMD auctionStart;
    private DateYMD auctionEnd;

    public Property(String location, int rooms, int price) {
        this.id = nextId++;
        this.location = location;
        this.rooms = rooms;
        this.price = price;
        this.available = true;
        this.auctionStart = null;
        this.auctionEnd = null;
    }

    public int getId() {
        return id;
    }

    public boolean isAvailable() {
        return available;
    }

    public void sell() {
        this.available = false;
    }

    public void setAuction(DateYMD start, int days) {
        this.auctionStart = start;
        this.auctionEnd = new DateYMD(start.getDay() + days, start.getMonth(), start.getYear());
    }

    @Override
    public String toString() {
        String result = String.format("Imóvel: %d; quartos: %d; localidade: %s; preço: %d; disponível: %s",
                id, rooms, location, price, available ? "sim" : "não");
        if (auctionStart != null && auctionEnd != null) {
            result += String.format("; leilão %s : %s", auctionStart, auctionEnd);
        }
        return result;
    }
}

class RealEstate {
    private List<Property> properties;

    public RealEstate() {
        this.properties = new ArrayList<>();
    }

    public void newProperty(String location, int rooms, int price) {
        properties.add(new Property(location, rooms, price));
    }

    public void sell(int id) {
        Property property = findPropertyById(id);
        if (property != null) {
            if (property.isAvailable()) {
                property.sell();
                System.out.println("Imóvel " + id + " vendido.");
            } else {
                System.out.println("Imóvel " + id + " não está disponível.");
            }
        } else {
            System.out.println("Imóvel " + id + " não existe.");
        }
    }

    public void setAuction(int id, DateYMD start, int days) {
        Property property = findPropertyById(id);
        if (property != null) {
            if (property.isAvailable()) {
                property.setAuction(start, days);
            } else {
                System.out.println("Imóvel " + id + " não está disponível.");
            }
        } else {
            System.out.println("Imóvel " + id + " não existe.");
        }
    }

    private Property findPropertyById(int id) {
        for (Property property : properties) {
            if (property.getId() == id) {
                return property;
            }
        }
        return null;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder("Propriedades:\n");
        for (Property property : properties) {
            sb.append(property).append("\n");
        }
        return sb.toString();
    }
}

public class Ex3 {

    public static void main(String[] args) {
        RealEstate imobiliaria = new RealEstate();
        imobiliaria.newProperty("Glória", 2, 30000);
        imobiliaria.newProperty("Vera Cruz", 1, 25000);
        imobiliaria.newProperty("Santa Joana", 3, 32000);
        imobiliaria.newProperty("Aradas", 2, 24000);
        imobiliaria.newProperty("São Bernardo", 2, 20000);

        imobiliaria.sell(1001);
        imobiliaria.setAuction(1002, new DateYMD(21, 3, 2023), 4);
        imobiliaria.setAuction(1003, new DateYMD(1, 4, 2023), 3);
        imobiliaria.setAuction(1001, new DateYMD(1, 4, 2023), 4);
        imobiliaria.setAuction(1010, new DateYMD(1, 4, 2023), 4);

        System.out.println(imobiliaria);
    }
}
