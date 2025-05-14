package project_euler.problems;

public class Problem1{

    public static int sumOfAllMultiples(int end, int[] numbers){
        int sum = 0;
        for(int i = 0; i < end; i++){
            for (int number : numbers) {
                if (i % number == 0) {
                    sum += i;
                    break;
                }
            }
        }
        return sum;
    }

    public static void main(String[] args){
        int[] numbers = {3, 5};

        int solution = sumOfAllMultiples(1000, numbers);

        System.out.println(solution);
    }
}