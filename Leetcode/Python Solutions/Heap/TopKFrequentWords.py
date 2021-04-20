"""
LeetCode Problem: 692. Top K Frequent Words
Link: https://leetcode.com/problems/top-k-frequent-words/
Language: Python
Written by: Mostofa Adib Shakib

Approach:
    Use dict to find count of words
    Add words and count to heap with negative count[by-default its min-heap, and we want max heap]
    
    For adding words to heap:
        1. If more than 1 word have same length then
            add on basis of alphabetic increasing order (sort again).
"""

# Solution 1: Heap
# Time Complexity: O(nlogk)
# Space Complexity: O(n)

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        result = []
        hashmap = {}
        maxHeap = []
        
        for i in words:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
        
        for key, value in hashMap.items():
            # multiply frequency by -1 to transform a minheap to max heap
            heapq.heappush(maxHeap, (-value, key))
        
        result = []
        
        while maxHeap and k > 0:
            result.append(heapq.heappop(maxHeap)[1])
            k -= 1
        
        return result

# Solution 2: Sorting
# Time Complexity: O(nlogn)
# Space Complexity: O(n)

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]: 
        words.sort()
        
        hashmap = {}
        
        for i in words:
            if i not in hashmap:
                hashmap[i] = 1
                
            else:
                hashmap[i] += 1
                
        ans = []
        
        hashmap = sorted(hashmap.items(), key = operator.itemgetter(1), reverse = True)
        
        for i in range(len(hashmap)):
            if k > 0:
                    ans.append(hashmap[i][0])
                    k -= 1
            
        return ans
