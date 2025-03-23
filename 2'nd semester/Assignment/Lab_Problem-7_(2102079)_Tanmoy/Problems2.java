import java.util.Scanner;

public class Problems2 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter the value in inch: ");
        double inch = scan.nextInt();
        double meter = 0.0254 * inch;
        System.out.printf("%f  inch is %.2f meters\n",inch,meter);
    }
}
