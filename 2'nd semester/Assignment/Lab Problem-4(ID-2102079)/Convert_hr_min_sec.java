 
package cscorner.lab_problem4;

 import java.util.Scanner;
public class Convert_hr_min_sec {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the Second : ");
        int seconds= sc.nextInt();
         int sec = seconds % 60;
        int hr = seconds / 60;
        int min = hr % 60;
        hr = hr / 60;
        System.out.println("hour : " +hr+ "\t min :" +min+  "\tsecond :" +sec);
    }
}
