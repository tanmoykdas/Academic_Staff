 
package cscorner.lab_problem4;

 import java.util.Scanner;
public class Less_than_Substruction_Equal20 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the first number :");
        int a = sc.nextInt();
        System.out.println("Enter the second number :");
        int b =sc.nextInt();
        System.out.println("Enter the third number : ");
        int c= sc.nextInt();
        System.out.println(Math.abs(a-b)>=20 || Math.abs(b-c)>=20||Math.abs(c-a)>=20);
                
    }
    
}
