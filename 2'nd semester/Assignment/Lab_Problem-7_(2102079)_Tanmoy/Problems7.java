import java.util.Scanner;

public class Problems7 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the distance in meter : ");
        double distance = input.nextDouble();
        System.out.print("Enter the hour: ");
        double hour = input.nextDouble();
        System.out.print("Enter the minutes: ");
        double min = input.nextDouble();
        System.out.print("Enter the Seconds: ");
        double sec = input.nextDouble();
        double speed_m_s = distance/((hour * 3600)+(min*60)+ sec);
        double speed_km_h = (distance/1000)/(hour+(min/60)+ (sec/3600));
        double speed_miles_h = speed_km_h / 1.61;
        System.out.println("Speed in meters/ second is : "+speed_m_s);
        System.out.println("Speed in km/ h is : "+speed_km_h);
        System.out.println("Speed in miles/ h is : "+speed_miles_h);



    }
}
