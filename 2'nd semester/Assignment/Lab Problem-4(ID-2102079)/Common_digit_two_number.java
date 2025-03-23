 
package cscorner.lab_problem4;
 import java.util.Scanner;
public class Common_digit_two_number {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
         
        
        
        
        System.out.println("Enter the first number :");
        int  num1 = sc.nextInt();
        System.out.println("Enter the second number: ");
        int num2 = sc.nextInt();
        
        if((num1>=25 && num1<=75) && (num2>=25 && num2<=75))
                {
                    if((num1%10 ==num2%10))  
                    {
                        System.out.println("True");
                    }
                    else if((num1/10==num2/10))
                    {
                        System.out.println("True");
                    }
                }
        else
        {
            System.out.println("Error");
        }
        
        
    }
}
