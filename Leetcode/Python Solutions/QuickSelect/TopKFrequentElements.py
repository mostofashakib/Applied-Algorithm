"""
LeetCode Problem: 347. Top K Frequent Elements
Link: https://leetcode.com/problems/top-k-frequent-elements/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(1)
"""

# QuickSelect

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
        
        unique = list(hashmap.keys())
        
        def partition(left, right, pivot_index):
            pivot = hashmap[unique[pivot_index]]
            # 1. move pivot to end
            unique[pivot_index], unique[right] = unique[right], unique[pivot_index]  
            
            # 2. move all smaller elements to the left
            store_index = left
            for i in range(left, right):
                if hashmap[unique[i]] < pivot:
                    unique[store_index], unique[i] = unique[i], unique[store_index]
                    store_index += 1

            # 3. move pivot to its final place
            unique[right], unique[store_index] = unique[store_index], unique[right]  
            
            return store_index
        
        def select(left, right, k_smallest):
            """
            Returns the k-th smallest element of list within left..right
            """
            if left == right:       # If the list contains only one element,
                return   # return that element
            
            # select a random pivot_index between 
            pivot_index = random.randint(left, right)     
                            
            # find the pivot position in a sorted list   
            pivot_index = partition(left, right, pivot_index)
            
            # the pivot is in its final sorted position
            if k_smallest == pivot_index:
                 return
            # go left
            elif k_smallest < pivot_index:
                select(left, pivot_index - 1, k_smallest)
            # go right
            else:
                select(pivot_index + 1, right, k_smallest)

        n = len(unique)
        select(0, n - 1, n - k)
        
        return unique[n - k:]

# Sorting
# Time Complexity: NlogN

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
                
        hashmap = sorted(hashmap.items(), key = operator.itemgetter(1), reverse = True)
        ans = []
        
        for i in hashmap:
            if k > 0:
                ans.append(i[0])
                k -= 1
        return ans