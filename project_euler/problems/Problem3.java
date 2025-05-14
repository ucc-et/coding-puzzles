package project_euler.problems;

public class Problem3 {

    public static double largestPrimeFactor(double num){

        int largestPrime = -1;

        while(num % 2 == 0){
            largestPrime = 2;
            num = num / 2;
        }

        for(int i = 3; i < Math.sqrt(num); i += 2){
            while(num % i == 0){
                largestPrime = i;
                num = num / i;
            }
        }

        if(num > 2) {
            return num;
        }

        return largestPrime;
    }

    public static void main(String[] args){
        System.out.println(largestPrimeFactor(600851475143.0));
    }
}