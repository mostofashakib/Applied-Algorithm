"""
LeetCode Problem 380. Insert Delete GetRandom O(1)
Link: https://leetcode.com/problems/insert-delete-getrandom-o1/
Language: Python
Written by: Mostofa Adib Shakib
"""

# Optimal solution
# Time Complexity: O(1)
# Space Complexity: O(n)

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # The hashmap stores the key and the index of the key as a key, value pair
        # the array stores the element as they appear in the sequence

        self.hashmap = {}
        self.array = []
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """

        # checks if the element is present in the hashmap. If present then return False
        # if the element is not present in the hashmap then it gets the new index of the element in the array
        # add the element in a key, value pair and return's True

        if val not in self.hashmap:
            index = len(self.array)
            self.hashmap[val] = index
            self.array.append(val)
            return True
        else:
            return False
                    

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """

        # checks if the element is present in the hashmap. If the element is not present then return False
        # if the element is present in the hashmap then it gets the index of the element in the array
        # move the last element to the place idx of the element to delete the last element from the array
        # also remove it from the hashmap.

        if val not in self.hashmap:
            return False
        else:
            index = self.hashmap[val]
            last_element = self.array[-1]
            self.array[index] = last_element
            self.hashmap[last_element] = index
            self.array.pop()
            del self.hashmap[val]
            return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """

        # gets the length of the array
        # uses the random function to generate a random index in the range
        # returns the element located at the index selected randomly

        length = len(self.array)
        index = random.randint(0, length-1)
        return self.array[index]

# Inefficient solution
# Time Complexity: O(n)
# Space Complexity: O(n)

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.randomSet = set()
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.randomSet:
            self.randomSet.add(val)
            return True
        else:
            return False
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.randomSet:
            return False
        else:
            self.randomSet.remove(val)
            return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        length = len(self.randomSet)
        ranVal = random.randint(0, length-1)
        randomArray = list(self.randomSet)
        val  = randomArray[ranVal]
        return val


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()