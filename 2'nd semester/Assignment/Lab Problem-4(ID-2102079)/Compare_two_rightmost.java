 
package cscorner.lab_problem4;

 import java.util.Scanner;
public class Compare_two_rightmost {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the first number : ");
        int a = sc.nextInt();
        System.out.println("Enter the Second number : ");
        int b = sc.nextInt();
        System.out.println("Enter the third number : ");
        int c = sc.nextInt();
        
        if(a%10==b%10 || b%10==c%10 || c%10==a%10)
        {
            System.out.println("The result is : True");
        }
        else
        {
            System.out.println("The result is : False");
        }
    }
    
}
