/*Write a Java method that accepts three integers and returns true if one is the middle point between the other two integers, otherwise false.

Expected Output:

Input the first number:  2
Input the second number:  4
Input the third number:  6
Check whether the three said numbers has a midpoint!
true */

import java.util.Scanner;
    public class problem19
{ 
     public static void main(String[] args)
        {
            Scanner in = new Scanner(System.in);
            System.out.print("Input the first number: ");
            int x = in.nextInt();
            System.out.print("Input the second number: ");
            int y = in.nextInt();
            System.out.print("Input the third number: ");
            int z = in.nextInt();
            System.out.print("Check whether the three said numbers has a midpoint!\n");
            System.out.print(test(x,y,z));
            }
    
     public static boolean test(int x, int y, int z){
        int max = Math.max(x, Math.max(y,z));
        int min = Math.min(x, Math.min(y,z));
        double mid_point1 = (max + min) / 2.0;
        int mid_point2 = x + y + z - max - min;
        return (mid_point1 == mid_point2);
      }
}
      

