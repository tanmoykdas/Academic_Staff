public class moveArrayElementsToTheEnd {
    public static void main(String[] args) throws Exception {
        int array_nums[] = {0, 0, 1, 0, 3, 0, 5, 0, 6};
        int i = 0;

        System.out.println("\nOriginal array: ");
        for (int n : array_nums)
            System.out.print(n+"  ");
        for (int j = 0,l = array_nums.length;j < l;) {
            if (array_nums[j] == 0)
                j++;
            else {
                int temp = array_nums[i];
                array_nums[i] = array_nums[j];
                array_nums[j] = temp;
                i++;
                j++;
            }
        }
        while (i < array_nums.length)
        array_nums[i++] = 0;
    System.out.println("\nAfter moving 0's to the end of the array: ");
    for (int n : array_nums)
        System.out.print(n+"  ");
    System.out.print("\n");
}
}
