 
package cscorner.lab_problem4;
import java.util.Scanner;
 
public class Penultimate_word {
    public static void main(String[] args) {
            Scanner sc = new Scanner(System.in);
     System.out.print("Input a Sentence: ");
	 String lenth = sc.nextLine();
	 String[] words = lenth.split("[ ]+");
	 System.out.println("Penultimate word: "+words[words.length - 2]);
	 }			
}
    
