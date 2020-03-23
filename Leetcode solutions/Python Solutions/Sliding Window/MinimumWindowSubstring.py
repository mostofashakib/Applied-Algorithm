"""
LeetCode Problem: 509. Fibonacci number
Link: https://leetcode.com/problems/fibonacci-number/
Language: Python
Written by: Mostofa Adib Shakib

Intuition:
Let us call a window desirable if it has all the characters from TT.
We can use a simple sliding window approach to solve this problem.
In any sliding window based problem we have two pointers. One rightright pointer whose job is to expand the current window and then we have the leftleft pointer whose job is to contract a given window.
At any point in time only one of these pointers move and the other one remains fixed.
The solution is pretty intuitive. We keep expanding the window by moving the right pointer.
When the window has all the desired characters, we contract (if possible) and save the smallest window till now.
The answer is the smallest desirable window.

Algorithm:
1) We start with two pointers, leftleft and rightright initially pointing to the first element of the string SS.
2) We use the rightright pointer to expand the window until we get a desirable window i.e. a window that contains all of the characters of TT.
3) Once we have a window with all the characters, we can move the left pointer ahead one by one. If the window is still a desirable one we keep on updating the minimum window size.
4) If the window is not desirable any more, we repeat step2 onwards.

Time Complexity: O(∣S∣+∣T∣) where |S| and |T| represent the lengths of strings SS and TT
Space Complexity: O(∣S∣+∣T∣) where |S| and |T| represent the lengths of strings SS and TT
"""

class Solution:
    def minWindow(self, string: str, pat: str) -> str:
        no_of_chars = 256
        len1 = len(string)  
        len2 = len(pat)  

        # check if string's length is less than pattern's  
        # length. If yes then no such window can exist  
        if len1 < len2:  

            print("No such window exists")  
            return ""  

        hash_pat = [0] * no_of_chars 
        hash_str = [0] * no_of_chars  

        # store occurrence ofs characters of pattern  
        for i in range(0, len2):  
            hash_pat[ord(pat[i])] += 1

        start, start_index, min_len = 0, -1, float('inf')  

        # start traversing the string  
        count = 0 # count of characters  
        for j in range(0, len1):  

            # count occurrence of characters of string  
            hash_str[ord(string[j])] += 1

            # If string's char matches with  
            # pattern's char then increment count  
            if (hash_pat[ord(string[j])] != 0 and
                hash_str[ord(string[j])] <= 
                hash_pat[ord(string[j])]):  
                count += 1

            # if all the characters are matched  
            if count == len2:  

                # Try to minimize the window i.e., check if  
                # any character is occurring more no. of times  
                # than its occurrence in pattern, if yes  
                # then remove it from starting and also remove  
                # the useless characters.  
                while (hash_str[ord(string[start])] >  
                       hash_pat[ord(string[start])] or
                       hash_pat[ord(string[start])] == 0):  

                    if (hash_str[ord(string[start])] >  
                        hash_pat[ord(string[start])]):  
                        hash_str[ord(string[start])] -= 1
                    start += 1

                # update window size  
                len_window = j - start + 1
                if min_len > len_window:  

                    min_len = len_window  
                    start_index = start  

        # If no window found  
        if start_index == -1: 
            return ""  

        # Return substring starting from  
        # start_index and length min_len  
        return string[start_index : start_index + min_len]
             