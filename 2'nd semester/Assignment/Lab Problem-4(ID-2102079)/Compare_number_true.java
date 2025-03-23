 
package cscorner.lab_problem4;
 import java.util.Scanner;
public class Compare_number_true {
    public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
        System.out.println("Enter first number : ");
        int a = sc.nextInt();
        System.out.println("Enter second number : ");
        int b = sc.nextInt();
        System.out.println("Enter third number : ");
        int c = sc.nextInt();
        if(a<b)
        {
            if(b<c)
            {
                System.out.println("The result is : True");
            }
            else
            {
                System.out.println("The result is : False");
            }
        }
        else
        {
            System.out.println("The result is : False");
        }
    
}
}
