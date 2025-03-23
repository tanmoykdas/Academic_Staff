 
package cscorner.lab_problem4;

 import java.util.Scanner;
public class Capitalize_First_letter {
    public static void main(String[] args) {
        	 Scanner in = new Scanner(System.in);
     System.out.print("Input a Sentence: ");
	 String lenth = in.nextLine();
	 String upper_case_lenth = ""; 
       Scanner lineScan = new Scanner(lenth); 
         while(lineScan.hasNext()) {
             String word = lineScan.next(); 
             upper_case_lenth += Character.toUpperCase(word.charAt(0)) + word.substring(1) + " "; 
         }
      System.out.println(upper_case_lenth.trim());
    }
    
}
