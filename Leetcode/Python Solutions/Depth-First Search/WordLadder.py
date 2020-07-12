"""
LeetCode Problem: 127. Word Ladder
Link: https://leetcode.com/problems/word-ladder/
Language: Python
Written by: Mostofa Adib Shakib

"""

# One directional BFS traversal
# Time Complexity: O (M (length of wordList) * N (word length) * N (slicing word)) 
# Space Complexity: O (M)

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    
        words = set(wordList)

        if endWord not in words:
            return 0

        q = collections.deque([(beginWord,1)])

        while q:
            word, steps = q.popleft()
            if word == endWord:
                return steps
            else:
                for i in range(len(word)):
                    for char in range(ord('a'), ord('z')+1):
                        # chr converts a unicode to a string
                        newWord = word[:i] + chr(char) + word[i+1:]
                        if newWord in words:
                            words.remove(newWord)
                            q.append((newWord, steps+1))      
        return 0

# Efficient
# Bi-directional BFS traversal

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        
        dictionary = defaultdict(set)
        for word in wordList+[beginWord]:
            for i in range(len(word)):
                dictionary[word[:i]+'*'+word[i+1:]].add(word)
                
        beginQueue,beginVisit,endQueue,endVisit = [(beginWord, 1)],{beginWord: 1},[(endWord, 1)],{endWord: 1}
        queues = [(beginQueue, beginVisit, endVisit),(endQueue, endVisit, beginVisit)]

        while beginQueue and endQueue:
            # below is the juice
            for queue,visited,target in queues:
                word, step = queue.pop(0)
                for i in range(len(word)):
                    for next_word in dictionary[word[:i]+'*'+word[i+1:]]:
                        if next_word in target:
                            return target[next_word]+step
                        else:
                            if next_word not in visited:
                                visited[next_word] = step + 1
                                queue.append((next_word,step + 1))
        return 0