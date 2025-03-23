import java.util.Scanner;

public class Problems13 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.print("Enter the first integer: ");
        int a = in.nextInt();
        System.out.print("Enter the Second integer: ");
        int b = in.nextInt();
        System.out.println("The result of Floor divisional using '/' is : "+(a/b));
        System.out.println("The result of Floor divisional using floorDiv() is : "+Math.floorDiv(a,b));
        System.out.println("The result of Floor modulus using '%' is : "+(a%b));
        System.out.println("The result of Floor modulus using floorMod() is : "+Math.floorMod(a,b));



    }
}
