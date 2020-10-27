"""
LeetCode Problem: 160. Intersection of Two Linked Lists
Link: https://leetcode.com/problems/intersection-of-two-linked-lists/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        visited = set()
        
        while headA:
            visited.add(headA)          # Store a node's reference in the hashSet
            headA = headA.next          # Traverse to the next node
            
        while headB:
            if headB in visited:        # If a node in B already exists in the hashSet that means we have found the point of intersection
                return headB
            else:
                headB = headB.next      # If you haven't found the point of intersection then move to the next node
        
        return None                     # If the two linkedLists doesn't have any point of intersection