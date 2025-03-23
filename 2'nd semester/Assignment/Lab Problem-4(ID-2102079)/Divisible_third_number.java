 
package cscorner.lab_problem4;
 
public class Divisible_third_number {
    public static void main(String[] args) {
         int a=5;
         int b=20;
         int p=3;
         if(a%p==0)
         {
             System.out.println(b/p-a/p+1);
         }
         else
         {
             System.out.println(b/p-a/p);
         }
    }
}
