package aula09;

import java.util.ArrayList;

public class PlaneManager {
    private ArrayList<Plane> planes = new ArrayList<>();

    public void addPlane(Plane plane){
        planes.add(plane);
    }

    public void removePlane(String id){
        planes.removeIf(obj -> obj.getIdentificador().equals(id));
    }


    public Plane searchPlane(String id){
        for(Plane obj : planes){
            if(obj.getIdentificador().equals(id)){
                    return obj;
            }
        }
        return null;
    }

    public ArrayList<Plane> getCommercialPlanes(){
    ArrayList<Plane> comerciais = new ArrayList<>();
    for(Plane obj : planes){
        if(obj.getPlaneType().equalsIgnoreCase("Comercial")){
            comerciais.add(obj);
        }
    }
    return comerciais;
}

public ArrayList<Plane> getMilitaryPlanes(){
    ArrayList<Plane> militares = new ArrayList<>();
    for(Plane obj : planes){
        if(obj.getPlaneType().equalsIgnoreCase("Militar")){
            militares.add(obj);
        }
    }
    return militares;
}


    public void printAllPlanes(){
        for(Plane obj : planes){
            System.out.println(obj);
        }
    }

    public Plane getFastestPlane(){
        int maxVelocidade = 0;
        Plane planeSpeed = null;
        for(Plane obj : planes){
            int velocidade = obj.getVelocidadeMax();
            if(velocidade > maxVelocidade){ 
                maxVelocidade = velocidade; 
                planeSpeed = obj;
            }
        }
        return planeSpeed;

    }

}
