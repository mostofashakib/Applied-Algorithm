/*
LeetCode Problem: 1143. Longest Common Subsequence
Link: https://leetcode.com/problems/longest-common-subsequence/
Written by: Mostofa Adib Shakib
Language: Java
Time Complexity: O(n*m)
Space Complexity: O(n*m)
*/

class Solution {
    public int[][] dp;
    
    public int longestCommonSubsequence(String text1, String text2) {
        int text1_length = text1.length();    // column
        int text2_length = text2.length();    // row
        
        dp = new int[text2_length + 1][text1_length + 1];
        
        for (int i = 0; i < text2_length+1; i++) {
            for (int j = 0; j < text1_length+1; j++) {
                if (i == 0 || j == 0){
                    dp[i][j] = 0;
                }
                else if ( text2.charAt(i-1) == text1.charAt(j-1)  ){
                    dp[i][j] = dp[i-1][j-1] + 1;
                } else{
                    dp[i][j] = Math.max(dp[i][j-1], dp[i-1][j]) ;
                }
            }
        }
        return dp[text2_length][text1_length];
    }
}