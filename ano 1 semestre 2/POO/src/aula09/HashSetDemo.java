package aula09;

import java.util.HashSet;
import java.util.Set;
import java.util.Iterator;

public class HashSetDemo {

    public static void main(String[] args){
        Set<Pessoa> c3 = new HashSet<>();

        c3.add(new Pessoa("Alice", 30));
        c3.add(new Pessoa("Bob", 25));
        c3.add(new Pessoa("Carlos", 28));
        c3.add(new Pessoa("Diana", 22));
        c3.add(new Pessoa("Eva", 35));

        boolean added = c3.add(new Pessoa("Alice", 30)); // é duplicado, logo nao vai entrar no hashset
        if (!added) {
            System.out.println("O elemento duplicado 'Alice, 30' não foi adicionado.");
        }
        
        System.out.println("Elementos no HashSet:");
        Iterator<Pessoa> iterator = c3.iterator();
        while (iterator.hasNext()) {
            System.out.println(iterator.next());
        }
    }
}
