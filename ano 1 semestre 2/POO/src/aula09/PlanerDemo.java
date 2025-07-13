package aula09;

public class PlanerDemo {
    public static void main(String[] args) {
            PlaneManager manager = new PlaneManager();

            // Adicionar aviões
            manager.addPlane(new CommercialPlane("C1", "Airbus", "A320", 2016, 180, 850, 800));
            manager.addPlane(new CommercialPlane("C2", "Boeing", "737", 2018, 160, 840, 840));
            manager.addPlane(new MilitaryPlane("M1", "Lockheed", "F-22", 2020, 1, 2400, 120));
            manager.addPlane(new MilitaryPlane("M2", "Dassault", "Rafale", 2019, 1, 1912, 80));

            System.out.println("🛫 Frota inicial:");
            manager.printAllPlanes();

            // Remover avião
            System.out.println("\n❌ Remover avião com ID C2");
            manager.removePlane("C2");

            // Procurar por avião
            System.out.println("\n🔎 Procurar avião com ID M1:");
            Plane p = manager.searchPlane("M1");
            System.out.println(p != null ? p : "Avião não encontrado");

            // Listar por tipo
            System.out.println("\n📋 Lista de aviões comerciais:");
            for (Plane plane : manager.getCommercialPlanes()) {
                System.out.println(plane);
            }

            System.out.println("\n📋 Lista de aviões militares:");
            for (Plane plane : manager.getMilitaryPlanes()) {
                System.out.println(plane);
}

            // Avião mais rápido
            System.out.println("\n🚀 Avião mais rápido da frota:");
            Plane fastest = manager.getFastestPlane();
            System.out.println(fastest != null ? fastest : "Frota vazia");
        }
}

