 
package cscorner.lab_problem4;
 import java.util.Scanner;
public class Count_factor_number {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number : ");
        int num=sc.nextInt();
        int count=0;
        for(int i=1;i<=(int)Math.sqrt(num);i++)
        {
            if(num%i==0 && i*i!=num)
            {
                count+=2;
            }
            else if(i*i==num)
            {
                count++;
            }
        }
        System.out.println(count);
    }
    
}
