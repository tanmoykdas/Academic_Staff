public class sumOfArray {
    public static void main(String[] args) {      
        int my_array[] = {1,3,5,7,9,11,13,15,17,19};
        int sum = 0;
        for (int i : my_array)
            sum += i;
        System.out.println("The sum is "+sum);
    }
}
