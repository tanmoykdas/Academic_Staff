 
package cscorner.lab_problem4;
 import java.util.Scanner;
public class Convert_String_to_Integer {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the string number : ");
       String s = sc.nextLine();
       int answer = Integer.parseInt(s);
        System.out.printf("The integer value is : %d" , answer); 
        System.out.println("\n");
    }
    
}
