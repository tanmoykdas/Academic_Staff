import java.util.Scanner;

public class Problems3 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter an integer between 0 to 1000: ");
        int num = input.nextInt();
        int sumDigit =0;
        while (num>0)
        {
            sumDigit += num%10;
            num /= 10;
        }
        System.out.println("Sum of the digit is : "+ sumDigit);

    }
}
