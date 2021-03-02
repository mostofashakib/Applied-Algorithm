/*
LeetCode Problem: 1297. Maximum Number of Occurrences of a Substring
Link: https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/
Language: Python
Written by: Mostofa Adib Shakib
*/

// Brute Force Solution
// Time Complexity: O(n*m)
// Space Complexity: O(n)

class Solution {
public:
    int maxFreq(string s, int maxLetters, int minSize, int maxSize) {
        map<string, int> hashmap;
        int length = s.length();
        string subString;
        int uniqueSubStringLength;
        int maximumValue = 0;
        
        for (int size = minSize; size <= maxSize; size++) {
            for (int i = 0; i <= length-size; i++ ) {                
                subString = s.substr(i, size);
                uniqueSubStringLength = set(subString.begin(), subString.end()).size();
                                
                if ( uniqueSubStringLength <= maxLetters) {
                    
                    if ( hashmap.find(subString) == hashmap.end() ) {
                        hashmap.insert({subString, 1 });
                    }
                    else {
                        hashmap[subString]++;
                    }
                    
                    if (hashmap[subString] > maximumValue) {
                        maximumValue = hashmap[subString];
                    }
                }
            }
        }
        return maximumValue;
    }
};