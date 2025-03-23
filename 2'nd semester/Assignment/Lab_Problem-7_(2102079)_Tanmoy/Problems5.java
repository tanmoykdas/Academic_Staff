import java.util.Scanner;

public class Problems5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the time zone offset in GMT: ");
        int timeZoneChange = sc.nextInt();
        long totalTime_In_Milli_Second = System.currentTimeMillis();
        long totalSeconds = totalTime_In_Milli_Second/1000;
        long totalMinutes = totalSeconds/60;
        long currentSecond = totalSeconds%60;
        long currentMinutes = totalMinutes % 60;
        long totalHour = totalMinutes /60;
        long currentHour = (totalHour + timeZoneChange) % 24;
        System.out.println("Current time is: "+ currentHour+ ":"+currentMinutes+":"+ currentSecond);

    }
}
