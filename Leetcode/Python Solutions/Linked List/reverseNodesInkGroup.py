"""
LeetCode Problem: 25. Reverse Nodes in k-Group
Link: https://leetcode.com/problems/reverse-nodes-in-k-group/
Language: Python
Written by: Mostofa Adib Shakib

Time complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        root = ListNode(0, head)
        cur = root.next
        prev = root
        
        while cur:
            tail = cur
            listIndex = 0    
            
            while cur and listIndex < k:
                cur = cur.next
                listIndex +=1
                
            if listIndex == k:
                prev.next= self.reverseLinkedList(tail, k)
                prev = tail
                
            # last node when iters are not evenly distributed
            else:
                prev.next = tail
                
        return root.next
    
    #Normal LL reversing but with a k
    def reverseLinkedList(self, head: ListNode, k: int) -> ListNode:
        prevNode= None
        
        while head and k:
            nextNode = head.next
            head.next = prevNode
            prevNode = head
            head = nextNode
            k-=1

        return prevNode