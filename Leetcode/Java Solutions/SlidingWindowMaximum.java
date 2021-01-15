/*
LeetCode Problem: 239. Sliding Window Maximum
Link: https://leetcode.com/problems/sliding-window-maximum/
Written by: Mostofa Adib Shakib
Language: Java
Time Complexity: O(n)
Space Complexity: O(n)
*/

class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        Deque<Integer> deque = new ArrayDeque<Integer>();
        int length = nums.length;
        int [] result = new int[length - k +1];
        int index = 0;
        
        for (int i = 0; i < length; i++) {
            if (!deque.isEmpty() && i - deque.peekFirst() == k) {
                deque.removeFirst();
            }
            
            while (!deque.isEmpty() && nums[deque.peekLast()] < nums[i]) {
                deque.removeLast();
            }
            
            deque.offer(i);
            
            if (i+1 >= k) {
                result[index] = nums[deque.peekFirst()];
                index++;
            }
        }
        
        return result;
    }
}