import java.util.ArrayList;
import java.util.List;

public class targetValue {
    public static void main(String[] args) {
        int input[] = {1, -2, 0, 5, -1, -4};
        int target = 2;

        targetValue r = new targetValue();

        System.out.println(r.threeSum(input, target));
    }

    public List<List<Integer>> threeSum(int[] nums, int target) {
        List<List<Integer>> my_List = new ArrayList<List<Integer>>();

        for (int i = 0;i < nums.length;i++) {
            for (int j = i;j < nums.length;j++) {
                for (int k = j;k < nums.length;k++) {
                    if (i != j && j != k && i != k && (nums[i] + nums[j] + nums[k] == target)) {
                        List<Integer> inner_List = new ArrayList<Integer>(3);
                        inner_List.add(nums[i]);
                        inner_List.add(nums[j]);
                        inner_List.add(nums[k]);
                        my_List.add(inner_List);
                    }
                }
            }
        }

        // Return the List of triplets that satisfy the condition.
        return my_List;
    }
}
