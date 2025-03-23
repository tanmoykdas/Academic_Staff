/* Write a Java method that checks whether all the characters in a given string are vowels (a, e,i,o,u) or not. Return true if each character in the string is a vowel, otherwise return false.

Expected Output:

Input a string:  AIEEE
Check all the characters of the said string are vowels or not!
true */

import java.util.Scanner;
public class problem23 
{
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.print("Input a string: ");
    String str = sc.nextLine();
    System.out.print("Check all the characters of the said string are vowels or not!\n");
    System.out.print(test(str));
  }

  public static boolean test(String input) {
    String str_vowels = "aeiou";
    String phrase = input.toLowerCase();
    for (int i = 0; i < phrase.length(); i++) {
      if (str_vowels.indexOf(phrase.charAt(i)) == -1)
        return false;
    }
    return true;
  }
}

