/*
LeetCode Problem 1239. Maximum Length of a Concatenated String with Unique Characters
Link: https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
Written by: Mostofa Adib Shakib
Language: C++
*/


class Solution {
    
public:
    int ans = 0;
    
    bool isUnique(string str) {
        vector<int> hashSet = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
        
        for (int i = 0; i < str.length(); i++) {
            if (hashSet[str[i] - 'a'] > 0 )  {
                return false;
            }
            else {
                hashSet[str[i] - 'a']++;
            }
        }
        
        return true;
    }
    
    int getMaximum(int x, int y) {
        return (x > y) ? x : y;
    }
    
    void generateUniqueCharacters(vector<string>& arr, string comb, int index) {
        
        if ( isUnique(comb) ) {
            ans = getMaximum(ans, comb.length());
        } 
        else {
            return;   // the current combination is not unique
        }
        
        for (int i = index; i < arr.size(); i++) {
            generateUniqueCharacters(arr, comb + arr[i], i+1);
        }
    }
    
    int maxLength(vector<string>& arr) {
        generateUniqueCharacters(arr, "", 0);
        return ans;
    }
};