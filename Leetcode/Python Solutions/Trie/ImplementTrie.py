"""
LeetCode Problem: 208. Implement Trie
Link: https://leetcode.com/problems/implement-trie-prefix-tree/
Language: Python
Written by: Mostofa Adib Shakib

Time complexity : O(m)   where m is the key length.
Space complexity : O(m)
"""

class TrieNode:
    def __init__(self):
        self.children = [0] * 26         # initializing an array of chars
        self.isWord = False              # a boolean flag to check if a word is complete

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()           # creates a Trie node
        
    def _char_to_index(self, char):
        return ord(char) - ord("a")      # find an index of the char
    
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        start = self.root                # creates a copy of the root node
        
        for char in word:               # loops over all the characters of the word
            index = self._char_to_index(char)
            
            if not start.children[index]:               # if the char is not present in the array.
                start.children[index] = TrieNode()      # initializes a new trinode
                
            start = start.children[index]               # moves the start pointer to it's appropriate position
            
        start.isWord = True                             # initializes end of word to be true
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        
        start = self.root
        
        for char in word:
            index = self._char_to_index(char)
            
            if not start.children[index]:               # if the char is not present in the array.
                return False
            start = start.children[index]
            
        if start.isWord: return True                    # checks to see if it's a complete word.

        return False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        start = self.root
        
        for char in prefix:
            index = self._char_to_index(char)
            
            if not start.children[index]:
                return False
            start = start.children[index]
    
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)