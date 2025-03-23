import java.util.Scanner;

public class Problems9 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the first integer: ");
        int num1 = input.nextInt();
        System.out.print("Enter the second integer: ");
        int num2 = input.nextInt();
        System.out.println("Sum : "+ (num1+num2));
        System.out.println("Difference : "+(num1-num2));
        System.out.println("Product : "+(num1*num2));
        double average = (double)(num1+num2)/2;
        System.out.println("Average : "+average);
        System.out.println("Distance : "+Math.abs(num1-num2));
        System.out.println("Max : "+Math.max(num1,num2));
        System.out.println("Min : "+Math.min(num1,num2));

    }
}
