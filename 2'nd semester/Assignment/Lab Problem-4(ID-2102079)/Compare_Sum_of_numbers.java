 
package cscorner.lab_problem4;
import java.util.Scanner;
public class Compare_Sum_of_numbers {
     public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Input the first number : ");
        int a = sc.nextInt();  
		System.out.print("Input the second number: ");
		int b = sc.nextInt(); 
		System.out.print("Input the third number : ");
        int c = sc.nextInt(); 
        System.out.print("The result is: "+sumoftwo(a, b, c));
		System.out.print("\n");
    }
    
    public static boolean sumoftwo(int x, int y, int z)
    {	
         return ((x + y) == z || (y + z) == x || (z + x) == y);	
	}
}

 