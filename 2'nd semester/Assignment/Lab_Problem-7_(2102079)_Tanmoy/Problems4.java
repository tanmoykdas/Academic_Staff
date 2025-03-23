import java.util.Scanner;

public class Problems4 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the minutes: ");
        int min = input.nextInt();
        int year = min / (365 * 24 * 60);
        int days = (min % (365 * 24 * 60)) / (24 *60);
        System.out.println("Years : "+year );
        System.out.println("Days: "+days);
    }
}
