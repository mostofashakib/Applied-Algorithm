"""
LeetCode Problem: 706. Design HashMap
Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
Language: Python
Written by: Mostofa Adib Shakib

N: The number of all possible keys
K: The number of predefined cell in the hashmap, which is 99371 in our case

Time complexity: O(K/N)
Space Complexity: O(K)
"""

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Use a large prime number for less collision
        # 99371 is a large prime number
        
        self.HashMap = [ -1 for i in range(99371)]
        
    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        key_value = self.hashing(key)
        self.HashMap[key_value] = value
    
    def hashing(self, keyvalue):
        return keyvalue % len(self.HashMap)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        key_value = self.hashing(key)
        if self.HashMap[key_value] != -1:
            return self.HashMap[key_value]
        else:
            return -1
        
    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        key_value = self.hashing(key)
        self.HashMap[key_value] = -1

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)