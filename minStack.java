import java.util.*;

public class minStack {
    Stack<Integer> stack; //for every action other than getMin
    Stack<Integer> minStack; //for getMin, keeps track of the current min val in the stack
    
    public minStack() {
        this.stack = new Stack<>();
        this.minStack = new Stack<>();
    }
    
    public void push(int val) {
        this.stack.push(val);
        
        int value = Math.min(val, minStack.isEmpty() ? val : this.minStack.peek());
        minStack.push(value);
    }
    
    public void pop() {
        this.stack.pop();
        this.minStack.pop();
    }
    
    public int top() {
        return this.stack.peek();
    }
    
    public int getMin() {
        return this.minStack.peek();
    }
}
