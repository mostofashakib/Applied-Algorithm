/*
LeetCode Problem: . Two Sum
Link: https://leetcode.com/problems/two-sum/
Written by: Mostofa Adib Shakib
Language: Java

This solution uses dictionary and set to find a easy and efficient solution.

*/

class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] arr = nums.clone();
        Arrays.sort(arr);
        int first = 0;
        int last = nums.length - 1;
        int[] res = new int[2];
        boolean f1 = false;
        boolean f2 = false;

        while (arr[first] + arr[last] != target) {
            if (arr[first] + arr[last] > target) {
                last--;
            }
            else if (arr[first] + arr[last] < target) {
                first++;
            }
        }

        for (int i = 0; i < nums.length; i++) {
            if(nums[i] == arr[first] && !f1){
                res[0] = i;
                f1 = true;
            }
            else if(nums[i] == arr[last] && !f2){
                res[1] = i;
                f2 = true;
            }
        }
        return res;
        
    }
}