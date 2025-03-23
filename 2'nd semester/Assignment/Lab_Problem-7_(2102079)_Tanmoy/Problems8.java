import java.util.Scanner;

public class Problems8 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter an integer: ");
        double num = input.nextDouble();
        System.out.println("Square of the number is: "+ Math.pow(num,2));
        System.out.println("Cube of the number is: "+Math.pow(num,3));
        System.out.println("Fourth power of the number is: "+Math.pow(num,4));
    }
}
