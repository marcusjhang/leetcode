import java.util.HashSet;

public class containsDuplicate {
    public static boolean containsDuplicateMethod(int[] nums) {
        HashSet<Integer> seen = new HashSet<Integer>();
        for (int i : nums) {
            if (seen.contains(i)) {
                return true;
            } else {
                seen.add(i);
                continue;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        int [] nums = {1,2,3,1};
        System.out.println(containsDuplicateMethod(nums));
    }
}