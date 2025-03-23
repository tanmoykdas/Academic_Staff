/* Write a Java method that accepts three integers and checks whether they are consecutive or not. Returns true or false.

Expected Output:

Input the first number:  15
Input the second number:  16
Input the third number:  17
Check whether the three said numbers are consecutive or not!true */

import java.util.Scanner;
    public class problem18  
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
            System.out.print("Check whether the three said numbers are consecutive or not!");
            System.out.println(test(x,y,z));
            }
    
     public static boolean test(int x, int y, int z){
        int max_num = Math.max(x, Math.max(y, z));
        int min_num = Math.min(x, Math.min(y, z));
        int middle_num = x+y+z - max_num - min_num;
        return (max_num - middle_num) == 1 && (middle_num - min_num == 1);
      }
    } 
     

