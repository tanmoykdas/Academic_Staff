 
package cscorner.lab_problem4;

 
public class Compute_100_Prime_number {
    public static void main(String[] args) {
       int sum=0;
       int g=0,i=2;
        while(g!=100)
       {
           int count=0;
           for(int j=2;j<=i/2;j++)
           {
               if(i%j==0)
               {
                   count++;
                   break;
               }
           }
           if(count==0)
           {
               sum+=i;
               g++;
           }
           i++;
       }
        System.out.println("sum of prime number: " +sum);
    }
}
