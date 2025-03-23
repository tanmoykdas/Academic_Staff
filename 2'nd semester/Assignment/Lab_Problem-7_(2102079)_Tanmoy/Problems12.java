public class Problems12 {
    public static void main(String[] args) {
        int a = -100, b = 100;
        System.out.println("Given numbers are "+ a+" "+b);
        int compare_sign = Integer.compare(a,b);
        int compare_unsigned = Integer.compareUnsigned(a,b);
        System.out.println("Result of comparing two signed number : "+ compare_sign);
        System.out.println("Result of comparing two unsigned number : "+compare_unsigned);
    }
}
