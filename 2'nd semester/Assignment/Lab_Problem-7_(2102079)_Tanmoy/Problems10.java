import java.util.Scanner;

public class Problems10 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter an Integer: ");
        int n = input.nextInt();
        String str = Integer.toString(n);
        int len = str.length();
        int[] array = new int[len];
        for(int i=0;i<len;i++)
        {
            array[i] = Character.getNumericValue(str.charAt(i));
        }
        for(int i=0;i<len;i++)
        {
            System.out.print(array[i]+" ");
        }
        input.close();
    }
}
