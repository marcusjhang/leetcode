import java.util.*;

public class topKFrequent {
    public static int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> freqMap = new HashMap<Integer, Integer>();
        for (int num: nums) {
            freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
        }
        
        // PriorityQueue has two main things, comparator in the constructor and .poll() which removes and returns the head of the queue
        PriorityQueue<Integer> pq = new PriorityQueue<>((n1, n2) -> freqMap.get(n1) - freqMap.get(n2)); // if comparator gives negative, first input is considered less and is put to the front of the PQ, vice versa for positive
        for (int n: freqMap.keySet()) {
            pq.add(n);
            if (pq.size() > k) {
                pq.poll(); // removes and returns the head of the pq
            }
        }

        int[] topK = new int[k];
        for (int i = 0; i < k; i++) {
            topK[i] = pq.poll();
        }

        return topK;
    }

    public static void main(String[] args) {
        int[] nums = {1, 1, 1, 2, 2, 3};
        int k = 2;
        int[] topK = topKFrequent(nums, k);
        System.out.println(Arrays.toString(topK));
    }
}
