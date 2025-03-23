import java.util.Scanner;

public class Problems1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the temperature in Fahrenheit : ");
        double f = sc.nextDouble();
        double c = ((f-32) * 5)/9;
        System.out.printf("After converting in Celsius the new temperature is : %.2f\n",c);
    }
}
