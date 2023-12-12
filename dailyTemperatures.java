import java.util.*;

public class dailyTemperatures {
    public static int[] dailyTemperaturesMet(int[] temperatures) {
        int [] ans = new int[temperatures.length];
        Stack<Integer> stack = new Stack<Integer>();

        for (int curr = 0; curr < temperatures.length; curr++) {
                while (!stack.isEmpty() && temperatures[curr] > temperatures[stack.peek()]) {
                    int prev = stack.pop();
                    ans[prev] = curr - prev;
                }

                stack.push(curr);
        }

        return ans;
    }
}
