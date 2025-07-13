package aula06;
import java.util.ArrayList;
import java.util.List;

public class Conjunto {
    public static void main(String[] args) {
        Conjunto c1 = new Conjunto();
        c1.insert(4); c1.insert(7); c1.insert(6); c1.insert(5);
        Conjunto c2 = new Conjunto();
        int[] test = { 7, 3, 2, 5, 4, 6, 7};
        for (int el : test) c2.insert(el);
        c2.remove(3); c2.remove(5); c2.remove(6);
        System.out.println(c1);
        System.out.println(c2);
        System.out.println("Número de elementos em c1: " + c1.size());
        System.out.println("Número de elementos em c2: " + c2.size());
        System.out.println("c1 contém 6?: " + ((c1.contains(6) ? "sim" : "não")));
        System.out.println("c2 contém 6?: " + ((c2.contains(6) ? "sim" : "não")));
        System.out.println("União:" + c1.unir(c2));
        System.out.println("Interseção:" + c1.interset(c2));
        System.out.println("Diferença:" + c1.subtrair(c2));
        c1.empty();
        System.out.println("c1:" + c1);
 }

    List<Integer> numeros = new ArrayList<>();
    
    public void insert(int n){
        if(contains(n)){System.out.println("Este número já está no Conjunto.");} else {numeros.add(n);}
    }

    public boolean contains(int n){
        if (numeros.isEmpty()){
            return false;
        } else if (numeros.contains(n)){
                return true;
            }
        return false;
    }

    public void remove(int n){
        if(contains(n)){numeros.remove(Integer.valueOf(n));} else {System.out.println("Este número não exite no Conjunto.");}
    }

    public void empty(){
        numeros.clear();
    }

    public String toString(){
        return numeros.toString();
    }

    public int size(){
        return numeros.size();
    }

    public Conjunto unir(Conjunto add) {
        Conjunto uniao = new Conjunto();

        for (int obj : this.numeros) {
            uniao.insert(obj); // Adiciona todos de this
        }

        for (int obj : add.numeros) {
            uniao.insert(obj); // Adiciona todos de add (sem repetir, porque insert já verifica)
        }

        return uniao;
}


    public Conjunto subtrair(Conjunto dif){
        Conjunto diferenca = new Conjunto();
        for(int obj : this.numeros){
            if(!dif.numeros.contains(obj)){diferenca.insert(obj);}
        }
        return diferenca;
    }

    public Conjunto interset(Conjunto inter){
        Conjunto intersecao = new Conjunto();
        for(int obj : inter.numeros){
            if(numeros.contains(obj)){intersecao.insert(obj);}
        }
        return intersecao;
    }
}

