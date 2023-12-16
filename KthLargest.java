import java.util.*;

public class KthLargest {
    PriorityQueue<Integer> heap;
    int k;
    
    public KthLargest(int k, int[] nums) {
        this.k = k;
        this.heap = new PriorityQueue<Integer>();
        for (int num : nums) {
            this.add(num);
        }
    }
    
    public int add(int val) {
        if (heap.size() < k) {
            heap.offer(val);
        } else if (val > heap.peek()){
            heap.poll();
            heap.add(val); //note: offer and add do same thing, just that add throws exeception if no more space, offer just returns false
        }

        return heap.peek();
    }
}
