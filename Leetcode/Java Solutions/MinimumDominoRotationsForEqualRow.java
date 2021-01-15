/*
LeetCode Problem: 1007. Minimum Domino Rotations For Equal Row
Link: https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/
Written by: Mostofa Adib Shakib
Language: Java
Time Complexity: O(n)
Space Complexity: O(n)
*/

class Solution {
    public int minimumDominoSwaps(int target, int[] A, int[] B) {
        int minSwaps = 0;
        
        for (int i = 0; i < A.length; i++) {
            if (A[i] != target && B[i] != target) {
                return Integer.MAX_VALUE;
            }
            else if (A[i] != target) {
                minSwaps++;
            }
        }
        return minSwaps;
    }
    
    public int minDominoRotations(int[] A, int[] B) {
        int minimumSwaps = Integer.MAX_VALUE;
        
        minimumSwaps = Math.min(minimumSwaps, minimumDominoSwaps(A[0], A, B));
        minimumSwaps = Math.min(minimumSwaps, minimumDominoSwaps(B[0], A, B));
        minimumSwaps = Math.min(minimumSwaps, minimumDominoSwaps(A[0], B, A));
        minimumSwaps = Math.min(minimumSwaps, minimumDominoSwaps(B[0], B, A));
        
        return minimumSwaps != Integer.MAX_VALUE ? minimumSwaps:-1;
    }
}