package project_euler.problems;

import java.util.ArrayList;

public class Problem2 {

    public static int evenFibonacciNumbers(int threshold){
        ArrayList<Integer> fibos = new ArrayList<>();
        fibos.add(1);
        fibos.add(2);
        int currentFibo = 0;
        int sumOfEven = 2;

        while (currentFibo < threshold){
            currentFibo = fibos.get(fibos.size()-1) + fibos.get(fibos.size()-2);
            fibos.add(currentFibo);
            if (currentFibo % 2 == 0 && currentFibo < threshold){
                sumOfEven += currentFibo;
            }
        }
        return sumOfEven;
    }

    public static void main(String[] args){
        System.out.println(evenFibonacciNumbers(4000000));
    }
}