"""
LeetCode Problem: 146. LRU Cache
Link: https://leetcode.com/problems/lru-cache/
Language: Python3
Written by: Mostofa Adib Shakib
"""

# Making a doubly linked list

class DoubleLL:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.curr_length = 0
        
        self.head = DoubleLL(0)
        self.tail = DoubleLL(0)
        
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def move_to_front(self, node):
        temp = self.head.next
        
        self.head.next = node
        node.prev = self.head
        
        node.next = temp
        temp.prev = node
    
    def remove_from_tail(self, node):
        temp_next = node.next
        temp_before = node.prev
        
        temp_before.next = temp_next
        temp_next.prev = temp_before
        
        return node
        
    def get(self, key: int) -> int:
        #check if key exists in hashmap
        
        if key in self.hashmap:
            #delete from tail
            node = self.remove_from_tail(self.hashmap[key][1])
            # move to the front
            self.move_to_front(node)

            return self.hashmap[key][0]
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        #check if key exists in hashmap
        if key in self.hashmap:
            #remove from tail
            node = self.remove_from_tail(self.hashmap[key][1])
            #move to front 
            self.move_to_front(node)
            #update the value in hashmap
            self.hashmap[key][0] = value
        else:
            #if the length is less than the capacity
            if self.curr_length < self.capacity:
                #move a new node
                new_node = DoubleLL(key)
                #put value in hashmap
                self.hashmap[key] = [value, new_node]
                #move to front
                self.move_to_front(new_node)
                #increase the length by 1
                self.curr_length += 1
            else:
                #if the length is more than or equal to the capacity

                #access the last element
                last_node = self.tail.prev
                old_key = last_node.val

                #remove the last element
                self.remove_from_tail(last_node)
                                
                #remove info from hashmap
                self.hashmap.pop(old_key)
                
                self.curr_length -= 1

                #put the new node
                self.put(key, value)
                
                
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)