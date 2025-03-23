 
package cscorner.lab_problem4;

 import java.util.Scanner;
public class Equal_smallest_value {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        System.out.println("ENter the first value : ");
        int num1 = sc.nextInt();
        System.out.println("Enter the second value: ");
        int num2 = sc.nextInt();
        
    
        if(num1==num2)
        {
             System.out.println("answer : 0");
        }
        else if(num1%6==num2%6)
        {
            if(num1<num2)
            {
                System.out.println(num2);
            }
            else
            {
                System.out.println(num1);
            }
        }
        else 
        {
            if(num1>num2)
        {
            System.out.println(num1);
        }
            else
            {
                System.out.println(num2);
            }
        }
        /*
       public static int answer(int num1, int num2)
     {  
	if(num1 == num2)
		return 0;
	    if(num1 % 6 == num2 % 6)
		    return (num1 < num2) ? num1 : num2;
	    return (num1 > num2) ? num1 : num2;
        
    }*/
    
    }
}
    

