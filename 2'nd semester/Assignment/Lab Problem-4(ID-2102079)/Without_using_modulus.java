 
package cscorner.lab_problem4;

 import java.util.Scanner;
public class Without_using_modulus {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the first number :");
        int num1 = sc.nextInt();
        System.out.println("Enter the second number : ");
        int num2 = sc.nextInt();
        int result=0;
        for(int i=1;i<=num1;i++)
        {
            if(num2*i<=num1)
            {
                result=(num1-(num2*i));
            }
        }
        System.out.println("result :" +result);
    }
}
