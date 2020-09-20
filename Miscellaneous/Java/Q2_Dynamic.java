import java.util.*;
import java.util.HashMap;

class Main {
  static int[][] dp;
  
  static int longestCommonSubsequence(String text1, String text2) {
      int text1_length = text1.length();
      int text2_length = text2.length();
      
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

  static String PrintlongestCommonSubsequence(String text1, String text2) {
      int firstPointer = text1.length();
      int secondPointer = text2.length();
      StringBuilder ans = new StringBuilder("");

      while (firstPointer > 0 && secondPointer > 0) {
        if(dp[secondPointer][firstPointer] == dp[secondPointer][firstPointer-1]){
          firstPointer -= 1;
        } else if (dp[secondPointer][firstPointer] == dp[secondPointer-1][firstPointer]) {
          secondPointer -= 1;
        } else {
            ans.append(text2.charAt(secondPointer-1));
            firstPointer -= 1;
            secondPointer -= 1;
        } 
      }
      return ans.reverse().toString();
  }

  public static void main(String[] args) {
    String X = "MWCADBOE"; 
    String Y = "DMWCAROP";  
    int m = X.length(); 
    int LCSlength = longestCommonSubsequence(X, Y);
    String singleString = PrintlongestCommonSubsequence(X, Y);

    HashMap<String, String> wordMap = new HashMap<String, String>();
    wordMap.put("M", "monkeys");
    wordMap.put("W", "wearing");
    wordMap.put("C", "coats");
    wordMap.put("A", "are");
    wordMap.put("D", "doctors");
    wordMap.put("B", "because");
    wordMap.put("O", "of");
    wordMap.put("E", "evolution");
    wordMap.put("R", "results");
    wordMap.put("P", "eruption");

    String[] arr = singleString.split("");
    StringBuilder ans = new StringBuilder("");
 
    for (String ch : arr) {
      ans.append(wordMap.get(ch));
      ans.append(" ");
    }

    System.out.println(LCSlength);
    System.out.println(ans);

  }
}