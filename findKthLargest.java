import java.util.*;

public class findKthLargest {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> queue = new PriorityQueue<>();
        for (int num : nums) {
            queue.add(num);
        }

        int result = 0;
        for (int i = 0; i < nums.length-k+1; i++) {
            result = queue.poll();
        }

        return result;
    }
}
