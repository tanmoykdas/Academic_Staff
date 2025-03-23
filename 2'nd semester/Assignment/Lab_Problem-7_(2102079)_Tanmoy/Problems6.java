import java.util.Scanner;

public class Problems6 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the weight in pounds: ");
        double weight = input.nextDouble();
        System.out.print("Enter the height in inch: ");
        double height = input.nextDouble();
        double BMI = (weight * 0.454 )/(height * height * 0.0254 * 0.0254);
        System.out.println("BMI is : "+BMI );
    }
}
