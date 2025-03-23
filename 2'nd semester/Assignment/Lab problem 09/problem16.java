 /*Write a Java method to find all twin prime numbers less than 100.

Expected Output:

(3, 5)                                                   
(5, 7)                                                   
(11, 13)                                                 
(17, 19)                                                 
(29, 31)                                                 
(41, 43)                                                 
(59, 61)                                                 
(71, 73)  */

 import java.util.Scanner;
    public class problem16  
{
     
     public static void main(String[] args) 
     {
    
            for (int i = 2; i < 100; i++) {
    
                if (is_Prime(i) && is_Prime(i + 2)) {
                    System.out.printf("(%d, %d)\n", i, i + 2);
                }
            }
        }
    
        public static boolean is_Prime(long n) {
    
            if (n < 2) return false;
    
            for (int i = 2; i <= n / 2; i++) {
    
                if (n % i == 0) return false;
            }
            return true;
        }
    
}
      

