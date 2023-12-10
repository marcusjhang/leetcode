public class productExceptSelf {
    public static int[] productExceptSelf(int[] nums) {
        /** 
        int [] result = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            int pdt = 1;
            for (int j = 0; j < nums.length; j++) {
                if (j == i) {
                    continue;
                } else {
                    pdt *= nums[j];
                }
            }
            result[i] = pdt;
        }
        return result;
        **/ // O(n^2)

        int[] result = new int[nums.length];
        int left = 1;
        int right = 1;
        for (int i = 0; i < nums.length; i++) {
            result[i] = left;
            left *= nums[i];
        } 

        for (int i = nums.length - 1; i >= 0; i--) {
            result[i] *= right;
            right *= nums[i];
        }

        return result;
    }

    public static void main(String[] args) {
        int [] nums = {1,2,3,4};
        System.out.println(productExceptSelf(nums));
    }
}
