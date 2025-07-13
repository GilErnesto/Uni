package aula02;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;

public class Ex4 {
    public static void main(String[] args) {
        ArrayList<Double> numbers = new ArrayList<Double>();
        //scanner
        Scanner sc = new Scanner(System.in);
        //loop
        while(true){
            System.out.print("Número: ");
            double num = sc.nextDouble();
            //condicao
            if(numbers.isEmpty()){
                numbers.add(num);
            } else if(num != numbers.get(0)){
                numbers.add(num);
            } else {
                sc.close();
                break;
            }
            
        }
        Collections.sort(numbers);
        //exercicio
        int size = numbers.size();
        double min = numbers.get(0);
        double max = numbers.get(size-1);
        double sum = 0;
        for(Double i : numbers){
            sum += i;
        }
        double media = sum / size;
        System.out.println("Mínimo: " + min);
        System.out.println("Máximo: " + max);
        System.out.println("Média: " + media);
        System.out.print("Os número acima da média são: ");
        for (Double i : numbers){
            if(i > media){
                System.out.print(i + " ");
            }
        }
    }
}
