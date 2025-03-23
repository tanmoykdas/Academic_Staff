public class Problems11 {
    public static void main(String[] args) {
        boolean num1_b = Double.isFinite(11.0/0);
        System.out.println("Is the double number(11/0) finite? :" + num1_b );
        double num2 = Double.MAX_VALUE * 0;
        boolean num2_b = Double.isFinite(num2);
        System.out.println("Is the number "+ num2+" finite? : "+num2_b);
        double num3 = Double.POSITIVE_INFINITY * 0;
        boolean num3_b = Double.isFinite(num3);
        System.out.println("Is the number "+ num3+" finite? : "+num3_b);

        float num_1 = 33.4f * 0;
        boolean num_1b = Float.isFinite(num_1);
        System.out.println("Is the float number "+ num_1+" finite? : "+num_1b);
        float num_2 = num_1/0.0f;
        boolean num_2b = Float.isFinite(num_2);
        System.out.println("Is the float number "+ num_2+" finite? : "+num_2b);

    }
}
