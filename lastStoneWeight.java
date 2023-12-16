import java.util.PriorityQueue;

public class lastStoneWeight {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        for (int stone : stones) {
            heap.add(-stone); //if want to order priority queue in opposite direction, just negative everything
        }
        while (heap.size() > 1) {
            int first = -heap.poll();
            int second = -heap.poll();
            if (first == second) {
                continue;
            } else if (first < second) {
                heap.add(-(second-first));
            } else {
                heap.add(-(first-second));
            }
        }
        return -heap.peek();
    }
}
