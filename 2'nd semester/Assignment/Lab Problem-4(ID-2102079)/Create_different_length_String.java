 
package cscorner.lab_problem4;

 
public class Create_different_length_String {
    public static void main(String[] args) {
        String str1="Python";
        String str2="Tutorial";
       // System.out.println(str1.substring(0, 6)+str2+str1.substring(0, 6));
       if(str1.length()>=str2.length())
       {
           System.out.println(str2+str1+str2);
       }
       else
       {
           System.out.println(str1+str2+str1);
       }
    }
    
}
