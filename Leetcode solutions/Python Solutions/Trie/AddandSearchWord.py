"""
LeetCode Problem: 211. Add and Search Word - Data structure design
Link: https://leetcode.com/problems/add-and-search-word-data-structure-design/
Language: Python
Written by: Mostofa Adib Shakib
"""

class TrieNode:
    def __init__(self):
        self.children = [0] * 26
        self.isWord = False
        
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        
    def _char_to_index(self, char):
        return ord(char) - ord("a")

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        start = self.root
        
        for char in word:
            index = self._char_to_index(char)
            if not start.children[index]:
                start.children[index] = TrieNode()
            start = start.children[index]
        start.isWord = True
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.searchWithNode(self.root, word, 0, len(word))
        
    def searchWithNode(self, node, word, idx, ln):
        if idx == ln:                # checks if the current index is equal to the length of the word
            return node.isWord
        
        char = word[idx]             # gets the char at the given index
        
        if char == ".":
            for child in node.children:
                if child and self.searchWithNode(child, word, idx + 1, ln):        # if a child exists then recursively check if any link also exists
                    return True
        else:
            index = self._char_to_index(char)           # converts the char to an index
            if not node.children[index]:                # if no further link exists
                return False
            return self.searchWithNode(node.children[index], word, idx + 1, ln)   # if link exists check then char at the next index.
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)