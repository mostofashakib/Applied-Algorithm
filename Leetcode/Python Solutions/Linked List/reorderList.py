"""
LeetCode Problem: 143. Reorder List
Link: https://leetcode.com/problems/reorder-list/
Language: Python
Written by: Mostofa Adib Shakib
"""

# Efficient-Solution
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
        
        prev_node, next_node = None, None
        curr = slow
        
        while curr:
            next_node = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = next_node
        
        first, second = head, prev_node
            
        while second.next:
            temp = first.next
            first.next = second
            first = temp
            
            temp = second.next
            second.next = first
            second = temp


# Brute-Force Solution
# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        
        hashmap = {}
        length = 0
        cur = head
        possible = []
        
        while cur:
            hashmap[cur] = cur.next
            possible.append(cur)
            cur = cur.next
            length += 1
        
        i = 0
        mid = length//2
        cur = head
        
        while i < mid:
            temp = cur
            cur.next = hashmap[possible[length-i-2]]
            cur = cur.next
            cur.next = hashmap[temp]
            cur = cur.next
            i += 1
        
        cur.next = None