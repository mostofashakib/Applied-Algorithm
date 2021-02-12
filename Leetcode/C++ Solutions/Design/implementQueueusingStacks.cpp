/*
LeetCode Problem: 232. Implement Queue using Stacks
Link: https://leetcode.com/problems/implement-queue-using-stacks/
Language: C++
Written by: Mostofa Adib Shakib

Time Complexity: Amortized O(1)
Space Complexity: O(n)
*/


class MyQueue { 
    stack<int> stack1;
    stack<int> stack2;
    
public:
    
    /** Push element x to the back of queue. */
    void push(int x) {
        if ( stack2.empty() == true) {
            stack2.push(x);
        }
        else {
            
            while (!stack2.empty()) {
                stack1.push(stack2.top());
                stack2.pop();
            }
            
            stack1.push(x);
            
            while (!stack1.empty()) {
                stack2.push(stack1.top());
                stack1.pop();
            }
        }
    }
    
    /** Removes the element from in front of queue and returns that element. */
    int pop() {
        int item = stack2.top();
        stack2.pop();
        return item;
    }
    
    /** Get the front element. */
    int peek() {
        return stack2.top();
    }
    
    /** Returns whether the queue is empty. */
    bool empty() {
        return stack2.empty() ? true: false; 
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */