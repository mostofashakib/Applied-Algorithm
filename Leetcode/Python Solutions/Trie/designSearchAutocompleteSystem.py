"""
LeetCode Problem: 642. Design Search Autocomplete System
Link: https://leetcode.com/problems/design-search-autocomplete-system/
Language: Python
Written by: Mostofa Adib Shakib

L = Length of the sentence array
k = Average length of each word in the sentence array.

Time Complexity: O(K * L)
Space Complexity: O(N)
"""

class TrieNode:
    def __init__(self, text):
        self.children = defaultdict(list)
        self.text = text
        self.freq = 0
        self.isWord = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode("")
        
    def insert(self, word, time):
        current = self.root
        
        for i, char in enumerate(word):
            if char not in current.children:
                prefix = word[:i+1]
                current.children[char] = TrieNode(prefix)
            current = current.children[char] 
        
        current.freq += time
        current.isWord = True
    
    def search(self, char, node):
        maxHeap = []
        
        def __starts__with(char, node):
            if not node:
                return
            
            if node.isWord:
                maxHeap.append((-node.freq, node.text))
            
            for child in node.children:
                __starts__with(child, node.children[child])
                
        __starts__with(char, node)
        heapq.heapify(maxHeap)
        result = []
        
        for _ in range(3):
            if maxHeap:
                result.append(heapq.heappop(maxHeap)[1])
        
        return result
        
class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.trieFinder = Trie()
        self.currentNode = self.trieFinder.root
        self.currentInput = ""
        
        for sentence, time in zip(sentences, times):
            self.trieFinder.insert(sentence, time)
        
    def input(self, c: str) -> List[str]:
        if c == "#":
            self.trieFinder.insert(self.currentInput, 1)
            self.currentInput = ""
            self.currentNode = self.trieFinder.root
            return []
        else:
            if not self.currentNode or c not in self.currentNode.children:
                self.currentInput += c
                self.currentNode = None
                return []
            else:          
                self.currentInput += c
                self.currentNode = self.currentNode.children[c]
                return self.trieFinder.search(c, self.currentNode)