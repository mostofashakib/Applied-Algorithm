"""
LeetCode Problem: 336. Palindrome Pairs
Link: https://leetcode.com/problems/palindrome-pairs/
Language: Python
Written by: Mostofa Adib Shakib

Time complexity : O(k^2 * n)   where n be the number of words, and k be the length of the longest word.
Space complexity :  O((k + n)^2))

Algorithm:

We'll call a suffix a "valid suffix" of a word if the remainder (prefix) of the word forms a palindrome.
The function allValidSuffixes finds all such suffixes. For example, the "valid suffixes" of the word "exempt" are "xempt" (remove "e") and "mpt" (remove 'exe').
We'll call a prefix a "valid prefix" of a word if the remainder (suffix) of the word forms a palindrome.
The function allValidPrefixes finds all such prefixes in a similar way to how the allValidSuffixes function does.
It is possible to combine more of the code for these functions here, but after going back and forth on the issue, I decided against it for this explanation because while it decreases the length of the code and some repetition, the cognitive load to understand it is higher.
In your own code, it would be fine to combine it.
    Examples of case 1 can be found by reversing the current word and looking it up.
    One edge case to be careful of is that if a word is a palindrome by itself, then we don't want to add a pair that includes that same word twice.
    This case only comes up in case 1, because case 1 is the only case that deals with pairs where the words are of equal length.

    Examples of case 2 can be found by calling allValidSuffixes and then reversing each of the suffixes found and looking them up.

    Examples of case 3 can be found by calling allValidPrefixes and then reversing each of the prefixes found and looking them up.

It would be possible to simplify further (not done here) by recognizing that case 1 is really just a special case of case 2 and case 3.
This is because the empty string is a palindrome prefix/ suffix of any word.

"""

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]: 
        res = set()
        mirror = {w[::-1]: i for i, w in enumerate(words)}
        
        for i, w in enumerate(words):
            for k in range(len(w) + 1):
                prefix, suffix = w[:k], w[k:]
                if prefix in mirror and mirror[prefix] != i and suffix == suffix[::-1]:
                    res.add((i, mirror[prefix]))
                if suffix in mirror and mirror[suffix] != i and prefix == prefix[::-1]:
                    res.add((mirror[suffix], i))
                    
        return [[i, j] for i, j in res]

# Brute Force
# Time Complexity : O(n^2 * k)
# Space Complexity : O(n * k + n ^ 2)

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def isPalindrome(word):
            if len(word) <= 1: return True
            return word == word[::-1]
        
        result = []
        
        for i in range(len(words)):
            for j in range(len(words)):
                string = ""
                if i != j: 
                    string += words[i] + words[j]
                    if isPalindrome(string):
                        result.append([i,j])
        return result