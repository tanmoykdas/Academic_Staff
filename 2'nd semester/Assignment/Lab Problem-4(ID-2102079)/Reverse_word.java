 
package cscorner.lab_problem4;

 import java.util.Scanner;
public class Reverse_word {
    public static void main(String[] args) {
             Scanner sc = new Scanner(System.in);
     System.out.print("Enter a word :  ");
	 String word = sc.nextLine();
	 word = word.trim();
	 String answer = ""; 
     char[] a=word.toCharArray();  
	 for (int i = a.length - 1; i >= 0; i--) {
			 answer += a[i];
		 }
	 System.out.println("Reverse word: "+answer.trim()); 
    }
    
}
